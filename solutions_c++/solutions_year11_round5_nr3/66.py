#include <stdio.h>
#define N 20
char m[N][N], g[N][N];
int u[N][N];
int di[]={-1, -1, -1, 0, 1, 1, 1, 0}, dj[]={-1, 0, 1, 1, 1, 0, -1, -1};
int get(char c, int b)
{
	if(c=='\\') return b*4;
	if(c=='|') return 1+b*4;
	if(c=='/') return 2+b*4;
	if(c=='-') return 3+b*4;
}
int main()
{
	int i, j, r, c, t, ts, a, h;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d%d", &r, &c), i=0; i<r; scanf("%s", m[i]), i++);
		for(a=0, h=0; h<(1<<r*c); h++)
		{
			for(i=0; i<r; i++)
				for(j=0; j<c; g[i][j]=get(m[i][j], (h>>(i*c+j))&1), u[i][j]=0, j++);
			for(i=0; i<r; i++)
				for(j=0; j<c; u[(i+di[g[i][j]]+r)%r][(j+dj[g[i][j]]+c)%c]++, j++);
			for(i=0; i<r; i++)
			{
				for(j=0; j<c && u[i][j]<2; j++);
				if(j<c) break;
			}
			if(i==r) a++;
		}
		printf("Case #%d: %d\n", t+1, a);
	}
	return 0;
}