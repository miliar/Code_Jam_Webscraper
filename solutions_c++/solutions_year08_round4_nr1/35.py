#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>
using namespace std;

#define FR(i,a,n) for(int (i) = (a); (i)<(n); (i)++)
#define RF(i,a,n) for(int (i) = int(n)-1; (i)>=(a); (i)--)
#define FOR(i,n) FR(i,0,n)
#define ROF(i,n) RF(i,0,n)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;

int dr[4] = {-1,0,1,0};
int dc[4] = {0,1,0,-1};

int gate[10000];
int change[10000];
int dp[10000][2];

int solve(int i, int val)
{
	int& ret = dp[i][val];
	if(ret!=-1)
		return ret;
	ret = 1000000;
	if(change[i]==-1)
	{
		if(gate[i]==val)
			return ret = 0;
		return ret;
	}
	int a0 = solve(2*i+1, 0);
	int a1 = solve(2*i+1, 1);
	int b0 = solve(2*i+2, 0);
	int b1 = solve(2*i+2, 1);
	if(gate[i]==1 || change[i]==1)
	{
		if(val==0)
		{
			ret = min(ret, a0+b0+(gate[i]==0 ? 1 : 0));
			ret = min(ret, a0+b1+(gate[i]==0 ? 1 : 0));
			ret = min(ret, a1+b0+(gate[i]==0 ? 1 : 0));
		}
		else
		{
			ret = min(ret, a1+b1+(gate[i]==0 ? 1 : 0));
		}
	}
	if(gate[i]==0 || change[i]==1)
	{
		if(val==0)
		{
			ret = min(ret, a0+b0+(gate[i]==1 ? 1 : 0));
		}
		else
		{
			ret = min(ret, a0+b1+(gate[i]==1 ? 1 : 0));
			ret = min(ret, a1+b0+(gate[i]==1 ? 1 : 0));
			ret = min(ret, a1+b1+(gate[i]==1 ? 1 : 0));
		}
	}
	return ret;
}

int main()
{
	int TESTS;
	scanf("%d", &TESTS);
	FOR(tests,TESTS)
	{
		int M, V;
		scanf("%d%d", &M, &V);
		FOR(i,(M-1)/2)
			scanf("%d%d", gate+i, change+i);
		FR(i,(M-1)/2, M)
		{
			scanf("%d", gate+i);
			change[i] = -1;
		}
		memset(dp, -1, sizeof(dp));
		int res = solve(0, V);
		if(res==1000000)
			printf("Case #%d: IMPOSSIBLE\n", tests+1);
		else
			printf("Case #%d: %d\n", tests+1, res);
	}
	return 0;
}
