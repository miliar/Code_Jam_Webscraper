#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <climits>
#include <map>
#include <memory.h>
#include <numeric>
#include <string>
#include <sstream>
#include <utility>
#include <vector>
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

int64 vector_to_number(vector<int>& vect)
{
    reverse(ALL(vect));
    int64 result = 0;
    int64 power = 1;
    REP(i, size(vect))
    {
        result += vect[i] * power;
        power *= 10;
    }
    reverse(ALL(vect));
    return result;
}

vector<int> all_permutations;

int64 to_power(int x)
{
    int64 result = 1;
    for (int i = 0; i < x; i++)
    {
        result *= 10;
    }
    return result;
}

int64 concatenate(vector<int>& v1, vector<int>& v2)
{
    int64 result = 0;
    result += vector_to_number(v2);
    result += vector_to_number(v1) * to_power(size(v2));
    return result;
}

void permute(vector<int>& v1, vector<int>& v2)
{
    if (size(v2) <= 1)
    {
        if (v1[0] != 0)
        {
            int64 permutation = concatenate(v1, v2);
            all_permutations.push_back(permutation);
        }
    }
    else
    {
        for (int i = 0; i < size(v2); i++)
        {
            vector<int> new_v2;
            int digit = -1;
            for (int j = 0; j < size(v2); j++)
            {
                if (j == i)
                {
                    digit = v2[j];
                    continue;
                }
                new_v2.push_back(v2[j]);
            }

            vector<int> new_v1 = v1;
            if (digit >= 0 && digit <= 9)
            {
                new_v1.push_back(digit);
            }

            permute(new_v1, new_v2);
        }
    }
}

int64 find_next_number(int64 number)
{
    if (number < 10)
    {
        return number * 10;
    }
    vector<int> digits;
    int n2 = number;
    while (n2 > 0)
    {
        const int digit = n2 % 10;
        n2 /= 10;
        digits.push_back(digit);
    }
    reverse(ALL(digits));

    vector<int> digits_sorted(digits);
    sort(ALL(digits_sorted));
    reverse(ALL(digits_sorted));

    int result = -1;
    if (digits_sorted == digits)
    {
        digits.insert(digits.begin(), 0);
    }

    {
        all_permutations.clear();
        vector<int> dummy;
        permute(dummy, digits);
        int64 best = 0xFFFFFFFFFFFFFFFll;
        for (int i = 0; i < size(all_permutations); i++)
        {
            const int64 permutation = all_permutations[i];
            if (permutation > number && permutation < best)
            {
                best = permutation;
            }
        }
        result = best;
    }

    return result;
}

int main()
{
    int num_cases;
    cin >> num_cases;

    FOR (ii, 1, num_cases)
    {
        int64 number;
        cin >> number;
        printf("Case #%d: %lld\n", ii, find_next_number(number));
    }

    return 0;
}

