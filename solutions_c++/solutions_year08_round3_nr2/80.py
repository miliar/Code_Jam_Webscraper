#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <cmath>
#include <functional>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <numeric>
#include <utility>
#include <cfloat>

using namespace std;

typedef long long int64_t;

template <typename T, int N>
inline size_t length_of(T(&)[N]) throw() { return N; }


vector<int64_t> eval(string s)
{
    vector<int64_t> result;
    int64_t n;
    sscanf(s.c_str(), "%lld", &n);

    result.push_back(n);

    for (int k = 0; k < s.size()-1; ++k) {
        vector<int64_t> b = eval(s.substr(k+1));
        vector<int64_t> a(1);

        sscanf(s.substr(0, k+1).c_str(), "%lld", &a[0]);

        for (vector<int64_t>::iterator i = a.begin(); i != a.end(); ++i)
        for (vector<int64_t>::iterator j = b.begin(); j != b.end(); ++j)
        {
            int64_t a = *i + *j;
            int64_t b = *i - *j;

            result.push_back(*i + *j);
            result.push_back(*i - *j);
        }
    }

    return result;
}

int main(int argc, char* argv[])
{
    int N;
    cin >> N;

    for (int Case = 1; Case <= N; ++Case) {
        string s;
        cin >> s;
        vector<int64_t> numberes = eval(s);

        vector<int64_t>::iterator iter = numberes.begin();
        vector<int64_t>::iterator end = numberes.end();

        int64_t result = 0;

        for (; iter != end; ++iter) {
            const int primes[] = { 2, 3, 5, 7 };
            const int64_t k = *iter > 0 ? *iter : -*iter;

            for (int i = 0; i < length_of(primes); ++i) {
                if (k % primes[i] == 0) {
                    ++result;
                    break;
                }
            }
        }

        printf("Case #%d: %lld\n", Case, result);
    }

    return 0;
}

