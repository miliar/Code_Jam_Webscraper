#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int x[50], v[50], podeChegar[50], antes[50];
	int c, n, b, k, t;
	
	scanf("%d", &c);
	for (int test = 1; test <= c; test++) {
		scanf("%d %d %d %d", &n, &k, &b, &t);
		
		for (int i = 0; i < n; i++)
			scanf("%d", &x[i]);
		
		for (int i = 0; i < n; i++) {
			scanf("%d", &v[i]);
			podeChegar[i] = (x[i] + t * v[i]) >= b;
			antes[i] = podeChegar[i];
		}

		for (int i = 1; i < n; i++) {
			antes[i] += antes[i - 1];
		}
		
		long long swap = 0;
		int resta = k;
		
		for (int i = n - 1; i >= 0 && resta > 0; i--) {
			if (!podeChegar[i]) {
				swap += min(resta, antes[i]);
			} else
				resta--;
		}
		
		if (resta > 0)
			printf("Case #%d: IMPOSSIBLE\n", test);
		else
			printf("Case #%d: %lld\n", test, swap);
	}
	
	return 0;
}
