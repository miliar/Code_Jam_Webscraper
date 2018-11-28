#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

typedef long long ll;

using namespace std;

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T, N, L, H, freq[120], ans;
    bool can;
    scanf("%d",&T);
    for (int tc = 1; tc <= T; ++tc) {
        scanf("%d%d%d",&N,&L,&H);
        REP(i,N) scanf("%d", &freq[i]);

        FOR(j,L,H+1) {
            can = true;
            REP(i,N) {
                if (j%freq[i]!=0&&freq[i]%j!=0) {
                    can = false;
                    break;
                }
            }
            if (can) {
                ans = j;
                break;
            }
        }
        printf("Case #%d: ", tc);
        if (!can) puts("NO");
        else printf("%d\n",ans);
    }
    return 0;
}
