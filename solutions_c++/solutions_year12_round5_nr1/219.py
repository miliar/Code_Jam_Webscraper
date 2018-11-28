#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define DEBUG(x) cout << ">>> " << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)

#define INF (1<<29)
typedef long long ll;

#define MAXN 25

int t, T, N;
int L[MAXN], P[MAXN];
int srt[MAXN];

bool lt(int i1, int i2) { return P[i1] > P[i2]; }

int main() {
	scanf("%d", &T);
	t = 0;
	while (t < T) {
		++t;
		scanf("%d", &N);
		REP(i,N) scanf("%d", L+i);
		REP(i,N) scanf("%d", P+i);
		REP(i,N) srt[i] = i;
		stable_sort(srt, srt+N, lt);
		printf("Case #%d:", t);
		REP(i,N) printf(" %d", srt[i]);
		printf("\n");
	}
	return 0;
}
