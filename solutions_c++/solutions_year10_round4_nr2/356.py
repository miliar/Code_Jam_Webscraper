#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000

//typedef long long LL;
typedef __int64 LL;

int memo[1050][1050],vals[1050],costs[12][1050];
int cost[1050],need[1050],n;

int solve(int u,int c,int lev)
{
	int i,ret=inf;

	if(c<0) return -1;
	if(memo[u][c]!=-1) return memo[u][c];

	if(lev==1)
	{
		if(c>=need[u]) return 0;
		if(c+1>=need[u]) return cost[u];
		return inf;
	}

	int q=cost[u]+solve(2*u,c+1,lev-1)+solve(2*u+1,c+1,lev-1);

	
	ret=MIN(ret,q);

	q=solve(2*u,c,lev-1)+solve(2*u+1,c,lev-1);
	ret=MIN(ret,q);
	
	//printf("%d %d %d\n",u,c,ret);

	return memo[u][c]=ret;
}

int main()
{
	int i,j,k,l,tests,cs=0;
	

	//freopen("D:\\gcj\\B-small.in","r",stdin);
	freopen("D:\\gcj\\B-large.out","w",stdout);

	scanf("%d",&tests);
	while(tests--)
	{
		scanf("%d",&n);
		for(i=0;i<(1<<n);i++)
		{
			scanf("%d",&vals[i]);
			vals[i]=n-vals[i];
		}


		for(j=n-1;j>=0;j--)
		{
			for(k=0;k<(1<<j);k++)
				scanf("%d",&costs[j][k]);
		}

		int id=0;

		for(i=0;i<n;i++)
		{
			if(i==n-1)
			{
				for(k=j=0;j<(1<<i);j++,k+=2)
					need[id+j+1]=MAX(vals[k],vals[k+1]);
			}

			for(j=0;j<(1<<i);j++)
				cost[++id]=costs[i][j];

			
		}

		//for(i=1;i<=id;i++)
		//	printf("%d %d\n",i,cost[i]);

		MEM(memo,-1);
		int ans=solve(1,0,n);
		printf("Case #%d: %d\n",++cs,ans);
	}

	return 0;
} 


