#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <climits>
#include <map>
#include <memory.h>
#include <numeric>
#include <utility>
#include <vector>
#include <sstream>
using namespace std;

#define FOREACH(it, c) for (__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return static_cast<int>(c.size()); }

string read_line()
{
    string line;
    char buf[2048];
    cin.getline(buf, sizeof(buf));
    line = buf;
    return line;
}

typedef map<int, bool> cache_type;
cache_type happy_cache[11];

int convert_base(int from, int from_base, int to_base)
{
    int number = 0;

    int power = 1;
    while (from > 0)
    {
        const int digit = from % 10;
        from /= 10;

        assert(digit < from_base);

        number += power * digit;
        power *= from_base;
    }

    int to = 0;
    power = 1;
    while (number > 0)
    {
        const int digit = number % to_base;
        number /= to_base;

        to += power * digit;
        power *= 10;
    }

    return to;
}

bool is_happy(int n, int base)
{
    assert(base >= 2);
    assert(base <= 10);

    if (n == 1)
    {
        return true;
    }

    cache_type &cache = happy_cache[base];
    cache_type::iterator iter = cache.find(n);
    if (iter != cache.end())
    {
        return cache[n];
    }

    int n_b = n;

    int sum = 0;
    while (n_b > 0)
    {
        const int digit = n_b % 10;
        n_b /= 10;
        sum += digit * digit;
    }

    cache[n] = false; // to avoid cycles
    bool result = is_happy(convert_base(sum, 10, base), base);
    cache[n] = result;
    return result;
}

int main()
{
    int num_cases;
    cin >> num_cases;

    // flush input stream
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    FOR (ii, 1, num_cases)
    {
        string line = read_line();
        vector<int> bases;

        istringstream iss(line);
        while (iss)
        {
            int base;
            iss >> base;
            bases.push_back(base);
        }
        bases.pop_back();

        int n;
        for (n = 2;; n++)
        {
            bool all_happy = true;
            for (int i = 0; i < size(bases); i++)
            {
                const int base = bases[i];
                if (!is_happy(convert_base(n, 10, base), base))
                {
                    all_happy = false;
                    break;
                }
            }
            if (all_happy)
            {
                break;
            }
        }

        printf("Case #%d: %d\n", ii, n);
    }

    return 0;
}

