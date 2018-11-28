#include <iostream>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <stdint.h>

//#define DEBUG

void output(int64_t result, size_t line)
{
    std::cout << "Case #" << line + 1 << ": " << result << std::endl;
}

class PermVec
{
private:
    typedef std::multiset<int32_t, std::less<int32_t> > m_set_t;
    m_set_t m_set;

public:
    PermVec() {};

    void insert(int32_t num)
    {
        m_set.insert(num);
    }

    int32_t pop_big()
    {
        int32_t result = *m_set.rbegin();
        m_set.erase(m_set.find(result));
#ifdef DEBUG
        printf("pop_big: %d size(%d)\n", result, m_set.size());
#endif
        return result;
    }

    int32_t pop_small()
    {
        int32_t result = *m_set.begin();
        m_set.erase(m_set.begin());
#ifdef DEBUG
        printf("pop_small: %d size(%d)\n", result, m_set.size());
#endif
        return result;
    }

    size_t size()
    {
        return m_set.size();
    }

};

int64_t minimize(PermVec a, PermVec b)
{
    int64_t result = 0;
    size_t size = a.size();
    for (int i = 0; i < size; ++i)
    {
        result += a.pop_big() * b.pop_small();
    }
    return result;
}
    

int main()
{
    size_t numlines;
    std::cin >> numlines;

    for (size_t line = 0; line < numlines; ++line)
    {
        size_t numcases;
        std::cin >> numcases;
        PermVec a, b;
        for (size_t item = 0; item < numcases; ++item)
        {
            int32_t num;
            std::cin >> num;
            a.insert(num);
        }
        for (size_t item = 0; item < numcases; ++item)
        {
            int32_t num;
            std::cin >> num;
            b.insert(num);
        }
        int64_t result_ab = minimize(a, b);
        int64_t result_ba = minimize(b, a);
        if (result_ab < result_ba)
            output(result_ab, line);
        else
            output(result_ba, line);
    }

    return 0;
}
