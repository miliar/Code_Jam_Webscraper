#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <complex>
#include <functional>
#include <bitset>
#include <string>
#include <valarray>
#include <algorithm>
using namespace std;

#define MP(a,b)     make_pair(a,b)
#define two(i)      (1<<(i))
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,s,e)  for(int i=(s); i<(e); ++i)
#define FORD(i,s,e) for(int i=(s); i>=(e); --i)



void solve() {
	int  T;
	scanf("%d", &T);
	REP(IT, T) {
		int  N;
		long long  K;
		scanf("%d%lld", &N, &K);
		long long  tot = 1LL<<N;
		K %= tot;
		printf("Case #%d: %s\n", IT+1,
			(K+1==tot) ? "ON" : "OFF");
	}
}

string name = "A-large";

void set_file() {
	string in = name+".in";
	string ou = name + ".out";
	freopen(in.c_str(), "r", stdin);
	freopen(ou.c_str(), "w", stdout);
}

int  main(int argc, char* argv[])
{
	set_file();
	solve();
	return 0;
}