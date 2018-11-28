#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <functional>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define REP(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define FOR(i, a, b) for (int i = (a), _n = (b); i <= _n; ++i)
#define FORD(i, a, b) for (int i = (a), _n = (b); i >= _n; --i)
#define FORE(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int PMAX = 400;

const int INF = 1000000000;

const int NMAX = 1000;

struct node {
	int val, cnt, starts;
};

int N;
node T[NMAX], TT[NMAX];

bool ok(int K) {
	REP(i, N) TT[i] = T[i]; 
	FORD(ind, N-1, 0) {
		int cnt_st = ind == N-1 || TT[ind].val+1 != TT[ind+1].val ? 0 : TT[ind+1].starts;
		cnt_st = min(cnt_st, TT[ind].cnt);
		TT[ind].starts += cnt_st;
		TT[ind].cnt -= cnt_st;
		
		if (TT[ind].cnt == 0) continue;
		if (ind < K-1) return false;
		REP(ii, K) if (TT[ind-ii].val != TT[ind].val-ii || TT[ind-ii].cnt < TT[ind].cnt)
			return false;
		cnt_st = TT[ind].cnt;
		REP(ii, K) TT[ind-ii].cnt -= cnt_st;
		TT[ind-(K-1)].starts += cnt_st;
	}
	return true;
}

void testcase() {
	scanf("%d", &N);
	
	if (N == 0) {
		printf("%d\n", 0);
		return;
	}

	static int A[NMAX];
	REP(i, N) scanf("%d", A+i);
	sort(A, A+N);
	
	int newN = 0;
	for (int i = 0; i < N;) {
		int j = i+1;
		while (j < N && A[j] == A[i]) ++j;
		T[newN].val = A[i];
		T[newN].cnt = j-i;
		T[newN++].starts = 0;
		i = j;
	}
	N = newN;
	
	FORD(K, N, 1) if (ok(K)) {
		printf("%d\n", K);
		return;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(i, 1, T) {
		printf("Case #%d: ", i);
		testcase();
	}
}
