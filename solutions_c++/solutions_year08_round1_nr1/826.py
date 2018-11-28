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


int main(int argc, char* argv[])
{
    int T, N;

    cin >> T;

    for (int t = 0; t < T; ++t) {
        cin >> N;

        vector<int> v1;
        vector<int> v2;

        for (int n = 0; n < N; ++n) {
            int x;
            cin >> x;
            v1.push_back(x);
        }
        for (int n = 0; n < N; ++n) {
            int y;
            cin >> y;
            v2.push_back(y);
        }

        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());

        int64_t products = LONG_MAX;

        do {
            int64_t sum = 0;
            for (int n = 0; n < N; ++n) {
                sum += (int64_t)v1[n] * v2[n];
            }
            products = min(products, sum);
        } while (next_permutation(v1.begin(), v1.end()));

        printf("Case #%d: %lld\n", t+1, products);
    }

    return 0;
}

