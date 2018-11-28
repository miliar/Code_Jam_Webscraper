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
#define LL unsigned long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000

#define MAXN 1100
using namespace std;
LL R, K, N;
vector<LL> G;
LL vis[MAXN];
LL cost[MAXN];
LL ccount[MAXN];

LL solve()
{
	if(N == 0)
		return 0;
	CLR(vis);
	CLR(cost);
	CLR(ccount);
	int i, j, k;
	int cycindex = -1;
	LL ret = 0;
	LL temp = 0;
	for(i = 0; i < N; i++)
	{
		temp += G[i];
	}
	if(temp <= K)
	{
		return temp * R;
	}
	int cur = 0;
	LL curcost = 0;
	LL curcnt = 0;
	while(vis[cur] == 0)
	{
		//cout << "1 : " << cur<<" " << curcost<<" " << curcnt<<endl;
		LL temptot = 0;
		vis[cur] = 1;
		cost[cur] = curcost;
		ccount[cur] = curcnt;
		for(i = cur;; i = (i+1)%N)
		{
			if(temptot + G[i] > K)
				break;
			curcost += G[i];
			temptot += G[i];
		}
		curcnt += 1;
		cur = i;
	}
	cycindex = cur;
	LL cyccost = curcost - cost[cur];
	LL cyccnt = curcnt - ccount[cur];
	//cout << cycindex << " " << cyccost << " " << cyccnt <<endl;
	int tp = K;
	cur = 0;
	int flag = 0;
	
	while(R)
	{
		if(flag == 0 && cycindex == cur)
		{
			flag = 1;
			LL tr = R/cyccnt;
			R = R%cyccnt;
			ret += cyccost * tr;
		}
		else
		{
			LL temptot = 0;
			for(i = cur;; i = (i+1)%N)
			{
				if(temptot + G[i] > K)
					break;
				temptot += G[i];
				ret += G[i];
			}
			cur = i;
			R--;
		}
	}
	return ret;
}

int main()
{
	int tes;
	int testnum = 0;
	scanf("%d", &tes);
	while(tes--)
	{
		testnum++;
		scanf("%lld%lld%lld", &R, &K, &N);
		int i, j, k;
		G.clear();
		for(i = 0; i < N; i++)
		{
			scanf("%d", &j);
			if(j > K)
				continue;
			G.PB(j);
		}
		N = SZ(G);
		LL ans = solve();
		printf("Case #%d: %lld\n", testnum, ans);
	}
	return 0;
}

