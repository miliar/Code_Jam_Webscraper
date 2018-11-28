#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <sstream>
#include <bitset>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
typedef unsigned long long UL;
typedef long double LD;
typedef pair<int,int> PII;

const int INF = 1000*1000*1000+1;
#define FOR(x,b,e) for (int x = (b); x < (e); ++x)
#define FORD(x,b,e) for (int x = (b); x >= (e); --x)
#define REP(x,n) for (int x = 0; x < (n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i,c) for (VAR(i,(c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

typedef vector<PII> VP;

void scase() {
	int n, k, b, t;
	scanf("%d%d%d%d",&n,&k,&b,&t);
	VP c(n);
	REP(i,n) scanf("%d",&c[i].ST);
	REP(i,n) scanf("%d",&c[i].ND);
	sort(ALL(c));
	int chicks=0;
	int swaps=0;
	FORD(i,n-1,0) {
		if (chicks == k) break;
		if (b-c[i].ST <= c[i].ND*t) { chicks++; }
		else swaps += k-chicks;
	}
	if (chicks < k) printf("IMPOSSIBLE\n");
	else printf("%d\n",swaps);
}

int main() {
	int z;
	scanf("%d",&z);
	REP(i,z) {
		printf("Case #%d: ",i+1);
		scase();
	}

	return 0;
}
