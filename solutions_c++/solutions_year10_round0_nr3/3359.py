#include <stdio.h>
#include <vector>
#include <algorithm>

int main(int argc, char* argv[])
{
	FILE* fp = fopen(argv[1], "r");
	if (!fp) return 1;

	int total;
	fscanf(fp, "%d\n", &total);

	int r, k, n;
	std::vector<int> v;
	for (int line = 1; line <= total; line++) {
		fscanf(fp, "%d %d %d\n", &r, &k, &n);
		v.clear();
		v.resize(n);

		for (int i = 0; i < n; i++) {
			fscanf(fp, "%d", &v[i]);
			fgetc(fp);
		}

		__int64 euro = 0;
		int g = 0;
		int left = v.size();
		for (int i = 0; i < r; i++) {
			int kk = k;
			for (;;) {
				if (kk - v[g] < 0) break;
				kk -= v[g];
				euro += v[g];
				left--;
				if (++g >= n) {
					g = 0;
					if (left == 0) break;
				}
			}
			left += v.size();
		}

		printf("Case #%d: %I64d\n", line, euro);
	}

	fclose(fp);
	return 0;
}
