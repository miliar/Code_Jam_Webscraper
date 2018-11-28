#include <cstdio>

const int MAX_M = 1500;
int T, P;
int m[MAX_M];

int solve(int start, int size) {
	if (size == 1) return 0;
	bool game = false;
	for (int i = start; i < start+size; ++i)
	 if (m[i] < P) game = true;
	if (!game) return 0;
	for (int i = start; i < start+size; ++i)
		m[i]++;
	return solve(start, size/2)+solve(start + size/2, size/2)+1;
}

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &P);
		for (int p = 0; p < (1<<P); ++p)
			scanf("%d", &m[p]);
		for (int p = 0; p < P+1; ++p)
			while (getchar() != '\n');
		printf("Case #%d: %d\n", t, solve(0, 1<<P));
	}
}
