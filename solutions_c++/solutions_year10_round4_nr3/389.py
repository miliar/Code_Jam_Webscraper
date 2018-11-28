#include <iostream>
#include <cstdlib>
#include <cstdio>
#define maxn 1000001

using namespace std;

struct point {
	int x,y;
};

point a[maxn];
int n,ii,tt,i,j,x,y,t,k,x1,y1,x2,y2;
bool flag;

bool comp(point x,point y) {
	if (x.x+x.y<y.x+y.y) return true;
	if (x.x+x.y==y.x+y.y)
		if (x.x<y.x) return true;
	return false;
}

int map[2][101][101];

int main() {
	freopen("bacteria.in","r",stdin);
	freopen("bacteria.out","w",stdout);

	scanf("%d\n",&tt);
	/*
	for (ii=1;ii<=tt;++ii) {
		scanf("%d\n",&n);
		for (i=1;i<=n;++i) scanf("%d\n",&a[i].x,&a[i].y);
		sort(a+1,a+n+1,comp);
	}
	*/
	for (ii=1;ii<=tt;++ii) {
		scanf("%d\n",&n);
		memset(map,0,sizeof(map));
		for (i=1;i<=n;++i) {
			scanf("%d%d%d%d\n",&x1,&y1,&x2,&y2);
			for (j=x1;j<=x2;++j)
				for (k=y1;k<=y2;++k) map[0][j][k]=1;
		}
		t=0; flag=true;
		while (flag) {
			++t;
			for (i=1;i<=100;++i)
				for (j=1;j<=100;++j) {
					if (map[(t ^ 1) & 1][i][j]==1)
						if (map[(t ^ 1) & 1][i-1][j]==1 || map[(t ^ 1) & 1][i][j-1]==1) map[t & 1][i][j]=1;
						else map[t & 1][i][j]=0;
					if (map[(t ^ 1) & 1][i][j]==0)
						if (map[(t ^ 1) & 1][i-1][j]==1 && map[(t ^ 1) & 1][i][j-1]==1) map[t & 1][i][j]=1;
						else map[t & 1][i][j]=0;
				}
			flag=false;
			for (i=1;i<=100;++i) {
				for (j=1;j<=100;++j)
					if (map[t & 1][i][j]) {
						flag=true;
						break;
					}
				if (flag) break;
			}
		}
		printf("Case #%d: %d\n",ii,t);
	}
}
