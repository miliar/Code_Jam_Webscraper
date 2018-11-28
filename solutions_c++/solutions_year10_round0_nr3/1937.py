#include <stdlib.h>
#include <stdio.h>
#include <memory.h>

const char inFileName[] = "C-large.in";
const char outFileName[] = "C-large.out";

const int MaxN = 1010;

int T, r, n, k;
int g[2 * MaxN], nextGroup[MaxN];
long long groupPrice[MaxN];
bool mark[MaxN];

long long Solve() {
	int i, j = 0, num = 0;
	int cycleLength, count;
	long long cyclePrice, sol;

	for (i = 1; i <= n; i++) {
		num -= g[i - 1];
		while (num + g[j + 1] <= k && j + 1 < n + i) {
			j++;
			num += g[j];
		}
		groupPrice[i] = num;
		nextGroup[i] = (j + 1 <= n ? j + 1 : j + 1 - n);
	}

	memset(mark, false, sizeof(mark));
	i = 1; mark[1] = true;
	while (!mark[nextGroup[i]]) {
		i = nextGroup[i];
		mark[i] = true;
	}
	j = i;
	cycleLength = 1;
	cyclePrice = groupPrice[i];
	while (nextGroup[j] != i) {
		j = nextGroup[j];
		cycleLength++;
		cyclePrice += groupPrice[j];
	}
	
	sol = 0;
	j = 1; count = 0;
	while (j != i && count < r) {
		sol += groupPrice[j];
		count++;
		j = nextGroup[j];
	}
	if (count == r) return sol;

	r = r - count;
	sol = sol + (r / cycleLength) * cyclePrice;
	r = r % cycleLength;
	j = i;
	count = 0;
	while (count < r) {
		sol += groupPrice[j];
		count++;
		j = nextGroup[j];
	}
	return sol;
}

int main() {
	
	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int i = 0; i < T; i++) {
		fscanf(inFile, "%d%d%d", &r, &k, &n);
		memset(g, 0, sizeof(g));
		for (int j = 1; j <= n; j++) {
			fscanf(inFile, "%d", &g[j]);
			g[j + n] = g[j];
		}
		fprintf(outFile, "Case #%d: %I64d\n", i + 1, Solve());
	}	
	
	fclose(inFile);
	fclose(outFile);
	return 0;
}
