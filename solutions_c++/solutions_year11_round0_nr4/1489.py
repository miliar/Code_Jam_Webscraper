#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
	int nt;
	scanf("%d", &nt);
	for (int it = 1; it <= nt; it++) {
		int n;
		scanf("%d", &n);
		vector<int> a(n);
		int pts = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			a[i]--;
			if (a[i] != i) {
				pts++;
			}
		}
		printf("Case #%d: %.10lf\n", it, (double)pts);
	}
	return 0;
}
