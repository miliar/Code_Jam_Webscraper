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
	string file = "B-small-attempt0";
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}

const int MAX = 1001;
const int MAXK = 11;
int DP[MAXK][MAX][MAX];

void precalc() {
	memset(DP, -1, sizeof(DP));
	for (int kk = 0; kk < MAXK; kk++)
	for (int i = 1; i < 1000; i++) {
		DP[kk][i][i+1] = 0;
	}
	for (int kk = 2; kk < MAXK; kk++) {
		//cout << kk << endl;
	for (int d = 2; d < MAX - 1; d++) {
		for (int i = 1; i < MAX - d; i++) {
			int j = i + d;
			if (i * kk >= j) {
				DP[kk][i][j] = 0;
				continue;
			}
			int best = 100000;
			for (int k = i + 1; k <= j - 1; k++) {
				best = min(best, max(DP[kk][i][k],DP[kk][k][j]) + 1);
			}
			DP[kk][i][j] = best;
		}
	}
	}
}

#define SOLVE_VOID
#ifdef SOLVE_VOID
void solve(int test)
{
	int a, b, k;
	scanf("%d %d %d",&a,&b,&k);
	printf("Case #%d: %d\n", test + 1, DP[k][a][b]);
}
#endif

int main()
{
	precalc();
	openfiles();
	#ifdef SOLVE_BOOL
		while(solve());
	#endif
	#ifdef SOLVE_VOID
		int n; scanf("%d ",&n); REP(i,n) solve(i);
	#endif
	
	return 0;
}