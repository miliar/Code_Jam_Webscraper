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
		freopen("B-large.in","rt",stdin);
		freopen("B-large.out","wt",stdout);   
	#endif
}

int M[105][105];
char C[105][105];

bool valid (int ii, int jj, int n, int m)
{
	return ii >= 0 && ii < n && jj >= 0 && jj < m;
}

int di[] = {-1, 0, 0, 1};
int dj[] = {0, -1, 1, 0};
char gc = 'a';

char dfs (int i, int j, int n, int m)
{
	if (C[i][j]) return C[i][j];

	int mind = 100000;
	for (int k = 0; k < 4; k++) {
		int ii = i + di[k];
		int jj = j + dj[k];
		if ( valid (ii, jj, n, m) ) {
			mind = min ( mind, M[ii][jj] );
		}
	}

	for (int k = 0; k < 4; k++) {
		int ii = i + di[k];
		int jj = j + dj[k];
		if ( valid (ii, jj, n, m) && mind == M[ii][jj] && M[ii][jj] < M[i][j] ) {
			return C[i][j] = dfs (ii, jj, n, m);
		}
	}

	return C[i][j] = gc++;
}

void solve() {
	int n, m;
	scanf("%d %d ", &n, &m);
	memset(C, 0, sizeof(C));
	gc = 'a';

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%d ", &M[i][j]);

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			dfs(i, j, n, m);

	static int ntest = 0;
	printf("Case #%d:\n", ++ntest);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (j) printf(" ");
			printf("%c", C[i][j]);
		}
		printf("\n");
	}
}

int main() {
	openfiles();
	int n;
	scanf("%d ",&n);
	REP(i,n) solve();

	return 0;
}