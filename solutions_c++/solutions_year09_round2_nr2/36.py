#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef long long i64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

int L;
char stg[1024];

bool next_no_add(int first)
{
	if (first == L-1)
		return false;

	if (next_no_add(first+1))
		return true;

	int sw = first+1;
	FOR(i, first+1, L)
		if (stg[i] > stg[first] && stg[i] < stg[sw])
			sw = i;

	if (stg[sw] > stg[first]) {
		swap(stg[sw], stg[first]);
		sort(stg+first+1, stg+L);
		return true;
	} else
		return false;
}

void solve()
{
	gets(stg);
	L = strlen(stg);
	if (next_no_add(0)) {
		puts(stg);
		return;
	}
	
	// Count and remove 0's
	int n0 = 0, k = 0;
	REP(i, L)
		if (stg[i] == '0')
			n0++; else
			stg[k++] = stg[i];
	sort(stg, stg+k);

	putchar(stg[0]);
	REP(i, n0+1)
		putchar('0');
	FOR(i, 1, k)
		putchar(stg[i]);
	puts("");
}

int main()
{
//	freopen("input.txt", "r", stdin);
	
	int n_test;
	scanf("%d\n", &n_test);
	REP(i_test, n_test) {
		printf("Case #%d: ", i_test+1);
		solve();
	}

	return 0;
}
