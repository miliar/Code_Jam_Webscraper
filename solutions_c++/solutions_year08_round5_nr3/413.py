#include <cstdio>
#include <cstring>

int best;
int chairs[82][82];
int M, N;

void rec(int x, int y, int s) {
	if (y == M + 1) {
		x++;
		y = 1;
		if (s + M * ((N - x + 2) / 2) <= best) {
			return;
		}
	}
	if (x == N + 1) {
		if (s > best) {
			best = s;
			//printf("%d\n", best);
		}
		return;
	}
	// seat student
	if (chairs[y][x] == 0) {
		chairs[y - 1][x + 1]++;
		chairs[y    ][x + 1]++;
		chairs[y + 1][x + 1]++;
		rec(x, y + 1, s + 1);
		chairs[y - 1][x + 1]--;
		chairs[y    ][x + 1]--;
		chairs[y + 1][x + 1]--;
	}
	// skip student
	rec(x, y + 1, s);
}

int solve() {
	fscanf(stdin, "%d %d\n", &M, &N);
	
	memset(chairs, 0, sizeof(chairs));
	for (int y = 1; y <= M; y++) {
		char line[83];
		fscanf(stdin, "%s\n", &line);
		for (int x = 1; x <= N; x++) {
			chairs[y][x] = int(line[x - 1] == 'x');
		}
	}

	best = 0;
	
	rec(1, 1, 0);

	return best;
}

int main() {
	int c;
	fscanf(stdin, "%d\n", &c);
	for (int i = 1; i <= c; i++) {
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}
