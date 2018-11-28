#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int t, pd, pg;
long long n;
bool ans;
int main() {
	FILE *fin = fopen("a.in", "r");
	FILE *fout = fopen("a.out", "w");

	fscanf(fin, "%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		fscanf(fin, "%lld %d %d", &n, &pd, &pg);

		ans = false;
		if ((pg == 100 && pd < 100) || (pg == 0 && pd > 0)) ans = false;
		else {
			int g = 0;
			for (int i = 1; i <= 100; i++) {
				if (i*pd % 100 == 0) {
					g = i;
					break;
				}
			}
			if ((long long)g <= n) ans = true;
		}

		if (ans) fprintf(fout, "Case #%d: Possible\n", cas);
		else fprintf(fout, "Case #%d: Broken\n", cas);
	}
	return 0;
}
