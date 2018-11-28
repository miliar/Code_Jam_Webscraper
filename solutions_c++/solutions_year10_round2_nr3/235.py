#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
using namespace std;

#define CLR(a, x) memset(a, x, sizeof(a)) // x = 0|-1, true|false.
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<=(b); i++)
#define FORD(i, b, a) for(int i=(b); i>=(a); i--)
#define FORE(ty, it, data) for(ty::iterator it=data.begin(); it!=data.end(); it++)
#define ALL(x) (x).begin(),(x).end()
#define TWO(X) (1<<(X))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define EPS 1e-10
const double PI = acos(-1.0);

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef map<string, int> MSI;

template<typename T> string toString(const T &n) { ostringstream O; O<<n; return O.str(); }

////////////////////////////////////////////////////////////////////////////////////////////////////////

#define MOD 100003

int gop(int x, int y)
{
	return ((ll)x*y)%MOD;
}
int hap(int x, int y)
{
	return (x+y)%MOD;
}

// nCk for small N, K: make Combination Table
// (int) N<=33, (long long) N<=66.
int combi[555][555]; 
void makeCombi(const int& N) {
	FOR(i, 0, N) {
		combi[i][0] = 1;
		FOR(j, 1, i)	combi[i][j] = hap(combi[i-1][j-1], combi[i-1][j]);
	}
}

int dp[555][555], sol[555];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	CLR(combi, 0);
	makeCombi(510);

	int N=500, K=500;
	CLR(dp, 0);
	dp[2][1] = 1;
	FOR(n, 3, N) {
		dp[n][1] = 1;
		FOR(k, 2, n-1) {

			int nn = k;
			int mid = n - nn - 1;
			FOR(kk, 1, min(k-1, nn-1)) {
				int here = gop(dp[nn][kk], combi[mid][k-kk-1]);
				dp[n][k] = hap(dp[n][k], here);
			}

		}
	}

	FOR(n, 2, N) {
		sol[n] = 0;
		FOR(k, 1, n-1) {
			sol[n] = hap(sol[n], dp[n][k]);
		}
	}


	int T;
	scanf("%d\n", &T);
	FOR(tc, 1, T) {
		printf("Case #%d: ", tc);

		int i;
		scanf("%d", &i);
		printf("%d\n", sol[i]);





		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}