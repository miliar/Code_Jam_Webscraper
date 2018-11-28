#include <cstdio>
#include <cstdlib>

int main(void) {
	int t;
	int n, k;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		scanf("%d%d", &n, &k);
		bool res = true;
		for (int j = 0; j < n; ++j)
			if ((k & (1 << j)) == 0) {
				res = false;
			}
//		bool res = (k & (1 << (n))) > 0;
		printf("Case #%d: %s\n", i + 1, (res) ? "ON" : "OFF");
		
	}
	return 0;
}
