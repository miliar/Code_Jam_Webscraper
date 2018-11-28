
#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <vector>
#include <map>
#include <ctime>

using namespace std;

#define Rep(i,a,b) for(int i=a;i<b;++i)
#define Repd(i,a,b) for(int i=a,_b=b;i>_b;--i)

typedef long long ll;
const int N = 10005;


int n, d;
int ar[N], br[N];
int dp[N];
bool in[N];
int q[N];

bool DP() {
    memset(in, 0, sizeof (in));
    memset(dp, 0, sizeof (dp));
    int f = 0, r = 0;
    dp[0] = ar[0];
    q[r++] = 0;
    in[0] = true;

    while (f != r) {
        int t = q[f++];
        if (f >= N) f -= N;
        in[t] = false;
        //cout << t <<" " << dp[t] <<" "<< ar[t] << endl;
        if (dp[t] + ar[t] >= d) return true;

        for (int i = t + 1; i < n; ++i) {
            if (dp[t] >= abs(ar[i] - ar[t])) {
                int tm = min(abs(ar[i] - ar[t]), br[i]);
                if (tm > dp[i]) {
                    dp[i] = tm;
                    if (!in[i]) {
                        q[r++] = i;
                        if (r >= N) r -= N;
                        in[i] = true;
                    }
                }
                // cout << "~~" <<t << " " <<  dp[i] <<" " << ar[i] << endl;
            } else {
                // cout << "~~" <<t << " " <<  dp[i] <<" " << ar[i] << endl;
                break;
            }
        }

        for (int i = t - 1; i >= 0; --i) {
            if (dp[t] >= abs(ar[i] - ar[t])) {
                int tm = min(abs(ar[i] - ar[t]), br[i]);
                if (tm > dp[i]) {
                    dp[i] = tm;
                    if (!in[i]) {
                        q[r++] = i;
                        if (r >= N) r -= N;
                        in[i] = true;
                    }
                }
            } else break;
        }
    }
    return false;
}


bool DP1() {
    memset(dp, 0, sizeof (dp));
    dp[0] = ar[0];
    for (int i = 0; i < n - 1; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (ar[i] + dp[i] >= ar[j]) {
                dp[j] = max(dp[j], min(ar[j] - ar[i], br[j]));
            } else break;
        }
        if (dp[i] + ar[i] >= d) return true;
    }
    return dp[n - 1] + ar[n - 1] >= d;
}

int main() {
    int cas, tcas = 0;

    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);

    for (cin >> cas; cas; --cas) {
        printf("Case #%d: ", ++tcas);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", ar + i, br + i);
        }
        scanf("%d", &d);
        if (DP1()) puts("YES");
        else puts("NO");
    }
}