#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<utility>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;

#define MP make_pair
#define PB push_back
#define REP(i, n) for(int i=0, _n=(n); i<_n; ++i)
#define min(a, b) ((a)<(b)?(a):(b))
#define max(a, b) ((a)>(b)?(a):(b))

const int MAXN = 222;
const int inf = 2000000000;

LL p[MAXN], v[MAXN];
int n;
LL d;

bool check(LL x)
{
	LL last = p[0] - x;
	for (int i = 0; i < n; ++i) {
//		cout << last << endl;
		if (last < p[i] - x) last = p[i] - x;
		last += d * (v[i] - 1);
		if (abs(last - p[i]) > x) return false;
		last += d;
	}
	return true;
}

int main()
{
	freopen("b.in", "rt", stdin);
	freopen("b3.out", "wt", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		int dd;
		scanf("%d%d", &n, &dd);
		d = dd * 2;
		for (int i = 0; i < n; ++i) {
			int pp, vv;
			scanf("%d%d", &pp, &vv);
			p[i] = pp * 2;
			v[i] = vv;
		}
		LL L = 0, R = (long long) inf * inf;
		while (L < R) {
			LL mid = (L + R) / 2;
			if (check(mid)) R = mid;
			else L = mid + 1;
		}
		printf("Case #%d: ", tt);
		if (R & 1) {
			printf("%I64d.5\n", R/2);
		} else printf("%I64d.0\n", R/2);
	}
	return 0;
}
