
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>

using namespace std;

#define NN 1000
char m[NN][NN];

int main() {
	int T;
	scanf("%d ", &T);
	for (int ct = 1; ct <= T; ct++) {
		int n, M; scanf("%d%d ", &n, &M);
		memset(m, 0, sizeof m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < M; j++)
				scanf(" %c", &m[i][j]);

		bool imp = false;

		for (int i = 0; i < n && !imp; i++)
			for (int j = 0; j < M; j++)
				if (m[i][j] == '#') {
					if (m[i+1][j] == '#' && m[i][j+1] == '#' && m[i+1][j+1] == '#') {
						m[i][j] = '/'; m[i+1][j] = '\\'; m[i][j+1] = '\\'; m[i+1][j+1] = '/'; 
					} else  {
						imp = true; break;
					}
				}
		printf("Case #%d:\n", ct);
		if (imp) printf("Impossible\n");
		else {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < M; j++)
					printf("%c", m[i][j]);
				printf("\n");
			}
		}
	}
	return 0;
}
