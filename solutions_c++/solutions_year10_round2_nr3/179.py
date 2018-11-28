/*******************************************************************************
* Program: your_rank_is_pure;
* Copyright (c) 22 May 2010, Mateusz Kwiatek;
* email: <kwiatek.mateusz@gmail.com>
*******************************************************************************/
/*******************************************************************************
* Codejam 2010
* http://code.google.com
* ROUND: 1B;
* TASK: Your Rank is Pure;
*******************************************************************************/

#define REP(i,n) for (int i = 0, _n = (n); i < _n; ++i)
#define REPD(i,n) for (int i = (n)-1; i >= 0; --i)
#define REPS(i,f,l) for (int i = (f), _l = (l); i < _l; ++i)
#define REPSD(i,f,l) for (int i = (l)-1, _f = (f); i >= _f; --i)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; ++i)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; --i)
#define FORE(it,c) for (__typeof((c).begin()) it = (c).begin(), _l = (c).end(); it != _l; ++it)
#define FORED(it,c) for (__typeof((c).rbegin()) it = (c).rbegin(), _l = (c).rend(); it != _l; ++it)
#define FOREACH(it,f,l) for (__typeof(f) it = (f), _l = (l); it != _l; ++it)
#define FOREACHD(it,f,l) for (__typeof(f) it = (l), _f = (f); it-- != _f; )
#define FORV(i,V) REP(i,(V).size())
#define ll long long

#include <cstdio>

using namespace std;

const int max_n = 500;
// 2 <= n <= max_n
const int mod = 100003;
//------------------------------------------------------------------------------

// N[n][k] = newton(n, k)
int N[max_n+1][max_n+1];
// C[n][k] = number of `k`-elements ascending sequences meeting problem
//   requirements where each element e[2..n] and last element equals `n`
int C[max_n+1][max_n+1];

void testcase() {
	int n;
	scanf("%d", &n);
	int res = 0;
	FOR(k,1,n-1) {
		res += C[n][k];
		if (res >= mod)
			res -= mod;
	}
	printf("%d\n", res);
}

int main()
{
	N[0][0] = 1;
	FOR(n,0,max_n) FOR(k,n+1,max_n)
		N[n][k] = 0;
	FOR(n,0,max_n) N[n][0] = 1;
	FOR(n,1,max_n) FOR(k,1,n) {
		N[n][k] = N[n-1][k-1]+N[n-1][k];
		if (N[n][k] >= mod)
			N[n][k] -= mod;
	}
	
	FOR(n,2,max_n) {
		C[n][0] = 0;
		C[n][1] = 1;
		FOR(k,2,n-1) {
			C[n][k] = 0;
			FOR(q,1,k-1) {
				C[n][k] += (C[k][q]*1LL*N[n-1-k][k-1-q])%mod;
			}
		}
	}
	/*
	FOR(n,0,10) {
		FOR(k,0,n)
			printf("%d ", N[n][k]);
		putchar('\n');
	}
	FOR(n,1,10) {
		FOR(k,1,n-1)
			printf("%d ", C[n][k]);
		putchar('\n');
	}
	*/
	
	int z;
	scanf("%d\n", &z);
	REP(tid,z) {
		printf("Case #%d: ", tid+1);
		testcase();
	}
	return 0;
}
