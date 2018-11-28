#pragma warning (disable:4786) 
#pragma warning (disable:4996) 
#include <time.h>
#include <algorithm> 
#include <iostream>  
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <stack>
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <cassert>
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
#define FILL(a,b) memset(a, (b), sizeof(a));
typedef long long ll; 
const double EPS = 1e-7;

void openfiles() {
	#ifndef ONLINE_JUDGE
		freopen("C-large.in","rt",stdin);
		freopen("C-large.out","wt",stdout);   
	#endif
}


void solve() {
	const char* codejam = " welcome to code jam";

	int dp[505][30];
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;

	char line[505];
	gets(line + 1);
	int linelen = strlen(line);

	for (int i = 1; i <= linelen; i++) {
		for (int j = 1; j <= 19; j++) {
			if (line[i] == codejam[j]) {
				dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % 10000;
			}
		}

		for (int j = 0; j <= 19; j++) {
			dp[i][j] = (dp[i][j] + dp[i - 1][j]) % 10000;
		}
	}

	int sum = dp[linelen][19];

	static int ntest = 0;
	printf("Case #%d: %04d\n", ++ntest, sum);
}

int main() {
	openfiles();
	int n;
	scanf("%d ",&n);
	REP(i,n) solve();

	return 0;
}