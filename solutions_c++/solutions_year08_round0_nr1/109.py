#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))
#define inf 1000000

using namespace std;

map<string, int> m;
int q, s, a[1005], dp[105];
char buf[1000];

void solvecase() {
	m.clear();
	scanf("%d\n", &s);
	FOR(i, s) {
		gets(buf);
		m[string(buf)] = i;
	}
	scanf("%d\n",  &q);
	FOR(i, q) {
		gets(buf);
		a[i] = m[string(buf)];
	}
	int mi;
	FOR(i, s) dp[i] = i == a[0] ? inf : 0;
	for (int i = 1; i < q; i++) {
		mi = inf;
		FOR(j, s) mi = min(mi, dp[j]);
		FOR(j, s) if (j == a[i]) {
			dp[j] = inf;
		} else {
			dp[j] = min(dp[j], mi + 1);
		}
	}
	mi = inf;
	FOR(j, s) mi = min(mi, dp[j]);
	printf("%d", mi);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
//	freopen("D:\Data\Firefox_Downloads\a-small-attempt0.in", "rt", stdin);
//	freopen("D:\Data\Firefox_Downloads\a-large.in", "rt", stdin);
	freopen("a-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}