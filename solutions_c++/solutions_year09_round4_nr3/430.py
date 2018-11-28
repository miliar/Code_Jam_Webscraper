#include<iostream>
#include<cmath>
#include<map>
#include<vector>
#include<string>
#include<sstream>
#include<cstdlib>
#include<stack>
#include<list>
#include<deque>
#include<queue>
using namespace std;

typedef long long LL;

#define EPS (1e-8)
#define INF 0x7fffffff
#define SZ(p) ((p).size())

int n,m,f[65536];
vector<int> vt;

int dfs(int s)
{
	if(s==0)
		return 0;
	int &d=f[s];
	if(d!=-1)
		return d;
	int i,j;
	d=INF;
	for(i=0;i<vt.size();i++)
	{
		if(!(vt[i]&s))
			continue;
		int t=s;
		for(j=0;j<n;j++)
		{
			if(((1<<j)&vt[i])&&((1<<j)&s))
				t-=(1<<j);
		}
		d=min(d,dfs(t)+1);
	}
	return d;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	//freopen("2.in","r",stdin);
	//freopen("2.out","w",stdout);

	int T,CS;
	scanf("%d",&T);
	for(CS=1;CS<=T;CS++)
	{
		int i,j,k,l,mp[105][50];
		bool mq[105][105];
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				scanf("%d",&mp[i][j]);
			}
		memset(mq,0,sizeof(mq));
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
			{
				if(i==j)
					continue;
				bool p=0,q=0,r=0;
				for(k=0;k<m;k++)
				{
					if(mp[i][k]==mp[j][k])
						r=1;
					else if(mp[i][k]>mp[j][k])
						p=1;
					else if(mp[i][k]<mp[j][k])
						q=1;
				}
				if(r||(p&&q))
					continue;
				mq[i][j]=1;
			}
		vt.clear();
		for(i=0;i<(1<<n);i++)
		{
			vector<int> v;
			for(j=0;j<n;j++)
			{
				if((1<<j)&i)
					v.push_back(j);
			}
			bool flag=0;
			for(j=0;j<SZ(v);j++)
				for(k=j+1;k<SZ(v);k++)
				{
					if(!mq[v[j]][v[k]])
					{
						flag=1;
						goto ll;
					}
				}
			for(j=0;j<n;j++)
			{
				if((1<<j)&i)
					continue;
				for(k=0;k<SZ(v);k++)
				{
					if(!mq[v[k]][j])
						break;
				}
				if(k==SZ(v))
				{
					flag=1;
					goto ll;
				}
			}
ll:			if(flag)
				continue;
			vt.push_back(i);
		}
		memset(f,-1,sizeof(f));
		printf("Case #%d: ",CS);
		fflush(stdout);

		printf("%d\n",dfs((1<<n)-1));
	}
}