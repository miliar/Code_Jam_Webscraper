#include <cstdio>
#include <cstring>
using namespace std;

bool g[2][2000][2000];
int n,x1,y1,x2,y2;

int main() {
	int cases;
	scanf("%d",&cases);
	for (int cc=1;cc<=cases;cc++) {
		scanf("%d",&n);
		memset(g,0,sizeof(g));
		int xx=0,yy=0;
		for (int i=1;i<=n;i++) {
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (int x=x1;x<=x2;x++)
				for (int y=y1;y<=y2;y++) {
					g[0][x][y]=true;
					if (x>xx) xx=x;
					if (y>yy) yy=y;
				}
		}
		if (n==0) {
			printf("Case #%d: 0\n",cc);
			continue;
		}
		int now=1,last=0,ans=0;
		while (1) {
			int tx=xx,ty=yy;
			ans++;
			bool live=false;
			for (int x=1;x<=xx;x++) {
				for (int y=1;y<=yy;y++) {
					g[now][x][y]=g[last][x][y];
					if (g[last][x][y]) {
						if (((x-1>0 && !g[last][x-1][y]) || (x==1)) && ((y-1>0 && !g[last][x][y-1]) || (y==1))) {
							g[now][x][y]=false;
						}
					} else {
						if (x-1>0 && g[last][x-1][y] && y-1>0 && g[last][x][y-1]) {
							g[now][x][y]=true;
							if (x>tx) tx=x;
							if (y>ty) ty=y;
						}
					}
					if (g[now][x][y]) live=true;
				}
			}
			xx=tx;yy=ty;
			last=1-last;now=1-now;
			if (!live) break;
		}
		printf("Case #%d: %d\n",cc,ans);
	}
}
