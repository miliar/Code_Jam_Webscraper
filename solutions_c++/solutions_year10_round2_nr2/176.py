/*******************************************************************************
* Program: picking_ip_chicks;
* Copyright (c) 22 May 2010, Mateusz Kwiatek;
* email: <kwiatek.mateusz@gmail.com>
*******************************************************************************/
/*******************************************************************************
* Codejam 2010
* http://code.google.com
* ROUND: 1B;
* TASK: Picking Up Chicks;
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

const int max_b = 1000000000;
// 1 <= b <= max_b
// 0 <= x < b
const int max_t = 1000;
// 1 <= t <= max_t
const int max_v = 100;
// 1 <= v <= max_v
const int max_n = 50;
// 1 <= n <= max_n
// 1 <= k <= n
//------------------------------------------------------------------------------

int X[max_n];
int V[max_n];

void testcase() {
	int n, k, b, t;
	scanf("%d %d %d %d", &n, &k, &b, &t);
	REP(i,n)
		scanf("%d", X+i);
	REP(i,n)
		scanf("%d", V+i);
	int ok = 0;
	int swaps = 0;
	REPD(i,n) if (b-X[i] <= V[i]*t) {
		swaps += n-(i+1)-ok;
		if (++ok == k)
			break;
	}
	if (ok == k)
		printf("%d\n", swaps);
	else
		printf("IMPOSSIBLE\n");
}

int main()
{
	int z;
	scanf("%d\n", &z);
	REP(tid,z) {
		printf("Case #%d: ", tid+1);
		testcase();
	}
	return 0;
}
