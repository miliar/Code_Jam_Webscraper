#pragma warning(disable:4786)
#include<math.h>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<utility>
#include<algorithm>
#include<string.h>
#include<stdio.h>
#include<set>
#include<stdlib.h>
#include<sstream>
#include<functional>
#include<queue>
#include<stack>
using namespace std;

#define MAX(A,B) ((A)>(B)?(A):(B))
#define MIN(A,B) ((A)<(B)?(A):(B))
#define ABS(A) ((A)>0?(A):(-(A)))
#define S(X) ((X)*(X))

typedef pair<int,int> PII;
typedef __int64 LL;

//int dr[]={-1,0,1,0};
//int dc[]={0,1,0,-1};
//int dr[]={-2,-2,-1,1,2,2,1,-1};
//int dc[]={-1,1,2,2,1,-1,-2,-2};

vector<int> V[102];
int vis[102],match1[102],match2[102];
int n,k;
int p[102][102];

int BPM(int at)
{
	int sz,i,v;

	vis[at]=1;
	sz=V[at].size();
	for(i=0;i<sz;i++)
	{
		v=V[at][i];

		if(match2[v]==-1 || (!vis[match2[v]] && BPM(match2[v])))
		{
			match1[at]=v;
			match2[v]=at;
			return 1;
		}
	}

	return 0;
}

int BELOW(int a,int b)
{
	int i;

	if(p[a][0] > p[b][0]) return 0;

	for(i=0;i<k-1;i++)
	{
		if(p[a][i]==p[b][i]) return 0;
		if(p[a][i+1]==p[b][i+1]) return 0;

		if(p[a][i]<p[b][i] && p[a][i+1]>p[b][i+1]) return 0;
		if(p[a][i]>p[b][i] && p[a][i+1]<p[b][i+1]) return 0;
	}

	return 1;
}

int main()
{
//	freopen("C-small-attempt0.in","r",stdin); freopen("C-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in\n","r",stdin); freopen("A-small-attempt1.out\n","w",stdout);
	freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);

	int T,ks,i,j,ans;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d%d",&n,&k);

		for(i=0;i<n;i++)
		{
			V[i].clear();
			for(j=0;j<k;j++)
				scanf("%d",&p[i][j]);
		}

		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
			{
				if(BELOW(i,j))
				{
					V[i].push_back(j);
				}
			}

		for(i=0;i<n;i++) match1[i]=match2[i]=-1;

		ans=0;
		for(i=0;i<n;i++)
			if(match1[i]==-1)
			{
				for(j=0;j<n;j++) vis[j]=0;

				if(BPM(i)) ans++;
			}

		printf("Case #%d: %d\n",ks,n-ans);
	}
	return 0;
}