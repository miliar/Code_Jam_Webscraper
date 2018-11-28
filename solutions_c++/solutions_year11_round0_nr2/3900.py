#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

//#define DEBUG
//#define UNIT_TEST

// Algorithm:
// Just apply the rules

class Magicka
{
public:
    Magicka()
    {
    }

    void addCombo(const std::string& combo)
    {
        int input = mungeChars(combo[0], combo[1]);
        mCombos[input] = combo[2];
    }

    void addOpp(const std::string& opp)
    {
        mOpps[opp[0]].push_back(opp[1]);
        mOpps[opp[1]].push_back(opp[0]);
    }

    void invoke(const std::string& elements)
    {
        typedef std::string::const_iterator siter_t;

        for (siter_t si = elements.begin(); si != elements.end(); ++si)
        {
            if (mElements.empty())
            {
                mElements.push_back(*si);
                mElementOccurs[*si]++;
                continue;
            }

            // test for combo
            int comboIn = mungeChars(*si, mElements.back());
            if (mCombos.count(comboIn))
            {
                char comboOut = mCombos[comboIn];
#ifdef DEBUG
                std::cout << *si << " + " << mElements.back() << " = " << comboOut << std::endl;
#endif
                mElementOccurs[mElements.back()]--;
                mElements.pop_back();
                mElements.push_back(comboOut);
                mElementOccurs[comboOut]++;
                continue;
            }

            // test for opposition
            typedef std::vector<char>::iterator citer_t;
            std::vector<char>& opps = mOpps[*si];
            bool wiped = false;
            for (citer_t ci = opps.begin(); ci != opps.end(); ++ci)
            {
                if (mElementOccurs[*ci])
                {
                    // wipe
                    mElements.clear();
                    mElementOccurs.clear();
                    wiped = true;
                    break;
                }
            }

            if (!wiped)
            {
                mElements.push_back(*si);
                mElementOccurs[*si]++;
            }
        }
    }

    std::string remains()
    {
        std::string result = "[";
        bool first = true;
        for (vci_t vci = mElements.begin(); vci != mElements.end(); ++vci)
        {
            if (!first) result += ", ";
            result.push_back(*vci);
            first = false;
        }
        result += "]";

        return result;
    }

private:
    typedef std::vector<char>::iterator vci_t;
    std::vector<char> mElements;

    std::map<char, int> mElementOccurs; // parallel data structure for speed

    int mungeChars(char a, char b)
    {
        if (a >= b)
        {
            return a << 8 + b;
        }
        else
        {
            return b << 8 + a;
        }
    }

    typedef std::map<int, char> comboMap_t;
    comboMap_t mCombos;

    typedef std::map<char, std::vector<char> > oppMap_t;
    oppMap_t mOpps;
};


void output(Magicka& result, size_t line)
{
    std::cout << "Case #" << line + 1 << ": " << result.remains() << std::endl;
}

int main()
{
#ifdef UNIT_TEST
#endif
    size_t numcases;
    std::cin >> numcases;
#ifdef DEBUG
    std::cout << numcases << " cases" << std::endl;
#endif
    for (size_t casex = 0; casex < numcases; ++casex)
    {
        size_t numcombos;
        
        std::cin >> numcombos;
#ifdef DEBUG
        std::cout << "numcombos: " << numcombos << std::endl;
#endif
        Magicka mag;

        while (numcombos--)
        {
            std::string combo;
            std::cin >> combo;
            assert(combo.size() == 3);
            mag.addCombo(combo);
        }

        size_t numopps;
        
        std::cin >> numopps;
#ifdef DEBUG
        std::cout << "numopps: " << numopps << std::endl;
#endif
        while (numopps--)
        {
            std::string opp;
            std::cin >> opp;
            assert(opp.size() == 2);
            mag.addOpp(opp);
        }


        size_t num_elements;
        std::string elements;
        
        std::cin >> num_elements >> elements;

        assert(elements.size() == num_elements);

        mag.invoke(elements);

        output(mag, casex);
    }

    return 0;
}
