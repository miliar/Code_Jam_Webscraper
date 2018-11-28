#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <array>
#include <complex>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

long long a[100], A[100];
long long b[100], B[100];

int N, M;

long long dp(int n, int m)
{
    if (n >= N || m >= M)
        return 0;

    long long res;
    if (A[n] == B[m]) {
        if (a[n] < b[m]) {
            b[m] -= a[n];
            res = a[n] + dp(n+1, m);
            b[m] += a[n];
        } else {
            a[n] -= b[m];
            res = b[m] + dp(n, m+1);
            a[n] += b[m];
        }
    } else {
        res = max(dp(n+1, m), dp(n, m+1));
    }

    return res;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T && cin >> N >> M; ++i) {
        for (int j = 0; j < N && cin >> a[j] >> A[j]; ++j)
            ;
        for (int j = 0; j < M && cin >> b[j] >> B[j]; ++j)
            ;

        cout << "Case #" << i+1 << ": " << dp(0, 0) << '\n';
    }
}
