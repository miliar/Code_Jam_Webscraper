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
#include <ctime>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000
#define maxn 1000000

//typedef long long  LL;
//typedef __int64 LL;
typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

int n,scores[105];
int best[2][105],p;
int memo[105][105];

int solve(int pos,int s)
{
	int ret=0;
	if(pos==n) 
	{
		if(s) return inf;
		return 0;
	}
	if(s<0) return inf;
	if(memo[pos][s]!=-1) return memo[pos][s];

	int sc=scores[pos];

	if(best[0][sc]!=-1)
	{
		int cost = best[0][sc]>=p;
		int q=solve(pos+1,s);
		if(q!=inf) ret=MAX(ret,cost+q);
	}

	if(best[1][sc]!=-1)
	{
		int cost = best[1][sc]>=p;
		int q=solve(pos+1,s-1);
		if(q!=inf) ret=MAX(ret,cost+q);
	}

	

	return memo[pos][s]=ret;
}
int main()
{
	int i,j,k,tests,cs=0,s;

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-attempt0.out","w",stdout);

	MEM(best,-1);

	for(i=0;i<=10;i++)
			for(j=i;j<=10;j++)
				for(k=j;k<=10;k++)
				{
					if(k-i>2) continue;

					int sc=i+j+k;
					if(j-i==2 || k-j==2 || k-i==2)
						best[1][sc]=MAX(best[1][sc],k);
					else
						best[0][sc]=MAX(best[0][sc],k);
				}
	scanf("%d",&tests);
	while(tests--)
	{
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;i++)
			scanf("%d",&scores[i]);

		MEM(memo,-1);
		int ans=solve(0,s);
		printf("Case #%d: %d\n",++cs,ans);


		
	}



	return 0;
} 


