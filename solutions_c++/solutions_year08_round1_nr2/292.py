#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <memory.h>

const int MAXN = 3010;

int N = 0;
int M = 0;
int c[MAXN] = {0};
int a[MAXN][MAXN][2] = {{0}};
int res[MAXN] = {0};

bool checkPerson(int i) {
	for (int j = 0; j < c[i]; ++j) {
		if (res[a[i][j][1] - 1] == a[i][j][2]) {return true;}
	}
	return false;
}

bool checkRes() {
	for (int i = 0; i < M; ++i) {
		if (!checkPerson(i)) {return false;}
	}
	return true;
}

int genRes(int i) {
	memset(res, 0, sizeof(res));
	int j = 0;
	while (i) {
		res[j++] = i % 2;
		i /= 2;
	}

	int rank = 0;
	for (int k = 0; k < N; ++k) {
		rank += res[k];
	}
	return rank;
}

void solve() {
	int best = 0;
	int rank = 100;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < M; ++i) {
		scanf("%d", c + i);
		for (int j = 0; j < c[i]; ++j) {
			scanf("%d %d", &a[i][j][1], &a[i][j][2]);
		}
	}

	int HI = (1 << (N + 1));
	bool f = false;
	for (int i = 0; i < HI; ++i) {
		int r = genRes(i);
		if (checkRes()) {
			f = true;
			if (r < rank) {
				best = i;
				rank = r;
			}
		}
	}
	if (f) {
		genRes(best);
		for (int j = 0; j < N; ++j) {
			printf("%d ", res[j]);
		}
	} else {printf("IMPOSSIBLE");}
	puts("");
}

int main(void) {
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);

	int T = 0;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
