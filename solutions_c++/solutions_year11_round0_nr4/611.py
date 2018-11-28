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
		int n; scanf("%d",&n); int res = 0;
		REP(i,n){ int j; scanf("%d",&j); if(i+1!=j) res++; }
		printf("Case #%d: %.6lf\n",x,double(res));
	}
	return 0;
}

