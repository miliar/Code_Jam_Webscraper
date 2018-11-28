#include <stdio.h>
#include <vector>
#include <algorithm>

int main(int argc, char* argv[])
{
	FILE* fp = fopen(argv[1], "r");
	if (!fp) return 1;

	int total;
	fscanf(fp, "%d\n", &total);

	std::vector<int> v;
	int n, k;
	for (int line = 1; line <= total; line++) {
		fscanf(fp, "%d %d\n", &n, &k);
//		printf("%d %d\n", n, k);
#if 1
//		printf("\t");

		int i;
		for (i = 0; i < n; i++) {
//			printf("%d ", k & 1);
			if ((k & 1) == 0) break;
			k >>= 1;
		}
		if (i == n) {
			printf("Case #%d: ON\n", line);
		} else {
			printf("Case #%d: OFF\n", line);
		}
#else
		v.clear();
		v.resize(n);

		for (int i = 0; i < k; i++) {
			std::vector<int>::iterator it = std::find(v.begin(), v.end(), 0);
			int length = it != v.end() ? &(*it) - &v[0] : 1;
			std::fill(v.begin(), v.begin() + length, 0);
			v[length] = 1;
		}

		printf("\t");
		for (int i = 0; i < n; i++) {
			printf("%d ", v[i]);
		}
		puts("");
#endif
	}

	fclose(fp);
	return 0;
}
