#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	//freopen("Lin.txt", "r", stdin);
	//freopen("Lout.txt", "w", stdout);

	int t, n;
	int result, tmp, sum;
	int minV;

	scanf("%d", &t);

	for (int cas = 1; cas <= t; cas ++) {
		scanf("%d", &n);

		sum = 0;
		result = 0;
		minV = 0x7fffffff;

		for (int i = 0; i < n; i ++) {
			scanf("%d", &tmp);
			result ^= tmp;
			minV = min(minV, tmp);
			sum += tmp;
		}

		printf("Case #%d: ", cas);
		if (result == 0)
			printf("%d\n", sum - minV);
		else
			puts("NO");
			
	}
}