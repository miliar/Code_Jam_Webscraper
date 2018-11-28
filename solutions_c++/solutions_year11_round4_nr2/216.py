#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

typedef long long LL;

const int MAXN = 12;
const double EPS = 1e-6;

int n,m,D;
int g[MAXN][MAXN];

bool mpoint(int x, int y, int l) {
    double cx = x+l/2.0, cy = y+l/2.0;
    double ansx = 0, ansy = 0;
    for (int i = x; i<x+l; i++ )
        for (int j = y; j<y+l; j++ ) {
            if (i==x && j==y) continue;
            if (i==x && j==y+l-1) continue;
            if (i==x+l-1 && j==y) continue;
            if (i==x+l-1 && j==y+l-1) continue;
            double t = g[i][j];
            ansx += t*(i+0.5-cx);
            ansy += t*(j+0.5-cy);
        }
    return (fabs(ansx)<EPS && fabs(ansy)<EPS);
}

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int ntest;
    scanf("%d",&ntest);
    for (int run = 1; run<=ntest; run++) {
        printf("Case #%d: ",run);
        scanf("%d%d%d",&n,&m,&D);
        for (int i = 0; i<n; i++)
            for (int j = 0; j<m; j++) {
                int ch = 0;
                while (!isdigit(ch)) ch = getchar();
                g[i][j] = D+ch-'0';
            }
        int ans = 0;
        for (int i = 0; i<n; i++)
            for (int j = 0; j<m; j++)
                for (int l = 3; l<=n; l++)
                    if (i+l<=n && j+l<=m)
                        if (mpoint(i,j,l) && ans<l) ans = l;
        if (ans>0) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
