#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
	int T;
	scanf("%d", &T);

	for (int cs = 1; cs <= T; cs++) {
		int N;
		int min = 1000001;
		int sum = 0, sumbit = 0;

		scanf("%d", &N);
		for (int j = 0; j < N; j++) {
			int C;

			scanf("%d", &C);
			if (C < min)
				min = C;
			sum += C;
			sumbit ^= C;
		}

		printf("Case #%d: ", cs);
		if (sumbit != 0)
			printf("NO\n");
		else
			printf("%d\n", sum - min);
	}

	return 0;
}
