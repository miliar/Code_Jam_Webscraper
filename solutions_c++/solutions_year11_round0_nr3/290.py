#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int testCount, nCount;
	int sum, xsum, minv;
	int x;
	
	freopen("c1.in", "r", stdin);
	freopen("c.out", "w", stdout);	
	scanf("%d", &testCount);
	for (int tc = 1; tc <= testCount; tc++) {
		scanf("%d", &nCount);
		sum = 0;
		xsum = 0;
		minv = 1 << 25;
		for (int i = 0; i != nCount; i++) {
			scanf("%d", &x);
			sum += x;
			xsum ^= x;
			minv = min(minv, x);
		}
		printf("Case #%d: ", tc);
		if (xsum == 0)
			printf("%d\n", sum - minv);
		else
			printf("%s\n", "NO");
	}
	return 0;
}
