#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

const int MAXN=110;
const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};

int a[MAXN][MAXN];
int lb[MAXN][MAXN];
int cnt, h, w;

void go(int x, int y)
{
	if (lb[x][y]) return;
		int tx, ty, nx, ny, low=a[x][y];
		nx=ny=-1;
		for(int i=0;i<4;++i) {
			tx=x+dx[i]; ty=y+dy[i];
			if (tx<0 || ty<0 || tx==h || ty==w) continue;
			if (a[tx][ty]<low) {
				nx=tx; ny=ty; low=a[tx][ty];
			}
		}
		if (nx==-1) lb[x][y]=++cnt;	
		else {
			go(nx,ny); lb[x][y]=lb[nx][ny];
		}

}

int main()
{
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
	int T, tt=0;
	scanf("%d",&T);
	while (tt<T) {
		scanf("%d%d",&h,&w);
		for(int i=0;i<h;++i)
			for(int j=0;j<w;++j)
				scanf("%d",&a[i][j]);
//		cout << "g" << endl;
		for(int i=0;i<h;++i) memset(lb[i],0,4*w);
		cnt=0;
		for(int i=0;i<h;++i)
			for(int j=0;j<w;++j)
				if (!lb[i][j]) {
					go(i,j);
		}
		printf("Case #%d:\n",++tt);
		for(int i=0;i<h;++i) {
			printf("%c",lb[i][0]-1+'a');
			for(int j=1;j<w;++j)
				printf(" %c",lb[i][j]-1+'a');
			printf("\n");
		}
	}
	return 0;
}