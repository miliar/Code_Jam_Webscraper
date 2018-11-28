#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 10000+5;


int n;
int d[MAXN], l[MAXN];
int x[MAXN];
int D;

void solve() {
	bool res = false;

	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		scanf("%d %d", &d[i], &l[i]);
	}

	scanf("%d", &D);

	for(int i = 0; i < n; i++) x[i] = 0;

	x[0] = d[0];
	for(int i = 0; i < n; i++) {
		for(int j = i; j < n && d[j] <= d[i] + x[i]; j++) {
			x[j] = max(x[j], min(l[j], d[j]-d[i]));
		}

		res = res || (d[i]+x[i] >= D);

	}




	printf("%s", res?"YES":"NO");
}

int main() {
	int t;
	scanf("%d\n", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
		printf("\n");
	}

}