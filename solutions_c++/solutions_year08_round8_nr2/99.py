#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <cassert>
#include <numeric>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef pair<int,int> PII;

#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define CLR(v,a) memset(v,a,sizeof(v))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define inf 1000000000
#define MAX_N 1000

int t, n, m, ans;
int minO[3000];
vector< pair<int, pair<int,int> > > tab;
vector<PII> moz[3000];
map<string,int> mapa;
map<int,int> wsp;
bool can[MAX_N];

int check()
{
	REP(i,m) minO[i] = inf;
	minO[0] = 0;

	REP(i,m)
	{
		REP(j,(int)moz[i].size()) {
			if (!can[moz[i][j].FI]) continue;
			int nn = inf;
			FOR(k,moz[i][j].SE-1,i-1) nn = min(nn, minO[k]);
			minO[i] = min(minO[i], nn+1);
		}
	}
	
	//REP(i,m) printf("%d ", minO[i]); printf("\n");
	return minO[m-1];
}

void go(int last, int left)
{
	if (left == 0)
	{
		ans = min(ans, check());
		return;
	}
	FOR(i,last,(int)mapa.size()-1) {
		can[i] = true;
		go(i+1,left-1);
		can[i] = false;
	}
}

int main()
{
	scanf("%d", &t);
	FOR(tc,1,t)
	{
		scanf("%d", &n);
		REP(i,n)
		{
			int id, a, b;
			char name[50];
			scanf("%s %d %d", name, &a, &b);
			if (mapa.find(name) != mapa.end())
				id = mapa[name];
			else {
				id = mapa.size();
				mapa[name] = id;
			}
			wsp[a] = 0, wsp[b] = 0;
			if (a-1>=0) wsp[a-1] = 0;
			if (b-1>=0) wsp[b-1] = 0;
			tab.PB(MP(id,MP(a,b)));
		}

		CLR(can,0);

		int nwsp = 0;
		wsp[0] = 0;
	  	wsp[10000] = 0;
		FOREACH(it,wsp) it->second = nwsp++;
		
		REP(i,n)
	  	{
			tab[i].SE.FI = wsp[tab[i].SE.FI];
		  	tab[i].SE.SE = wsp[tab[i].SE.SE];
			assert(tab[i].SE.FI <= tab[i].SE.SE);
		}

		REP(i,n) moz[tab[i].SE.SE].PB(MP(tab[i].FI,tab[i].SE.FI));

		m = wsp.size();

		/*REP(i,m) {
			printf("%d: ", i);
			REP(j,(int)moz[i].size()) printf("%d ", moz[i][j].SE);
			printf("\n");
		}*/

		
		ans = inf;
		go(0,1);
		go(0,2);
		go(0,3);

		tab.clear();
	  	wsp.clear();
	  	mapa.clear();
		REP(i,m) moz[i].clear();

		printf("Case #%d: ", tc);
		if (ans == inf) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);

		//break;
	}
	return 0;
}
