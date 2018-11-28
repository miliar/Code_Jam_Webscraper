#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;
const int maxn = 10000;
int a[maxn];
int n, L, H;

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d %d %d", &n, &L, &H);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		int res = -1;
		for (int i = L; i <= H; i++) {
			bool ok = true;
			for (int j = 0; j < n; j++) {
				if (a[j] % i == 0 || i % a[j] == 0)
					continue;
				else {
					ok = false;
					break;
				}
			}
			if (ok) {
				res = i;
				break;
			}
		}
		if (res == -1) 
			printf("Case #%d: NO\n", t);
		else
			printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
