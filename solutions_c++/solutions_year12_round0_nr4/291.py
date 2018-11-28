#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>

int T,h,w,d,ans,wa;
char map[40][40];
double a[100000][2],x,y;

int pan(double a,double b,double c,double d)
{
	if (c==x && d==y)return 0;
	if ((a-x)*(d-y)==(c-x)*(b-y) && ((a-x) * (c-x)>0 || (b-y) * (d-y)>0))
	{
		return 1;
	}
	return 0;
}
double dis(double a,double b)
{
	return sqrt((a-x)*(a-x)+(b-y)*(b-y));
}

void dfs(double x,double y)
{
	double i,j;
	int k;
	i=2-x;j=y;
	if (dis(i,j)<=d)
	{
		for (k=0;k<=ans;k++)if ((i==a[k][0] && j==a[k][1]))break;
		if (k>ans)
		{
			ans++;
			a[ans][0]=i;
			a[ans][1]=j;
			dfs(i,j);
		}
	}
	i=h-2-x+h;j=y;
	if (dis(i,j)<=d)
	{
		for (k=0;k<=ans;k++)if ((i==a[k][0] && j==a[k][1]))break;
		if (k>ans)
		{
			ans++;
			a[ans][0]=i;
			a[ans][1]=j;
			dfs(i,j);
		}
	}
	i=x;j=2-y;
	if (dis(i,j)<=d)
	{
		for (k=0;k<=ans;k++)if ((i==a[k][0] && j==a[k][1]))break;
		if (k>ans)
		{
			ans++;
			a[ans][0]=i;
			a[ans][1]=j;
			dfs(i,j);
		}
	}
	i=x;j=w-2-y+w;
	if (dis(i,j)<=d)
	{
		for (k=0;k<=ans;k++)if ((i==a[k][0] && j==a[k][1]))break;
		if (k>ans)
		{
			ans++;
			a[ans][0]=i;
			a[ans][1]=j;
			dfs(i,j);
		}
	}
}

int main()
{
	int i,j;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for (int id=1;id<=T;id++)
	{
		ans=wa=0;
		scanf("%d%d%d",&h,&w,&d);
		for (i=0;i<h;i++)
		{
			scanf("%s",map[i]);
			for (j=0;j<w;j++)if (map[i][j]=='X')
			{
				x=i+0.5;
				y=j+0.5;
				a[0][0]=x;a[0][1]=y;
			}
		}
		dfs(x,y);
		for (i=1;i<=ans;i++)
		{
			for (j=1;j<i;j++)if (pan(a[i][0],a[i][1],a[j][0],a[j][1])==1)break;
			if (j<i)wa++;
		}
		printf("Case #%d: %d\n",id,ans-wa);
	}
	return 0;
}
/*
1.5 0.5 //
1.5 2.5 //
0.5 1.5 //
2.5 1.5 //
0.5 0.5 //
0.5 2.5 //
2.5 0.5 //
2.5 2.5
*/