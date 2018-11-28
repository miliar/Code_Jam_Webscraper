#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int c = 0; c < numCases; c++) {
		int len;
		scanf("%d", &len);
		int smallest;
		scanf("%d", &smallest);
		int sum = smallest;
		int xorSum = smallest;

		for (int i = 1 ; i < len; i++) {
			int tmp;
			scanf("%d", &tmp);
			if (tmp < smallest) {
				smallest = tmp;
			}
			sum += tmp;
			xorSum ^= tmp;
		}

		if (xorSum != 0) {
			printf("Case #%d: NO\n", c + 1);
		} else {
			printf("Case #%d: %d\n", c + 1, sum - smallest);
		}
	}

	return 0;
}
