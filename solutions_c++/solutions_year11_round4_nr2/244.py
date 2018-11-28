#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long LL;

const int maxn = 12;
const double eps = 1e-6;

int n, m, D, cas;
int map[maxn][maxn];

bool check(int x0, int y0, int l )
{
    double cx = x0+(double)l/2.0, cy = y0+(double)l/2.0;
    double ansx = 0, ansy = 0;
    for (int i = x0; i<x0+l; i++ )
        for (int j = y0; j<y0+l; j++ )
        {
            if (i == x0 && j == y0) continue;
            if (i == x0 && j == y0+l-1) continue;
            if (i == x0+l-1 && j == y0) continue;
            if (i == x0+l-1 && j == y0+l-1) continue;
            double t = map[i][j];
            ansx += t*(double)(i+0.5-cx);
            ansy += t*(double)(j+0.5-cy);
        }
    return (fabs(ansx)<eps && fabs(ansy)<eps);
}

int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    scanf("%d",&cas);
    for (int run = 1; run<=cas; run++ )
    {
        scanf("%d%d%d",&n,&m,&D);
        for (int i = 0; i<n; i++ )
            for (int j = 0; j<m; j++ )
            {
                int ch = 0;
                while (ch<'0' || ch>'9') ch = getchar();
                map[i][j] = D+ch-'0';
            }
        int ans = 0;
        for (int i = 0; i<n; i++ )
            for (int j = 0; j<m; j++ )
                for (int l = 3; l<=n; l++ )
                {
                    if (i+l>n || j+l>m) break;
                    if (check(i, j, l) && ans<l) ans = l;
                }
        printf("Case #%d: ", run);
        if (ans) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
    }
    //system("pause");
    return 0;
}
