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

const int MaxN = 64;

int N;
int a[MaxN], b[MaxN], c[MaxN];

bool can_solve(int start, int end)
{
	copy(b, b+N, c);
	sort(c+start, c+end);
	for (int i = start; i < end; i++)
		if (c[i] > i)
			return false;
	return true;
}

void solve()
{
	scanf("%d\n", &N);
	REP(i, N) {
		static char stg[1024];
		gets(stg);
		int &r = a[i];
		r = 0;
		REP(j, N)
			if (stg[j] == '1')
				r = j;
	}

	int ans = 0;
	REP(i, N) {
		bool ok = false;
		for (int j = i; j < N; j++) {
			if (a[j] > i)
				continue;

			b[i] = a[j];
			copy(a+i, a+j, b+i+1);
			copy(a+j+1, a+N, b+j+1);
			if (can_solve(i+1, N)) {
				ok = true;
				ans += j-i;
				copy(b+i, b+N, a+i);
				break;
			}
		}
		if (!ok)
			puts("shit");
	}

	printf(" %d\n", ans);
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);

	int n_test;
	scanf("%d\n", &n_test);
	REP(i_test, n_test) {
		printf("Case #%d:", i_test+1);
		solve();
	}

	return 0;
}
