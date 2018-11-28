#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <vector>
#include <map>
#include <string>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)

void openfiles()
{
#ifndef ONLINE_JUDGE
	//string file = "A-small-attempt2";
	string file = "A-large";
	//string file = "test";
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}


#define SOLVE_VOID
#ifdef SOLVE_VOID
void solve(int test)
{
	long long N, K;
	scanf("%lld %lld ",&N,&K);
	long long MOD = (1 << N);

	static int ntest = 0;
	printf("Case #%d: %s\n", ++ntest, (K % MOD == MOD - 1) ? "ON" : "OFF");
}
#endif

int main()
{
	openfiles();
	#ifdef SOLVE_BOOL
		while(solve());
	#endif
	#ifdef SOLVE_VOID
		int n; scanf("%d ",&n); REP(i,n) solve(i);
	#endif
	
	return 0;
}