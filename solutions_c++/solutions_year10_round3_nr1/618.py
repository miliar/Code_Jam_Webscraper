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
typedef long long i64;
typedef unsigned long long u64;

string name = "AAL";
bool   is_file__ = true;

int  N;
typedef pair<int, int> PII;

PII  A[1024];

void solve() {
	int  T;
	scanf("%d", &T);
	REP(Ti, T) {
		scanf("%d", &N);
		REP(i, N)
			scanf("%d%d", &A[i].first, &A[i].second);
		sort(A, A+N);
		int  ans = 0;
		REP(i, N) REP(j, i) if(A[i].second < A[j].second)
			++ans;
		printf("Case #%d: %d\n", Ti+1, ans);
	}
}


void set_file() {
	string in = name+".in";
	string ou = name + ".out";
	freopen(in.c_str(), "r", stdin);
	freopen(ou.c_str(), "w", stdout);
}

int  main(int argc, char* argv[])
{
	if(is_file__)
		set_file();
	solve();
	return 0;
}

