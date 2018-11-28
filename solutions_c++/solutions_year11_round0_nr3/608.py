//Grzegorz Prusak
#include <cstdio>
#include <algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,p,k) for(int i=(p); i<=(k); ++i)

int main()
{
	int t; scanf("%d",&t); FOR(x,1,t)
	{
		int s = 0, m = 10e7, c = 0;
		int n; scanf("%d",&n); REP(i,n)
		{
			int v; scanf("%d",&v);
			s += v; c ^= v; if(m>v) m = v;
		}
		printf("Case #%d: ",x);
		if(c) puts("NO"); else printf("%d\n",s-m);
	}
	return 0;
}

