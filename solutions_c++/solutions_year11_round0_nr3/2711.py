#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>

using namespace std;

int t, n, a, xor_sum, sum, _min;

int main()
{
	int i, j;

	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d", &n);
		scanf("%d", &a);
		xor_sum = sum = _min = a;
		for (j = 1; j < n; j++) {
			scanf("%d", &a);
			xor_sum ^= a;
			sum += a;
			_min = min(_min, a);
		}
		printf("Case #%d: ", i + 1);
		if (xor_sum != 0)
			printf("NO\n");
		else
			printf("%d\n", sum - _min);
	}

	return (0);
}


