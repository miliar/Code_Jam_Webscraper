#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<vector>
#include<algorithm>
#include<utility>
#include<climits>
#include<complex>
#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>

using namespace std;

bool g[21][21];
int n;
int res[21];
vector<vector<int> >poly;
vector<int>belong[21];
int ans,ok;
int so[21],po,ts[21],has[21];
int use;
int bit[3000];
void dfs(int p)
{
	if (ok)return;
	int i,j;
	if (p==n)
	{
		if (bit[use]!=ans)return;
		memset(so,0,sizeof(so));
		for (i=0;i<n;i++)
		{
			for (j=0;j<belong[i].size();j++)
			{
				so[belong[i][j]]|=(1<<res[i]);
			}
		}
		for (i=0;i<po;i++)
		{
			if (so[i]!=((1<<ans)-1))break;
		}
		if (i==po)
		{
			ok=1;
			//for (i=0;i<n;i++)printf("%d\n",res[i]);
			memcpy(has,res,sizeof(res));
		}
		return;
	}
	
	for (i=0;i<ans;i++)
	{
		res[p]=i;
		int tt=use;
		use|=(1<<i);
		dfs(p+1);
		use=tt;
	}
}
int u[21],v[21];
int main()
{
	freopen("C:\\1\\out.txt","w",stdout);
	int i,j,k;
	int  _;
	int T=0;
	scanf("%d",&_);
	while (_--)
	{
		scanf("%d%d",&n,&k);
		memset(g,0,sizeof(g));
		for (i=0;i<n;i++)
		{
			belong[i].clear();
			g[i][(i+1)%n]=g[(i+1)%n][i]=1;
		}
		for (i=0;i<k;i++)
		{
			scanf("%d",u+i);u[i]--;
		}
		for (i=0;i<k;i++)
		{
			scanf("%d",v+i);v[i]--;
		}
		for (i=0;i<k;i++)
		{
			g[u[i]][v[i]]=g[v[i]][u[i]]=1;
		}
		poly.clear();
		int ii;
		for (ii=0;ii<(1<<n);ii++)
		{
			vector<int>tmp;
			for (j=0;j<n;j++)
			{
				if (ii&(1<<j))tmp.push_back(j);
			}
			bit[ii]=(int)tmp.size();
			if (tmp.size()<3)continue;
			//0 1 3
			
			int go=0;
			do 
			{
				int sz=tmp.size();
				for (i=0;i<sz;i++)
				{
					if (!g[tmp[i]][tmp[(i+1)%sz]])break;
				}
				if (i<sz)continue;
				int fd=1,ss=0;
				for (i=0;i<sz;i++)
				{
					for (j=i+1;j<sz;j++)
					{
						if (i==j)continue;
						if (g[tmp[i]][tmp[j]])
						{
							ss++;
						}
					}
					if (ss>sz)break;
				}
				if (ss>sz)continue;
				go=1;
				break;
			}
			while (next_permutation(tmp.begin(),tmp.end()));
			if (go)
			{
				poly.push_back(tmp);
			}
		}
		po=poly.size();
		for (i=0;i<po;i++)
		{
			for (j=0;j<poly[i].size();j++)
			{
				//printf("%d ",poly[i][j]);
				belong[poly[i][j]].push_back(i);
			}
		//	puts("-_");
		}
		/*for (i=0;i<n;i++)
		{
			for (j=0;j<belong[i].size();j++)
			{
				printf("%d ",belong[i][j]);
			}
			puts("");
		}*/
		for (ans=n;;ans--)
		{	
			ok=0;
			use=0;
			memset(so,0,sizeof(so));
			dfs(0);
			if (ok)break;
		}
		printf("Case #%d: %d\n",++T,ans);
		for (i=0;i<n;i++)
		{
			printf("%d%c",has[i]+1,i==n-1?'\n':' ');
		}
	}
	return 0;
}
