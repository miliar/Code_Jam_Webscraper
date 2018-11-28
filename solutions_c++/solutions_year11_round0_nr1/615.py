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
		int P[2]={1,1},T[2]={},res = 0;
		int n; scanf("%d",&n); REP(i,n)
		{
			char bot; int p; scanf(" %c%d",&bot,&p);
			bool j = bot=='O'; int step = max(0,abs(P[j]-p)-T[j])+1;
			P[j] = p; T[j] = 0; T[!j] += step; res += step;
		}
		printf("Case #%d: %d\n",x,res);
	}
	return 0;
}

