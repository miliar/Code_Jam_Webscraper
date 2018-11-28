#include <iostream>
#include <string>
#include <list>
#include <algorithm>

//#define DEBUG
//#define UNIT_TEST

// Algorithm:
// ARGH: use next_permutation, if returns false, figure out which digit to add
// ARGH!! doesn't include 0 in definition.


// If not all digits are in descending order, 
// find the rightmost subset that is in descending order
// take the rightmost number in that subset and move it before
// the number before the subset (zeros screw this up) 
// if the rightmost is a zero, pick the first nonzero number from the
// right in the subset, move that before the number before the subset,
// and reorder the subset in ascending order

// 189 -> 198 -> 819 -> 891  

// 109 -> 190 -> 901 -> 910

// If all digits in decending order, switch them to ascending order
// and, if there are any ones digits, add a zero after the first digit.
// If there are no ones digits, add a one to the front.
//nonono
// 2205 -> 12205


class Num
{
#ifdef UNIT_TEST
public:
#else
private:
#endif
    typedef std::list<int> num_t;
    num_t m_num;

num_t make_num(const std::string& str)
{
    num_t result;
    for (std::string::const_iterator c = str.begin(); c != str.end(); ++c)
    {
        result.push_back(*c - '0');
    }
    return result;
}

    bool is_maximal()
    {
        int max = 10;

        for (num_t::const_iterator i = m_num.begin(); i != m_num.end(); ++i)
        {
            if (*i > max)
                return false;
            else max = *i;
        }
        return true;
    }
#if 0
    int lowest_not_represented(bool but_not_zero = false)
    {
        int min = but_not_zero ? 1 : 0;

        num_t copy = m_num;
        copy.sort();

        for (num_t::const_iterator i = copy.begin(); i != copy.end(); ++i)
        {
            if (*i == min)
            {
                ++min;
            }
            else if (*i > min)
            {
                return min;
            }
        }

        return min;
    }
#endif

    void add_digit()
    {
        m_num.push_front(0);
        fix_initial_zero();
    }

    void fix_initial_zero()
    {
        if (!m_num.empty() && *m_num.begin() == 0)
        {
            // move first nonzero number before all zeros
            for (num_t::iterator i = m_num.begin(); i != m_num.end(); ++i)
            {
                if (*i != 0)
                {
                    m_num.push_front(*i);
                    m_num.erase(i);
                    break;
                }
            }
            
        }
    }

    const Num& make_minimal()
    {
        m_num.sort();
        fix_initial_zero();
        return *this;
    }

    const Num& next_reorder()
    {
        assert(std::next_permutation(m_num.begin(), m_num.end()));
        return *this;
    }

public:
    Num(const std::string& str)
    {
        m_num = make_num(str);
    }

    void next_num()
    {
        if (is_maximal())
        {
            m_num.sort();
            add_digit();
        }
        else
        {
            next_reorder();
        }
    }

    std::string to_str() const
    {
        char result_cstr[32] = {};
        int r_i = 0; 

        for (num_t::const_iterator i = m_num.begin(); i != m_num.end(); ++i, ++r_i)
        {
            result_cstr[r_i] = (char)*i + '0';    
        }

        return result_cstr;
    }
};



void output(const Num& result, size_t line)
{
    std::cout << "Case #" << line + 1 << ": " << result.to_str() << std::endl;
}

int main()
{
#ifdef UNIT_TEST
    assert(Num("987654321").is_maximal());
    assert(!Num("987654312").is_maximal());
    assert(Num("990").is_maximal());
    assert(!Num("909").is_maximal());

    assert(Num("987").make_minimal().to_str() == std::string("789"));
    assert(Num("9870").make_minimal().to_str() == std::string("7089"));
    assert(Num("40102").make_minimal().to_str() == std::string("10024"));
    assert(Num("1002").make_minimal().to_str() == std::string("1002"));

    assert(Num("987").lowest_not_represented() == 0);
    assert(Num("9870").lowest_not_represented() == 1);
    assert(Num("98710").lowest_not_represented() == 2);
    assert(Num("928710").lowest_not_represented() == 3);
    assert(Num("101234558").lowest_not_represented() == 6);
#endif

    size_t numcases;
    std::cin >> numcases;
#ifdef DEBUG
    std::cout << numcases << " cases" << std::endl;
#endif
    for (size_t casex = 0; casex < numcases; ++casex)
    {
        std::string numstr;
        std::cin >> numstr;
#ifdef DEBUG
        std::cout << "in: " << numstr << std::endl;
#endif
        Num num(numstr);
        num.next_num();
        //double result = racket.calculate();
        output(num, casex);
    }

    return 0;
}
