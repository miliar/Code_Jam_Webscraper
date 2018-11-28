#include <stdio.h>
#include <algorithm>
#include <vector>
#define debug(x)
using namespace std;
int Want[4024];
int Cost[11][4024];

int Dp[11][11][1024];
int Visit[11][11][1024];

int solve(int round,int seen,int m)
{
	if (round==0)
	{
		if (seen<Want[m]) return -1;
		return 0;
	}
	if (Visit[round][seen][m]) return Dp[round][seen][m];
	Visit[round][seen][m] = 1;
	int &ret = Dp[round][seen][m];
	//to See
	int s1 = solve(round-1,seen+1,m*2);
	int s2 = solve(round-1,seen+1,m*2+1);
	int toSee = -1;
	if (s1>=0 && s2>=0) toSee = s1 + s2 + Cost[round][m];
	//not to See
	int n1 = solve(round-1,seen,m*2);
	int n2 = solve(round-1,seen,m*2+1);
	int ntSee = -1;
	if (n1>=0 && n2>=0) ntSee = n1 + n2;
	if (toSee<0) return ret = ntSee;
	if (ntSee<0) return ret = toSee;
	return ret = min(ntSee,toSee);
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int Test;
	scanf("%d",&Test);
	for (int kase=1;kase<=Test;++kase)
	{
		int n;
		scanf("%d",&n);
		int t = 1<< n;
		for (int q=0;q<t;++q)
		{
			int x;
			scanf("%d",&x);
			Want[q] = n-x;
		}
		for (int q=1;q<=n;++q)
			for (int w=0;w<(t>>q);++w)
				scanf("%d",&Cost[q][w]);
		for (int q=0;q<=n;++q) for (int w=0;w<=n;++w) for (int e=0;e<t;++e) Visit[q][w][e] = 0;
		printf("Case #%d: %d\n",kase, solve(n,0,0) );
	}
	return 0;
}