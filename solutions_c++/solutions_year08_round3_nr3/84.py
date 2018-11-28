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

const int MOD = 1000000007;

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int Case = 1; Case <= T; ++Case) {
        int64_t n, m, X, Y, Z;
        cin >> n >> m >> X >> Y >> Z;

        vector<int64_t> A(m);
        for (int i = 0; i < m; ++i) cin >> A[i];

        vector<int64_t> limits(n);
        for (int i = 0; i < n; ++i) {
            limits[i] = A[i % m];
            A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
        }

        int64_t result = 0;
        vector<int64_t> DP(n);

        for (int i = n-1; i >= 0; --i) {
            DP[i] = 1;
            for (int j = i+1; j < n; ++j)
                if (limits[i] < limits[j]) DP[i] = (DP[i] + DP[j]) % MOD;
            result = (result + DP[i]) % MOD;
        }

        printf("Case #%d: %lld\n", Case, result);
    }

    return 0;
}

