#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;


int n,m,D,a[600][600],tes;
char s[600];
double eps=1e-6;

double sumsi[600][600],sumsj[600][600],sumss[600][600];

int check(int x,int y,int d)
{
	double cx=(x+x+d)/2.0,cy=(y+y+d)/2.0;
	
	double tx=0,ty=0;
	for (int i=x;i<=x+d-1;i++)
		for (int j=y;j<=y+d-1;j++)
		{
			if ((i==x || i==x+d-1) && (j==y || j==y+d-1)) continue;
			tx=tx+(i+0.5-cx)*a[i][j];
			ty=ty+(j+0.5-cy)*a[i][j];
		}
	if (fabs(tx)>eps || fabs(ty)>eps) return 0;
	return 1;
}

double si(int x,int y,int d)
{
	double t=sumsi[x+d-1][y+d-1]+sumsi[x-1][y-1]-sumsi[x+d-1][y-1]-sumsi[x-1][y+d-1];
	t=t-(sumsi[x+d-1][y+d-1]+sumsi[x+d-1-1][y+d-1-1]-sumsi[x+d-1][y+d-1-1]-sumsi[x+d-1-1][y+d-1]); //cell x+d-1,y+d-1
	t=t-(sumsi[x+d-1][y]+sumsi[x+d-1-1][y-1]-sumsi[x+d-1][y-1]-sumsi[x+d-1-1][y]);		//cell x+d-1,y
	t=t-(sumsi[x][y+d-1]+sumsi[x-1][y+d-1-1]-sumsi[x][y+d-1-1]-sumsi[x-1][y+d-1]);		//cell x,y+d-1
	t=t-(sumsi[x][y]+sumsi[x-1][y-1]-sumsi[x][y-1]-sumsi[x-1][y]);
	return t;
}

double ss(int x,int y,int d)
{
	double t=sumss[x+d-1][y+d-1]+sumss[x-1][y-1]-sumss[x+d-1][y-1]-sumss[x-1][y+d-1];
	t=t-(sumss[x+d-1][y+d-1]+sumss[x+d-1-1][y+d-1-1]-sumss[x+d-1][y+d-1-1]-sumss[x+d-1-1][y+d-1]); //cell x+d-1,y+d-1
	t=t-(sumss[x+d-1][y]+sumss[x+d-1-1][y-1]-sumss[x+d-1][y-1]-sumss[x+d-1-1][y]);		//cell x+d-1,y
	t=t-(sumss[x][y+d-1]+sumss[x-1][y+d-1-1]-sumss[x][y+d-1-1]-sumss[x-1][y+d-1]);		//cell x,y+d-1
	t=t-(sumss[x][y]+sumss[x-1][y-1]-sumss[x][y-1]-sumss[x-1][y]);
	return t;
}

double sj(int x,int y,int d)
{
	double t=sumsj[x+d-1][y+d-1]+sumsj[x-1][y-1]-sumsj[x+d-1][y-1]-sumsj[x-1][y+d-1];
	t=t-(sumsj[x+d-1][y+d-1]+sumsj[x+d-1-1][y+d-1-1]-sumsj[x+d-1][y+d-1-1]-sumsj[x+d-1-1][y+d-1]); //cell x+d-1,y+d-1
	t=t-(sumsj[x+d-1][y]+sumsj[x+d-1-1][y-1]-sumsj[x+d-1][y-1]-sumsj[x+d-1-1][y]);		//cell x+d-1,y
	t=t-(sumsj[x][y+d-1]+sumsj[x-1][y+d-1-1]-sumsj[x][y+d-1-1]-sumsj[x-1][y+d-1]);		//cell x,y+d-1
	t=t-(sumsj[x][y]+sumsj[x-1][y-1]-sumsj[x][y-1]-sumsj[x-1][y]);
	return t;
}

int ok(int d)
{

	for (int i=1;i<=n;i++) 
		for (int j=1;j<=m;j++)
		{	
			sumsi[i][j]=sumsi[i-1][j]+sumsi[i][j-1]-sumsi[i-1][j-1]+i*a[i][j];
			sumsj[i][j]=sumsj[i-1][j]+sumsj[i][j-1]-sumsj[i-1][j-1]+j*a[i][j];
			sumss[i][j]=sumss[i-1][j]+sumss[i][j-1]-sumss[i-1][j-1]+a[i][j];
		}
	
	for (int x=1;x+d-1<=n; x++)
	{
		double tx,ty;
		for (int y=1;y+d-1<=m;y++)
		{
			double cx=(x+x+d-1)/2.0,cy=(y+y+d-1)/2.0;
			tx=si(x,y,d)-cx*ss(x,y,d);
			ty=sj(x,y,d)-cy*ss(x,y,d);
			if (fabs(tx)<eps && fabs(ty)<eps) return 1;
		}
	}
	return 0;
}


int solve()
{
	for (int d=min(n,m);d>=3;d--)
	{
		if (ok(d)) return d;
	}
	return 0;
}

int main()
{
	freopen("b1.out","w",stdout);
	scanf("%d",&tes);
	for (int ttt=1;ttt<=tes;ttt++)
	{
		printf("Case #%d: ",ttt);
		scanf("%d%d%d",&n,&m,&D);
		for (int i=1;i<=n;i++) 
		{
			scanf("%s",s);
			for (int j=0;j<m;j++) a[i][j+1]=s[j]-'0';
		}
		int t=solve();
		if (!t) puts("IMPOSSIBLE");
		else printf("%d\n",t);
	}
	return 0;
}
