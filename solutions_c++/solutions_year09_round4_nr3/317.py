#include<iostream>
#include<cstring>
#include<algorithm>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<cassert>
#include<numeric>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<deque>
using namespace std;

#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

VI ok;
int cache[1<<16];
int go(int have)
{
	if(have == 0) return 0;
	if(cache[have] != -1) return cache[have];
	int ret = 9999;
	int must = 1 << __builtin_ctz(have);
	for(int subset = have; subset; subset = ((subset-1)&have))
	{
		if(ok[subset] && (must & subset))
			ret = min(ret, go(have - subset) + 1);
	}
	return cache[have] = ret;
}
bool LESS(const VI& a, const VI& b)
{
	REP(i,a.sz) if(a[i] >= b[i]) return false;
	return true;
}
int main()
{
    int cases;
    scanf("%d", &cases);
    for(int cc = 0; cc < cases; ++cc)
    {
		int n, f;
		scanf("%d %d", &n, &f);
		VVI price(n, VI(f));
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < f; ++j)
				scanf("%d", &price[i][j]);
		VI no(n);
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < i; ++j)
			{
				if(LESS(price[i], price[j]) || LESS(price[j], price[i]))
					continue;
				no[i] += (1<<j);
				no[j] += (1<<i);
			}
		ok.resize(1<<n);
		for(int subset = 0; subset < (1<<n); ++subset)
		{
			ok[subset] = 1;
			for(int i = 0; i < n; ++i)
				if((subset & (1<<i)) && (subset & no[i]))
				{
					ok[subset] = 0;
					break;
				}
		}
		CLEAR(cache,-1);
		printf("Case #%d: %d\n", cc+1, go((1<<n)-1));
    }
}

