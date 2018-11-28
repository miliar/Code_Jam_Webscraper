#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#define mp make_pair
#define st first
#define nd second
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORO(i,n) for(int i=1;i<=(n);i++)
#define FORS(i,a,n) for(int i=(a);i<(n);i++)
#define FORB(i,a,n) for(int i=(a);i>=(n);i--)
#define FORE(i,v) for(typeof((v).begin())i=(v).begin();i!=(v).end();i++)
#define INRANGE(a,b,c,d) ((a)>=0&&(b)>=0&&(a)<(c)&&(b)<(d))
#define pf printf
typedef long long ll;
using namespace std;

typedef pair<int, int> pii;

ll L, T, N, C;
int A[1500];
pii V[1500];

void solve() {
	scanf("%lld%lld%lld%lld", &L, &T, &N, &C);
	FOR(i, C)
		scanf("%d", &A[i]);
	int full_ct = N / C, rem_lim = N % C;
	FOR(i, C) {
		V[i] = mp(A[i], full_ct + (i < rem_lim));
	}
	//pf("\n");
	ll tdist = T >> 1;
	ll left_dist = tdist;
	ll time_spent = 0;
	for (int i = 0, j = 0; i < N; i++, j = (j == C-1) ? 0 : (j+1)) {
		if (V[j].st > left_dist) {
			ll left = V[j].st - left_dist;
			left_dist = 0;
			time_spent += 2 * (V[j].st - left);
			V[j].nd--;
			V[C] = mp(left, 1);
			C++;
			break;
		}
		left_dist -= V[j].st;
		time_spent += V[j].st * 2;
		V[j].nd--;
	}
	//FOR(i, C)
	//	pf("(%d; %d)\n", V[i].st, V[i].nd);
	if (left_dist > 0) {
		pf("%lld\n", time_spent);
		return;
	}
	sort(V, V + C, greater<pii>());
	FOR(i, C) {
		if (L > 0) {
			int nboost = min(V[i].nd, (int)L);
			time_spent += V[i].st * nboost;
			L -= nboost;
			V[i].nd -= nboost;
		}
		time_spent += V[i].st * 2 * V[i].nd;
	}
	pf("%lld\n", time_spent);
}

int main() {
	//freopen(".in", "r", stdin); freopen(".out", "w", stdout);
	int n;
	scanf("%d", &n);
	FORO(i, n) {
		pf("Case #%d: ", i);
		solve();
	}
}


