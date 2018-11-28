#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <numeric>
#include <algorithm>
using namespace std;
#ifdef DEBUGRUN
#define LOG(a) (cerr<<__LINE__<<": "#a" = "<<(a)<<endl)
#define DBG(...) (__VA_ARGS__)
#else
#define LOG(...) ((void)0)
#define DBG(...) ((void)0)
#endif
#define rep(i, n) for(int i=0; i<(int)(n); i++)
#define mp make_pair
#define foreach(it, c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
typedef long long Int;
#define INF (MY_INFINITY)
#define MOD (YOUR_MODULUS)

char f[100][100];
int w[100][100];

void solve() {
    int R, C, D;
    scanf("%d%d%d", &R, &C, &D);
    rep(i, R) rep(j, C) scanf(" %c", f[i]+j);
    rep(i, R) rep(j, C) w[i][j] = D + f[i][j]-'0';
    int ans = -1;
    rep(i, R) rep(j, C) for(int k=3; k<20; k++) {
        double ux=0, uy=0;
        int sx, ex, sy, ey;
        if(k%2) sx=i-k/2, ex=i+k/2, sy=j-k/2, ey=j+k/2;
        else sx=i-k/2, ex=i+k/2-1, sy=j-k/2, ey=j+k/2-1;
        if(sx<0 || ex>=R || sy<0 || ey>=C) continue;
        double cx = (sx+ex)/2.0;
        double cy = (sy+ey)/2.0;
        for(int x=sx; x<=ex; x++) for(int y=sy; y<=ey; y++) {
            if(x==sx && y==sy) continue;
            if(x==sx && y==ey) continue;
            if(x==ex && y==sy) continue;
            if(x==ex && y==ey) continue;
            ux += (cx-x)*w[x][y];
            uy += (cy-y)*w[x][y];
        }
        if(ux==0 && uy==0) {
            LOG(i);
            LOG(j);
            LOG(sx);
            LOG(ex);
            LOG(sy);
            LOG(ey);
            ans = max(ans, k);
        }
    }
    if(ans==-1) puts("IMPOSSIBLE");
    else printf("%d\n", ans);
}

int main() {
    int T;
    scanf("%d", &T);
    rep(t, T) {
        printf("Case #%d: ", t+1);
        solve();
    }
    return 0;
}



