#include <iostream>

using namespace std;

int main() {

	int Tc; 

	
	freopen("C-large.in", "r", stdin);
	freopen("qc-large.out", "w", stdout);

	scanf("%d", &Tc);

	for (int tc = 1; tc <= Tc; ++tc) {

		int n;

		scanf("%d", &n);
		
		int sum = 0;
		int s = 0;
		int min = 10000000;

		for (int i = 0; i < n; ++i) {
			int v;
			scanf("%d", &v);
			s = s ^ v;
			sum += v;
			if (v < min) {
				min = v;
			}
		}

		printf("Case #%d: ", tc);

		if (s != 0) {
			printf("NO\n");
		} else {
			printf("%d\n", sum - min);
		}

	}

	return 0;
}
