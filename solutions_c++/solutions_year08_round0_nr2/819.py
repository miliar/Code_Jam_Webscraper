#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

const int maxn=205;

int t,n1,n2,t1[maxn][2],t2[maxn][2];
int nx,ny,m,g[maxn][maxn],sy[maxn],cx[maxn],cy[maxn],ans1,ans2;

int path(int u)
{
	for (int v=1;v<=ny;v++)
		if (g[u][v]&&!sy[v])
		{
			sy[v]=1;
			if (!cy[v]||path(cy[v]))
			{
				cx[u]=v;
				cy[v]=u;
				return 1;
			}
		}
	return 0;
}

void maxmatch()
{
	int i,ret=0;
	memset(cx,0,sizeof(cx));
	memset(cy,0,sizeof(cy));
	for (i=1;i<=nx;i++)
		if (!cx[i])
		{
			memset(sy,0,sizeof(sy));
			ret+=path(i);
		}
}

void solve()
{
	memset(g,0,sizeof(g));
	int N=n1+n2;
	nx=N;ny=N;
	for (int i=1;i<=n1;i++)
		for (int j=1;j<=n2;j++)
			if (t1[i][1]+t<=t2[j][0]) g[i][n1+j]=1;
	for (int i=1;i<=n2;i++)
		for (int j=1;j<=n1;j++)
			if (t2[i][1]+t<=t1[j][0]) g[n1+i][j]=1;

	maxmatch();
//	for (int i=1;i<=nx;i++) cout<<cx[i]<<" ";cout<<endl;
//	for (int i=1;i<=ny;i++) cout<<cy[i]<<" ";cout<<endl;
	ans1=ans2=0;
	for (int i=1;i<=n1;i++)
		if (!cy[i]) ans1++;
	for (int i=1;i<=n2;i++)
		if (!cy[n1+i]) ans2++;

/*
	cout<<"test"<<endl;
	cout<<source<<" "<<target<<endl;
	for (int i=1;i<=n1+n2+2;i++){
		for (int j=1;j<=n1+n2+2;j++)
			cout<<c[i][j]<<" ";
		cout<<endl;
	}
	cout<<endl;
	for (int i=1;i<=n1+n2+2;i++){
		for (int j=1;j<=n1+n2+2;j++)
			cout<<w[i][j]<<" ";
		cout<<endl;
	}

	mincost(n1+n2+2,source,target,flow,cost);
	
	cout<<flow<<" "<<cost<<endl;

	ans1=ans2=0;
	for (int i=1;i<=n1;i++)
		if (f[source][i]) ans1++;
	for (int i=1;i<=n2;i++)
		if (f[source][n1+i]) ans2++;
		*/
}

int main()
{
	int T,hh1,mm1,hh2,mm2,kase=0;
	cin>>T;
	while (T--)
	{
		cin>>t>>n1>>n2;
		for (int i=1;i<=n1;i++)
		{
			scanf("%d:%d %d:%d",&hh1,&mm1,&hh2,&mm2);
			t1[i][0]=hh1*60+mm1;
			t1[i][1]=hh2*60+mm2;

//			cout<<t1[i][0]<<" "<<t1[i][1]<<endl;
		}
		for (int i=1;i<=n2;i++)
		{
			scanf("%d:%d %d:%d",&hh1,&mm1,&hh2,&mm2);
			t2[i][0]=hh1*60+mm1;
			t2[i][1]=hh2*60+mm2;

//			cout<<t2[i][0]<<" "<<t2[i][1]<<endl;
		}
		solve();
		cout<<"Case #"<<++kase<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}
