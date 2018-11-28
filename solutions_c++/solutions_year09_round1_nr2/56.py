#include<stdio.h>
#include<string.h>
#include<memory.h>
#define HOR 0
#define VER 1
#define INF -1
#define max(a, b) (((a)>(b))?(a):(b))
struct its
{
	__int64 s, w, t;
};
struct dif
{
	int dx, dy, dd;
};
int n, m;
its a[32][32];
__int64 d[32][32][4];
bool v[32][32][4];
dif nxt[4][3];
__int64 f_get(int x, int y, int dir, __int64 sv)
{
	__int64 z, len;
	if(dir==VER)
	{
		z=sv/(a[x][y].s+a[x][y].w); z*=(a[x][y].s+a[x][y].w); z+=a[x][y].t; len=a[x][y].s;
	}
	else
	{
		z=sv/(a[x][y].s+a[x][y].w); z*=(a[x][y].s+a[x][y].w); z+=a[x][y].t+a[x][y].s; len=a[x][y].w;
	}
	z-=(a[x][y].s+a[x][y].w)*5;
	while(z+len<=sv) z+=a[x][y].s+a[x][y].w;
	return max(z, sv);
}
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j, k;
	int t, tc;
	int nx, ny, nd;
	__int64 mc;
	int mx, my, md;
	__int64 tmp;
	int dir;
	nxt[0][1].dx=0; nxt[0][1].dy=-1; nxt[0][1].dd=3;
	nxt[0][2].dx=1; nxt[0][2].dy=0; nxt[0][2].dd=1;
	nxt[1][1].dx=-1; nxt[1][1].dy=0; nxt[1][1].dd=0;
	nxt[1][2].dx=0; nxt[1][2].dy=-1; nxt[1][2].dd=2;
	nxt[2][1].dx=0; nxt[2][1].dy=1; nxt[2][1].dd=1;
	nxt[2][2].dx=-1; nxt[2][2].dy=0; nxt[2][2].dd=3;
	nxt[3][1].dx=1; nxt[3][1].dy=0; nxt[3][1].dd=2;
	nxt[3][2].dx=0; nxt[3][2].dy=1; nxt[3][2].dd=0;

	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d%d", &n, &m);
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				fscanf(fp, "%I64d%I64d%I64d", &a[i][j].s, &a[i][j].w, &a[i][j].t);
				a[i][j].t%=(a[i][j].s+a[i][j].w);
				for(k=0;k<=3;k++) d[i][j][k]=INF;
			}
		}
		d[n][1][0]=0;
		memset(v, false, sizeof(v));
		while(!v[1][m][2])
		{
			mc=INF;
			for(i=1;i<=n;i++)
			{
				for(j=1;j<=m;j++)
				{
					for(k=0;k<=3;k++)
					{
						if(d[i][j][k]==INF || v[i][j][k]) continue;
						if(mc==INF || mc>d[i][j][k]){mc=d[i][j][k]; mx=i; my=j; md=k;}
					}
				}
			}
			v[mx][my][md]=true;
			for(k=1;k<=2;k++)
			{
				nx=mx+nxt[md][k].dx; ny=my+nxt[md][k].dy; nd=nxt[md][k].dd;
				if(nx<1 || ny<1 || nx>n || ny>m) continue;
				if(v[nx][ny][nd]) continue;
				if(d[nx][ny][nd]==INF || d[nx][ny][nd]>mc+2) d[nx][ny][nd]=mc+2;
			}
			for(k=1;k<=3;k+=2)
			{
				dir=(md+(k+1)/2)%2;
				tmp=f_get(mx, my, dir, mc)+1;
				if(d[mx][my][(md+k)%4]==INF || d[mx][my][(md+k)%4]>tmp) d[mx][my][(md+k)%4]=tmp;
			}
		}
		printf("Case #%d: %d\n", t, d[1][m][2]);
		fprintf(ofp, "Case #%d: %d\n", t, d[1][m][2]);
	}
	return 0;
}
