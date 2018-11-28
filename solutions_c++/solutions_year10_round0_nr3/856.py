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

void scase() {
	int r, k, n;
	scanf("%d%d%d",&r,&k,&n);
	VI g(n);
	REP(i,n) scanf("%d",&g[i]);
	VI nx(n), sm(n);
	REP(i,n) {
		int j, cnt=0;
		for (j=0; j < n && cnt+g[(i+j)%n] <= k; ++j) 
			cnt += g[(i+j)%n];
		nx[i] = (i+j)%n;
		sm[i] = cnt;
	}
	LL ret=0;
	int j=0;
	REP(i,r) {
		ret += sm[j];
		j = nx[j];
	}
	printf("%lld\n",ret);
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
