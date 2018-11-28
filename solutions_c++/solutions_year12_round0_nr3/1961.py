#include <set>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 16;

char buff[MAXN];
int ten[MAXN];

void init() {
	ten[0] = 1;
	for (int i=1; i<MAXN; ++i) ten[i] = ten[i-1] * 10;
}

inline int len(const int x) {
	sprintf(buff, "%d", x);
	return strlen(buff);
}

int main() {
	int i, j, k;
	int m, n;
	int a, b;
	int tc, cn(0);
	int x;
	int tot;
	
//	freopen("C-large.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
	
	init();
	scanf("%d", &tc);
	while (tc--) {
		scanf("%d%d", &a, &b);
		tot = 0;
		for (i=a; i<b; ++i) {
			k = len(i);
			x = i;
			for (j=1; ; ++j) {
				x = (x % 10) * ten[k-1] + x / 10;
				if (x == i) break;
				if (i < x && x <= b) {
//					printf("%d %d\n", i, x);
					++tot;
				}
			}
		}
		printf("Case #%d: %d\n", ++cn, tot);
	}
	return 0;
}