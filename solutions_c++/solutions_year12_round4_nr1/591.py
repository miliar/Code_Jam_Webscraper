#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SZ(X) ((int)(X.size()))
#define REP(I,N) for (int I = 0; I < (N); ++I)
#define FOR(I,L,H) for (int I = (L); I < (H); ++I)
#define MP(X,Y) make_pair((X),(Y))
#define PB push_back
#define ALL(X) X.begin(), X.end()
template <typename T> inline bool checkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template <typename T> inline bool checkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
typedef long long lint;

const int MAXN = 10000 + 10;

lint d[MAXN], l[MAXN], D, dp[MAXN];

int main() {
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int n;  
        scanf("%d", &n);
        REP(i, n) {
            scanf("%I64d%I64d", d + i, l + i);
        }
        memset(dp, 0, sizeof(dp));
        dp[0] = d[0];
        for (int i = 0; i < n; ++i) {
            lint range = d[i] + dp[i];
            //out(i); out(dp[i]); out(range);
            for (int j = i + 1; j < n && range >= d[j]; ++j) {
                //out(j);
                checkmax(dp[j], min(d[j] - d[i], l[j]));
                //out(dp[j]);
            }
        }
        scanf("%I64d", &D);
        printf("Case #%d: ", t);
        bool ans = false;
        for (int i = n - 1; !ans && i >= 0; --i) {
            if (d[i] + dp[i] >= D) {
                ans = true;
            }
        }
        if (ans) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }
    return 0;
}

