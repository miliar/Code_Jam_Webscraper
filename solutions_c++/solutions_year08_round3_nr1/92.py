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
    int T;
    cin >> T;

    for (int Case = 1; Case <= T; ++Case) {
        int P, K, L;
        cin >> P >> K >> L;

        printf("Case #%d: ", Case);

        if (P * K < L) {
            printf("Impossible\n");
            continue;
        }

        vector<int64_t> freq(L);
        for (int i = 0; i < L; ++i) {
            cin >> freq[i];
        }

        sort(freq.begin(), freq.end(), greater<int64_t>());

        int64_t result = 0;

        for (int i = 0; i < L; ++i) {
            result += freq[i] * (i / K + 1);
        }

        printf("%lld\n", result);
    }

    return 0;
}

