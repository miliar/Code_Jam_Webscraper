#include <cstdio>
#define MAXR 55

const int mr[] = {0, 1, 1, 0};
const int mc[] = {0, 0, 1, 1};
const char rt[] = {'/', '\\', '/', '\\'};

int T, R, C;
char t[MAXR][MAXR];
bool possible;

int main() {
	scanf("%d ", &T);
	for(int i = 0; i < T; i++) {
		scanf("%d %d ", &R, &C);
		for(int j = 0; j < R; j++) {
			scanf("%s ", &t[j][0]);
		}
		possible = true;
		for(int j = 0; j < R && possible; j++) {
			for(int k = 0; k < C; k++) {
				if(t[j][k] == '#') {
					for(int x = 0; x < 4 && possible; x++) {
						int nr = j + mr[x];
						int nc = k + mc[x];
						if(nr >= R || nc >= C || t[nr][nc] != '#') {
							possible = false;
						}
					}
					if(possible) {
						for(int x = 0; x < 4 && possible; x++) {
							int nr = j + mr[x];
							int nc = k + mc[x];
							t[nr][nc] = rt[x];
						}
					}
				}
			}
		}
		if(!possible) {
			printf("Case #%d:\nImpossible\n", i + 1);
		} else {
			printf("Case #%d:\n", i + 1);
			for(int j = 0; j < R; j++) {
				for(int k = 0; k < C; k++) {
					printf("%c", t[j][k]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}
