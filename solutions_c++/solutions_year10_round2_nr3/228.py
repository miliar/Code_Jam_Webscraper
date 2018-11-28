/**
 * 1. Compile
 *
 *    g++ -O2 -Wall C.cpp -o C
 *
 * 2. Run
 *
 *    cat input_file_name | ./C > output_file_name
 *
 * Or use the Makefile:
 *
 * http://github.com/doitian/google-code-jam-2010/blob/master/Makefile
 */

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <numeric>
#include <cstdio>
#include <inttypes.h>

using namespace std;

const uint64_t MODULO = 100003UL;

typedef map<pair<unsigned, unsigned>, uint64_t> cache_type;
cache_type cache;

typedef map<pair<unsigned, unsigned>, uint64_t> combination_cache_type;
combination_cache_type combination_cache;

uint64_t combination(unsigned n, unsigned k)
{
    if (n < k)
    {
        return 0;
    }
    if (k == 0 || k == n)
    {
        return 1;
    }

    pair<combination_cache_type::iterator, bool> result =
        combination_cache.insert(make_pair(make_pair(n, k), 0));

    if (result.second)
    {
        result.first->second =
            (combination(n - 1, k) + combination(n - 1, k - 1)) % MODULO;
    }

    return result.first->second;
}

uint64_t solve(unsigned n, unsigned k)
{
    if (k == 1 || (n - 1) == k)
    {
        return 1;
    }

    pair<cache_type::iterator, bool> result =
        cache.insert(make_pair(make_pair(n, k), 0));
    if (result.second)
    {
        uint64_t available = n - k - 1;
        for (unsigned i = 1; i < k; ++i)
        {
            uint64_t selection = k - 1 - i;
            if (selection <= available)
            {
                result.first->second += (
                    (combination(available, selection) * solve(k, i))
                    % MODULO
                );

                result.first->second %= MODULO;
            }
        }
    }

    return result.first->second;
}

int main(int argc, char *argv[])
{
    cout.setf(ios::fixed);
    cout.precision(8);

    unsigned case_count = 0;
    cin >> case_count;

    unsigned n;
    for (unsigned case_number = 1; case_number <= case_count; ++case_number)
    {
        cin >> n;
        uint64_t count = 0;
        for (unsigned k = 1; k < n; ++k)
        {
            count += solve(n, k);
            count %= MODULO;
        }

        cout << "Case #" << case_number << ": "
             << count << endl;
    }

    // cout << solve(5, 1) << endl;
    // cout << solve(5, 2) << endl;
    // cout << solve(5, 3) << endl;
    // cout << solve(5, 4) << endl;

    return 0;
}
