#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int MAXN = 1011;
int a[MAXN], b[MAXN];

int main()
{
	freopen("d.in", "rt", stdin);
	freopen("d.out", "wt", stdout);
	int T;
	int n;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		sort(a, a + n);
		int cnt = 0;
		for (int i = 0; i < n; ++i)
			if (a[i] != b[i]) ++cnt;
		printf("Case #%d: %d.000000\n", tt, cnt);
	}
	return 0;
}
