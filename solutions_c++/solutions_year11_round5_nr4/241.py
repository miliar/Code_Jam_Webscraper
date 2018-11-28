#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

const int maxn = 200;

int a[maxn], ans[maxn], pos[maxn];
char s[maxn];
int len, n;
int ok;

void check() {
	long long t = 0;
	for (int i=0;i<len;i++)
		t = (t << 1) + a[i];

	long long x = (long long)(sqrt((double)t));
	if ((x - 1) * (x - 1) == t ||
		(x + 1) * (x + 1) == t ||
		x * x == t) {

		ok = 1;
		memcpy(ans, a, sizeof(a));
		return;
	}
}

void search(int dep) {
	if (dep == n) {
		check();
		return;
	}
	if (ok) return;
	for (int x=0;x<=1;x++) {
		a[pos[dep]] = x;
		search(dep + 1);
		a[pos[dep]] = 0;
	}
}

int main() {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int ti=1;ti<=T;ti++) {
		scanf("%s", &s);
		len = strlen(s);
		n = 0;
		ok = 0;
		for (int i=0;i<len;i++)
			if (s[i] == '?') {
				pos[n++] = i;
				a[i] = 0;
			}
			else a[i] = (s[i] - '0');
		search(0);
		printf("Case #%d: ", ti);
		for (int i=0;i<len;i++) printf("%d", ans[i]);
		printf("\n");
	}
	return 0;
}
