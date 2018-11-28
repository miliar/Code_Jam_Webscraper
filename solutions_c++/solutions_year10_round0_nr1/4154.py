/*******************************************************************************
* Program: snapper_chain;
* Copyright (c) 08 May 2010, Mateusz Kwiatek;
* email: <kwiatek.mateusz@gmail.com>
*******************************************************************************/
/*******************************************************************************
* Codejam 2010
* http://code.google.com
* ROUND: 0;
* TASK: Snapper Chain;
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

const int max_n = 30;
// 1 <= n <= max_n
const int max_k = 100000000;
// 1 <= k <= max_k
//------------------------------------------------------------------------------

void testcase() {
	int n, k;
	scanf("%d %d", &n, &k);
	if (k&((1<<n)-1) == (1<<n)-1)
		printf("ON\n");
	else
		printf("OFF\n");
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
