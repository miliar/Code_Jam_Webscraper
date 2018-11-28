#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

/* Prewritten code begins */
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,a,b)  for(int i=(a); i<=(b); ++i)
#define FILL(a,v)   memset(a,v,sizeof(a))
/* Prewritten code ends */

const int INF = 1000000000;
int mem[11][1024][11], p[32], M[1<<11], price[11][1<<11];
int f(int rnd, int a, int m) {
	//assert(rnd >= 0);
	int &res = mem[rnd][a][m];
	if(res >= 0) return res;
	//assert(a % p[rnd] == 0);
	if(rnd == 0) return res = m<=M[a] ? 0 : INF;
	return res = min(INF,min(price[rnd][a/p[rnd]]+f(rnd-1,a,m)+f(rnd-1,a+p[rnd-1],m),f(rnd-1,a,m+1)+f(rnd-1,a+p[rnd-1],m+1)));
}
int main() {
	int T, P;
	REP(i,32) p[i] = 1<<i;
	cin >> T;
	FOR(cs,1,T) {
		cin >> P;
		REP(i,p[P]) cin >> M[i];
		FOR(r,1,P) REP(i,p[P-r]) cin >> price[r][i];
		FILL(mem,0xff);
		cout << "Case #" << cs << ": " << f(P,0,0) << endl;
	}
	return 0;
}
