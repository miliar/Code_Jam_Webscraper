#include <stdio.h>
#include <memory.h>
#include <algorithm>
#define MN 501
#define ll long long
using namespace std;
int n, m, r;
ll d[MN][MN], dd[MN][MN];
ll x[MN][MN], xx[MN][MN];
ll y[MN][MN], yy[MN][MN];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt, T, i, j, k;
	ll x1, y1, x2, y2;

	scanf("%d",&T);
	for (tt = 1; tt <= T; tt++) {
		printf("Case #%d: ",tt);
		scanf("%d%d%*d",&n,&m);
		memset(d,0,sizeof(d));
		for (i = 1; i <= n; i++) {
			for (j = 1; j <= m; j++) {
				scanf("%1d",&k);
				d[i][j] = k;
			}
		}
		memset(x,0,sizeof(x));
		memset(y,0,sizeof(y));
		for (i = 1; i <= n; i++) {
			for (j = 1; j <= m; j++) {
				x[i][j] = d[i][j]*(2*i+1);
				y[i][j] = d[i][j]*(2*j+1);
			}
		}
		memset(dd,0,sizeof(dd));
		memset(xx,0,sizeof(xx));
		memset(yy,0,sizeof(yy));
		for (i = 1; i <= n; i++) {
			for (j = 1; j <= m; j++) {
				dd[i][j] = dd[i-1][j]+dd[i][j-1]-dd[i-1][j-1]+d[i][j];
				xx[i][j] = xx[i-1][j]+xx[i][j-1]-xx[i-1][j-1]+x[i][j];
				yy[i][j] = yy[i-1][j]+yy[i][j-1]-yy[i-1][j-1]+y[i][j];
			}
		}
		for (r = n+m; r >= 3; r--) {
			for (i = 1; i+r-1 <= n; i++) {
				for (j = 1; j+r-1 <= m; j++) {
					x1 = xx[i+r-1][j+r-1]-xx[i-1][j+r-1]-xx[i+r-1][j-1]+xx[i-1][j-1];
					x1 -= x[i][j]+x[i][j+r-1]+x[i+r-1][j]+x[i+r-1][j+r-1];
					y1 = yy[i+r-1][j+r-1]-yy[i-1][j+r-1]-yy[i+r-1][j-1]+yy[i-1][j-1];
					y1 -= y[i][j]+y[i][j+r-1]+y[i+r-1][j]+y[i+r-1][j+r-1];
					x2 = dd[i+r-1][j+r-1]-dd[i-1][j+r-1]-dd[i+r-1][j-1]+dd[i-1][j-1];
					x2 -= d[i][j]+d[i][j+r-1]+d[i+r-1][j]+d[i+r-1][j+r-1];
					y2 = x2;
					x2 *= i*2 + r;
					y2 *= j*2 + r;
					if (x1 == x2 && y1 == y2) break;
				}
				if (j+r-1 <= m) break;
			}
			if (i+r-1 <= n) break;
		}
		if (r >= 3) printf("%d\n",r);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}