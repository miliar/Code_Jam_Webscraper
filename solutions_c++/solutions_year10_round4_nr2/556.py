#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>

using namespace std;
#define EL long long

int maxmiss[(1<<11)];

EL memo[(1<<11)+1][25];
int price[(1<<12)];
const EL INF = (1LL<<44);
int prices[11][(1<<11)];
int P;
EL dp(int at,int lvl,int missed)
{
	if(missed > maxmiss[at]){return INF;}
	if(lvl == P){return 0;}
	EL &ret = memo[at][missed];
	if(ret != -1){return ret;}
	ret = INF;
	//we can miss this or not
	EL a = dp(at*2,lvl+1,missed);
	EL b = dp(at*2 + 1,lvl+1,missed);
	if(a == INF || b == INF){ret = INF;}
	else
	{
		ret = prices[lvl][at-(1<<lvl)] + a+b;
	}
	//MISS?
	a = dp(at*2,lvl+1,missed+1);
	b = dp(at*2+1,lvl+1,missed+1);
	if(a == INF || b == INF)
	{;
	}
	else
	{
		ret = min(ret,a+b);
	}
	return ret;
}

int cons[(1<<11)];
int main(int argc,char **argv)
{
	if(argc>1){freopen(argv[1],"r",stdin);}
	int CASES;
	cin >> CASES;
	for(int cn_ = 1; cn_ <= CASES;++cn_)
	{
		cin >> P;
		int p2 = (1<<P);
		for(int i=0;i<p2;++i)
		{
			cin >> cons[i];
			maxmiss[p2 + i] = cons[i];
		}
		for(int i=(1<<(P))-1;i>=1;--i)
		{
			maxmiss[i] = min(maxmiss[2*i],maxmiss[2*i+1]);
		}
		for(int i=P-1;i>=0;--i)
		{
			for(int j=0;j<(1<<i);++j)
			{
				cin >> prices[i][j];
			}
		}

		memset(memo,-1,sizeof(memo));
		printf("Case #%d: %lld\n",cn_,dp(1,0,0));
	}
	return 0;
}
