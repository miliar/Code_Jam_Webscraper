#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <map>
#include <string.h>
#include <string>
#include <assert.h>
using namespace std;
#define N 100
int edge[N][N],etop[N];
int rm[N];
bool rset[N];
bool DFS(int v)
{
	for(int i=0;i<etop[v];i++)
	{
		int u=edge[v][i];
		if(rset[u])continue;
		rset[u]=true;
		if(rm[u]==-1||DFS(rm[u]))
		{
			rm[u]=v;
			return true;
		}
	}
	return false;
}
int maxMatch(int n,int m)
{
	memset(rm,0xff,sizeof(int)*m);
	memset(rset,false,sizeof(bool)*m);
	int re=0;
	for(int i=0;i<n;i++)
	{
		if(DFS(i))
		{
			re++;
			memset(rset,false,sizeof(bool)*m);
		}
	}
	return re;
}
int AB1[N],AB2[N],BA1[N],BA2[N];
int main()
{
	int t,ca;
	for(scanf("%d",&t),ca=1;ca<=t;ca++)
	{
		int turn, n,m;
		scanf("%d %d %d",&turn,&n,&m);
		assert(n<=N&&m<=N);
		for(int i=0;i<n;i++)
		{
			int h,m;
			scanf("%d:%d",&h,&m);
			AB1[i]=h*60+m;
			scanf("%d:%d",&h,&m);
			AB2[i]=h*60+m;
		}
		for(int i=0;i<m;i++)
		{
			int h,m;
			scanf("%d:%d",&h,&m);
			BA1[i]=h*60+m;
			scanf("%d:%d",&h,&m);
			BA2[i]=h*60+m;
		}
		memset(etop,0,sizeof(int)*n);
		for(int i=0;i<n;i++)
		{
			etop[i]=0;
			for(int j=0;j<m;j++)
				if(AB1[i]>=BA2[j]+turn)
					edge[i][etop[i]++]=j;
		}
		int n1=n-maxMatch(n,m);
		for(int i=0;i<m;i++)
		{
			etop[i]=0;
			for(int j=0;j<n;j++)
				if(BA1[i]>=AB2[j]+turn)
					edge[i][etop[i]++]=j;
		}
		int n2=m-maxMatch(m,n);
		printf("Case #%d: %d %d\n",ca,n1,n2);
	}
	return 0;
}
