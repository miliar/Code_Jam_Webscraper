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

LL n;

const int MAXN = 1000010;
bool a[MAXN];
int p[MAXN];
int np;

int main()
{
	freopen("c.in", "rt", stdin);
	freopen("c2.out", "wt", stdout);
	memset(a, 1, sizeof(a));
	a[0]=a[1] = 0;
	for (int i = 4; i < MAXN; i += 2)
		a[i] = 0;
	for (int i = 3; i < MAXN; i += 2)
		if (a[i])
		for (int j = i + i; j < MAXN; j += i)
			a[j] = false;
	np = 0;
	for (int i = 2; i < MAXN; ++i)
		if (a[i]) p[np++] = i;
//	cout << np << endl;
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		cin >> n;
		int ans = 0;
//		cout << n << endl;
		for (int i = 0; i < np; ++i) {
			LL tmp = p[i];
			int cnt = 0;
			while (tmp * p[i] <= n) ++cnt, tmp *= p[i];
			ans += cnt;
//			cout << cnt << endl;
			if (cnt == 0) break;
		}
		if (n > 1) ans += 1;
		printf("Case #%d: %I64d\n", tt, ans);
	}
	return 0;
}
