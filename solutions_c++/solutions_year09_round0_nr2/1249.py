#include "stdio.h"
int map[101][101],to[101][101],a[5]={0,-1,0,0,1},b[5]={0,0,-1,1,0},x[101][101],y[101][101];
char res[101][101];
void dfs(int sx,int sy)
{
	if(x[sx][sy]!=0)
		return;
	dfs(sx+a[to[sx][sy]],sy+b[to[sx][sy]]);
	x[sx][sy]=x[sx+a[to[sx][sy]]][sy+b[to[sx][sy]]];
	y[sx][sy]=y[sx+a[to[sx][sy]]][sy+b[to[sx][sy]]];
}
int main()
{
	int tt,c,m,n,i,j,k,l,s[27],t[27];
	scanf("%d",&tt);
	for(c=1;c<=tt;c++)
	{
		scanf("%d%d",&m,&n);
		for(i=0;i<=m+1;i++)
			for(k=0;k<=n+1;k++)
				map[i][k]=0x7fffffff;
		for(i=1;i<=m;i++)
			for(k=1;k<=n;k++)
				scanf("%d",&map[i][k]);
		for(i=1;i<=m;i++)
			for(k=1;k<=n;k++)
			{
				x[i][k]=0;
				y[i][k]=0;
				j=map[i][k];
				to[i][k]=0;
				if(map[i-1][k]<j){j=map[i-1][k];to[i][k]=1;}
				if(map[i][k-1]<j){j=map[i][k-1];to[i][k]=2;}
				if(map[i][k+1]<j){j=map[i][k+1];to[i][k]=3;}
				if(map[i+1][k]<j){j=map[i+1][k];to[i][k]=4;}
				if(to[i][k]==0)
				{
					x[i][k]=i;
					y[i][k]=k;
				}
			}
		for(i=1;i<=m;i++)
			for(k=1;k<=n;k++)
				dfs(i,k);
		j=0;
		for(i=1;i<=m;i++)
			for(k=1;k<=n;k++)
			{
				for(l=0;l<j;l++)
					if(x[i][k]==s[l]&&y[i][k]==t[l])
						break;
				res[i][k]=97+l;
				if(l==j)
				{
					s[j]=x[i][k];
					t[j]=y[i][k];
					j++;
				}
			}
		printf("Case #%d:\n",c);
		for(i=1;i<=m;i++)
			for(k=1;k<=n;k++)
			{
				putchar(res[i][k]);
				if(k!=n)putchar(' ');
				else putchar('\n');
			}
	}
	return 0;
}