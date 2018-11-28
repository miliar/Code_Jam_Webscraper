#include <cstdio>
#include <cmath>

const int MAX_N = 2005;
const double E = 1e-6;
int N, T, peaks[MAX_N], heights[MAX_N];

bool gteq(double a, double b) {
	return a > b - E;
}

bool gt(double a, double b) {
	return a > b+E;
}

bool equ(double a, double b) {
	return fabs(a-b) < E;
}

bool over(int stindex, int enindex, int overindex) {
	double stheight = heights[stindex], enheight = heights[enindex], overheight = heights[overindex];
	double rrun = (double(enheight-stheight))/(double(enindex-stindex));
	double proj = stheight+rrun*(overindex-stindex);
	return gteq(overheight, proj);
}

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &N);
		for (int i = 0; i < N-1; ++i) {
			scanf("%d", &peaks[i]);
			peaks[i]--;
			heights[i] = 0;
		}
		bool okay = false;
		for (int i = 0; i < 1000000; ++i) {
			okay = true;
			for (int i = 0; i < N; ++i) {
				for (int j = 0; j < i; ++j) {
					if (i == peaks[j]) continue;
					while (over(j, peaks[j], i)) {
						okay = false;
						if (i < peaks[j]) heights[j]++;
						else heights[peaks[j]]++;
					}
				}
			}
			if (okay) break;
		}
		printf("Case #%d:", t);
		if (!okay) printf(" Impossible");
		else {
			for (int i = 0; i < N; ++i) {
				printf(" %d", heights[i]);
			}
		}
		printf("\n");

	}
}