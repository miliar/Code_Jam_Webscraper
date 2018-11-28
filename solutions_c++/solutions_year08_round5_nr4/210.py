#include<stdio.h>
#include<string.h>

#define rint(x) scanf("%d",&x)
#define clr(x,y) memset(x, y, sizeof(x))
#define myabs(x) (((x)<0)?-(x):(x))

const int maxn = 105;
int n, m;
int r[10][2],g;
int f[maxn][maxn];
int mod = 10007;

int main() {
	int cs, step;
	int i,j,k;
	rint(cs);
	for(step=1;step<=cs;step++)
	{
		rint(n);
		rint(m);
		rint(g);
		for(i=0;i<g;i++)
		{
			rint(r[i][0]);
			rint(r[i][1]);
		}
		clr(f, 0);
		f[1][1] = 1;
		for(i=1;i<=n;i++)for(j=1;j<=m;j++)if(!(i==1&&j==1))
		{
			for(k=0;k<g;k++)if(i==r[k][0]&&j==r[k][1])break;
			if(k<g) continue;
			int i1 = i-1;
			int j1 = j-2;
			if(j1>=0){
				f[i][j] += f[i1][j1];
			}
			i1 = i-2;
			j1 = j-1;
			if(i1>=0)
				f[i][j] += f[i1][j1];
			f[i][j] %= mod;
		}			
		printf("Case #%d: %d\n", step, f[n][m]);
	}
	return 0;
}