#include <iostream>
#include <fstream>
using namespace std;
int n,target;
int f[11000][2],a[11000][2];
int dfs(int x,int nowstate)
{
	if (x>(n-1)/2)
	{
		if (nowstate==a[x][0]) f[x][nowstate]=0; else f[x][nowstate]=11000;
		return f[x][nowstate];
	}
	if (f[x][nowstate]>=0) return f[x][nowstate];
	int wh,i,j,t1,t;
	for (i=0;i<=1;i++)
	{
		dfs(x*2,i);
		dfs(x*2+1,i);
	}
	wh=a[x][0];
	for (i=0;i<=1;i++)
		for (j=0;j<=1;j++)
			if ((f[x*2][i]<=n)&&(f[x*2+1][j]<=n))
			{
				t1=f[x*2][i]+f[x*2+1][j];
				if (wh==0) t=(i|j); else t=(i&j);
				if (t==nowstate)
				{
					if ((f[x][nowstate]==-1)||(f[x][nowstate]>t1))
						f[x][nowstate]=t1;
				}
			}
	if (a[x][1]==1)
	{
		wh=1-a[x][0];
		for (i=0;i<=1;i++)
		for (j=0;j<=1;j++)
			if ((f[x*2][i]<=n)&&(f[x*2+1][j]<=n))
			{
				t1=f[x*2][i]+f[x*2+1][j]+1;
				if (wh==0) t=(i|j); else t=(i&j);
				if (t==nowstate)
				{
					if ((f[x][nowstate]==-1)||(f[x][nowstate]>t1))
						f[x][nowstate]=t1;
				}
			}
	}
	if (f[x][nowstate]==-1) f[x][nowstate]=11000;
	return f[x][nowstate];
}



int main()
{
	ifstream cin("a-large.in");
	ofstream cout("a-large.out");
	int i,t,ii,nn;
	cin >>nn;
	for (ii=1;ii<=nn;ii++)
	{
		cin >>n >>target;
		memset(f,-1,sizeof(f));
		for (i=1;i<=(n-1)/2;i++)
			cin >>a[i][0] >>a[i][1];
		for (i=1;i<=(n+1)/2;i++)
			cin >>a[i+(n-1)/2][0];
		t=dfs(1,target);
		cout <<"Case #" <<ii <<": ";
		if (t>n) cout <<"IMPOSSIBLE" <<endl; else cout <<t <<endl;
	}
	return 0;
}

