#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<queue>
#include<set>
#include<algorithm>
#include<sstream>
#include<cmath>
#include<cstdlib>
#include<deque>
#include<list>
#include<stack>
#include<cstdio>
#include<cstring>
#include<memory.h>
using namespace std;

typedef long long LL;

#define INF 0x7fffffff
#define PI acos(-1.0)
#define EPS (1e-10)

#define SZ(a) int((a).size())
#define PB push_back
#define MP make_pair

int gcd(int a,int b){return b>0?gcd(b,a%b):a;}

int c[15][1<<10],p,m[1<<11];
int f[15][1<<11][11];

void get(int n,int k,vector<int> &v)
{
	if(n==p)
	{
		v.push_back(m[k]);
		return;
	}
	get(n+1,k*2,v);
	get(n+1,k*2+1,v);
}

int dfs(int n,int k,int minm)
{
	if(n==p-1)
	{
		if(minm==0)
			return c[p-n-1][k];
		else
			return 0;
	}
	int &d=f[n][k][minm];
	if(d!=-1)
		return d;
	int ans=INF,i,t;
	vector<int> v;
	get(n,k,v);
	int min1,min2,tmin;
	min1=min2=tmin=INF;
	for(i=0;i<v.size()/2;i++)
	{
		min1=min(min1,v[i]);
		tmin=min(tmin,v[i]);
	}
	for(;i<v.size();i++)
	{
		min2=min(min2,v[i]);
		tmin=min(tmin,v[i]);
	}
	tmin-=minm;
	min1-=tmin;
	min2-=tmin;
	if(minm>0)
	{
		ans=min(ans,dfs(n+1,k*2,min1-1)+dfs(n+1,k*2+1,min2-1));
	}
	t=c[p-n-1][k];
	ans=min(ans,t+dfs(n+1,k*2,min1)+dfs(n+1,k*2+1,min2));
	return d=ans;
}

int main()
{
	freopen("C:\\Users\\LL\\Desktop\\GCJ\\2.in","r",stdin);
	freopen("C:\\Users\\LL\\Desktop\\GCJ\\3.out","w",stdout);

	int csNum,cs;
	scanf("%d",&csNum);
	for(cs=1;cs<=csNum;cs++)
	{
		int i,j,ans,minm=INF;
		scanf("%d",&p);
		for(i=0;i<(1<<p);i++)
		{
			scanf("%d",&m[i]);
			minm=min(minm,m[i]);
		}
		for(i=0;i<p;i++)
		{
			for(j=0;j<(1<<(p-i-1));j++)
				scanf("%d",&c[i][j]);
		}
		memset(f,-1,sizeof(f));
		ans=dfs(0,0,minm);
		printf("Case #%d: %d\n",cs,ans);
	}
}