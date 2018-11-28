#include "iostream"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "vector"
#include "queue"
#include "cmath"
#include "string"
#include "cctype"
#include "map"
#include "iomanip"
#include "set"
#include "utility"
using namespace std;
typedef pair<int, int> pii;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sof(x) sizeof(x)
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long
#define maxn 10050
int d[maxn], l[maxn];
int dp[maxn];
int n, dist;
bool solve() {
    memset(dp, 0, sof(dp));
    dp[1] = d[1];
    for(int i = 1; i <= n; i++) {
        if(dp[i]) {
            dp[i] = min(dp[i], l[i]);
            for(int j = i + 1; j <= n; j++) {
                int tmp = d[j] - d[i];
                if(tmp > dp[i]) break;
                if(!dp[j]) dp[j] = tmp;
                else if(tmp > dp[j]) dp[j] = tmp;
            }
        }
    }
    for(int i = 1; i <= n; i++) {
        dp[i] = min(dp[i], l[i]);
    }
    for(int i = 1; i <= n; i++) {
        if(d[i] + dp[i] >= dist) return true;
    }
    return false;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("aout.txt", "w", stdout);
    int T, Case = 1;
    scanf("%d", &T);
    while(T--) {
        scanf("%d", &n);
        for(int i = 1; i <= n; i++) scanf("%d%d", &d[i], &l[i]);
        scanf("%d", &dist);
        printf("Case #%d: ", Case++);
        if(solve()) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
