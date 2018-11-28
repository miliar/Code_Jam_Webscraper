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
#define LL          long long
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define MIN(a,b)    a = (a>(b))?(b):a
#define FOR(i,a,b)  for(int i=(a); i<=(b); ++i)
/* Prewritten code ends */

const int maxN = 111, INF = 1000000000;
int a[maxN], mem[maxN*maxN];
void fff() {
	LL L;
	int N;
	cin >> L >> N;
	REP(i,N) cin >> a[i];
	int LIM = 10001;
	REP(i,LIM) mem[i] = INF; mem[0] = 0;
	REP(i,N) REP(j,LIM-a[i]) MIN(mem[j+a[i]],mem[j]+1);
	LL mn = numeric_limits<LL>::max();
	REP(i,LIM) if(mem[i]!=INF) REP(j,N) if((L-i)%a[j]==0) MIN(mn,(L-i)/a[j]+mem[i]);
	if(mn == numeric_limits<LL>::max()) printf("IMPOSSIBLE\n");
	else printf("%lld\n",mn);
}
int main() {
	int T;
	scanf("%d",&T);
	FOR(cs,1,T) printf("Case #%d: ",cs),fff();
	return 0;
}
