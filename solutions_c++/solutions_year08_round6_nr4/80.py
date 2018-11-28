
#include <stdio.h>

int prob, nprob;
int N, M;
int gl[10][10], gs[10][10];
int used[10], lst[10];
int idx[10];


int search(int lev) {
	if (lev == M) {
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < M; j++) {
				if (gs[i][j] != gl[lst[i]][lst[j]])
					return 0;
			}
		}

		return 1;
	}

	for (int i = 0; i < N; i++)
		if (!used[i]) {
			used[i] = 1;
			lst[lev] = i;

			if (search(lev+1)) return 1;

			used[i] = 0;
		}

	return 0;
}

int main() {
	freopen("d.in", "r", stdin);
//	freopen("d.out", "w", stdout);

	scanf("%d", &nprob);
	for (prob = 1; prob <= nprob; prob++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				gl[i][j] = 0;

		for (int i = 1; i < N; i++) {
			int a, b; scanf("%d%d", &a, &b); a--; b--;
			gl[a][b] = gl[b][a] = 1;
		}

		scanf("%d", &M);
		for (int i = 0; i < M; i++)
			for (int j = 0; j < M; j++)
				gs[i][j] = 0;

		for (int i = 1; i < M; i++) {
			int a, b; scanf("%d%d", &a, &b); a-- ;b--;
			gs[a][b] = gs[b][a] = 1;
		}

		for (int i = 0; i < N; i++) used[i] = 0;
		printf("Case #%d: ", prob);
		if (search(0))
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}
