#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
#define FOR(i,j) for(int (i)=1;(i)<=(j);(i)++)
#define cango(x1,y1,x2,y2) (a[x1][y1]>a[x2][y2])
#define code(x,y) ((x)*108+(y))

int p[11000];

int find(int x){
	if (x==p[x]) return x;
	return p[x] = find(p[x]);
}

void uni(int x, int y){
	x = find(x);
	y = find(y);
	p[x] = y;
}

int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};

int main(){
	int t;
	scanf("%d",&t);
	for (int z=1;z<=t;++z){
		int h, w;
		scanf("%d%d",&h,&w);
		int a[h+2][w+2];
		memset(a,0x3f,sizeof(a));
		for (int i=0;i<11000;++i)
			p[i] = i;
		FOR(i,h)
			FOR(r,w)
				scanf("%d",&a[i][r]);
		int group[h][w];
		memset(group,-1,sizeof(group));
		FOR(i,h)
			FOR(r,w){
				int best = 1<<29;
				for (int k=0;k<4;++k){
					int nx = i + dx[k], ny = r + dy[k];
					if (cango(i,r,nx,ny)) best=min(best,a[nx][ny]);
				}
				for (int k=0;k<4;++k){
					int nx = i + dx[k], ny = r + dy[k];
					if (best==a[nx][ny]){
						uni(code(i,r),code(nx,ny));
						break;
					}
				}
			}
		FOR(i,h)
			FOR(r,w)
				p[code(i,r)] = find(code(i,r));
		char label[110][110], gl[11000], c='a';
		memset(label,0,sizeof(label));
		memset(gl,0,sizeof(gl));
		FOR(i,h)
			FOR(r,w){
				if (gl[p[code(i,r)]]==0) gl[p[code(i,r)]]=c++;
				label[i][r] = gl[p[code(i,r)]];
			}
		printf("Case #%d:\n",z);
		FOR(i,h){
			FOR(r,w)
				printf("%c ",label[i][r]);
			puts("");
		}
	}
	return 0;
}
