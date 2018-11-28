#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000
using namespace std;

#define MAXN 2001
int P;
int N;
LL base[MAXN];

LL vals[MAXN][MAXN];

LL tree[4*MAXN];
pair<int, int> treerng[2*MAXN];
int treeend;
LL dp[2*MAXN][2*MAXN];
#define INF (LL)1e14
void makerng(int node, int st, int en)
{
	if(node > treeend+N)
		return;
	treerng[node] = MP(st, en);
	makerng(node*2, st, (st+en)/2);
	makerng(node*2+1, (st+en)/2+1, en);
}
LL solve(int node, int missed)
{
	if(node > treeend)
	{
		if(missed <= base[treerng[node].first])
		return 0;
		else
			return INF;
	}
	LL &ret = dp[node][missed];
	if(ret != -1)
		return ret;
	pair<int, int> p1 = treerng[node];
	int i, j, k;
	for(i = p1.first; i <= p1.second; i++)
	{
		if(missed > base[i])
			return (ret = INF);
	}
	ret = INF;
	ret = min(solve(node*2, missed) + solve(node*2+1, missed) + tree[node], solve(node*2, missed+1) + solve(node*2+1, missed+1));
	return ret;
}
int main()
{
	int tes;
	cin >> tes;
	int tesnum = 0;
	while(tes--)
	{
		tesnum++;
		CLR(base);
		CLR(vals);
		CLRM(dp);
		cin >> P;
		N = 1<<P;
		int i, j, k;
		for(i = 0; i < N; i++)
		{
			cin >> base[i];
		}
		for(i = P-1; i >= 0; i--)
		{
			for(j = 0; j < 1<<i; j++)
			{
				cin >> vals[i][j];
			}
		}
		int st = 1;
		for(i = 0; i < P; i++)
		{
			for(j = 0; j < 1<<(i); j++)
			{
				tree[st++] = vals[i][j];
			}
		}
		treeend = st-1;
		for(i = 0; i < N; i++)
		{
			tree[st+i] = base[i];
		}
		makerng(1, 0, N-1);	
		/*for(i = 1; i <= treeend; i++)
		{
			cout<<tree[i]<<" "<<treerng[i].first<<" "<<treerng[i].second<<endl;
		}*/
		LL ans = solve(1, 0);
		printf("Case #%d: %lld\n", tesnum, ans);
	}
	return 0;
}
