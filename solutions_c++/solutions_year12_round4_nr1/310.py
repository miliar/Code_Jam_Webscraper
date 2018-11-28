#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

int T;

int n;
int d[10010];
int l[10010];
int dp[10010];
int D;
bool good;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d ", &T);
    forn(t, T) {
        scanf("%d", &n);
        forn(i, n) {
            scanf("%d%d", &d[i], &l[i]);
            dp[i] = -1;
        }
        scanf("%d", &D);
        good = 0;
        dp[0] = d[0];
        forn(i, n) {
            if (D - d[i] <= dp[i]) good = 1;
            if (dp[i] != -1)
                forab(j, i + 1, n)
                    if (d[i] + dp[i] >= d[j])
                        dp[j] = max(dp[j], min(d[j] - d[i], l[j]));
        }

        printf("Case #%d: ", t + 1);

        if (good) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
