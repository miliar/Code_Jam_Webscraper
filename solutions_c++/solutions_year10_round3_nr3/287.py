#include <cstdio>
#include <algorithm>
#define MAXN 512
using namespace std;

const int mx[] = {-1, -1, 0};
const int my[] = {-1,  0,-1};

char hex_conv[255];

int T, M, N;
char buf[MAXN/4 + 1];
bool white[MAXN][MAXN];
int D[MAXN][MAXN];
int cnt[MAXN+1];

int main() {
	hex_conv[int('0')] = 0;
	hex_conv[int('1')] = 1;
	hex_conv[int('2')] = 2;
	hex_conv[int('3')] = 3;
	hex_conv[int('4')] = 4;
	hex_conv[int('5')] = 5;
	hex_conv[int('6')] = 6;
	hex_conv[int('7')] = 7;
	hex_conv[int('8')] = 8;
	hex_conv[int('9')] = 9;
	hex_conv[int('A')] = 10;
	hex_conv[int('B')] = 11;
	hex_conv[int('C')] = 12;
	hex_conv[int('D')] = 13;
	hex_conv[int('E')] = 14;
	hex_conv[int('F')] = 15;

	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		fill(&white[0][0], &white[MAXN][0], false);
		fill(&D[0][0], &D[MAXN][0], 0);
		fill(&cnt[0], &cnt[MAXN+1], 0);

		scanf("%d %d ", &M, &N);
		for(int j = 0; j < M; j++) {
			scanf("%s ", &buf[0]);
			for(int k = 0; k < N/4; k++) {
				int hex = hex_conv[int(buf[k])];
				for(int l = 3; l >= 0; l--) {
					white[j][k*4+l] = hex%2;
					hex /= 2;
				}
			}
		}

		for(int r = 0; r < M; r++) {
			D[r][0] = 1;
		}
		for(int c = 0; c < N; c++) {
			D[0][c] = 1;
		}

		for(int its = 0; true; its++) {
			int nr, nc, mini;
			for(int r = 1; r < M; r++) {
				for(int c = 1; c < N; c++) {
					if(its && !D[r][c]) {
						continue;
					}

					mini = 1000;
					for(int k = 0; k < 3; k++) {
						nr = r + mx[k];
						nc = c + my[k];
						mini = min(mini, D[nr][nc]);
					}
					if(white[r][c] == white[r-1][c-1] &&
							white[r][c] != white[r-1][c] &&
							white[r-1][c] == white[r][c-1]) {
						D[r][c] = mini + 1;
					} else {
						D[r][c] = 1;
					}
				}
			}

			int maxi = 0, mr, mc;
			for(int r = 0; r < M; r++) {
				for(int c = 0; c < N; c++) {
					if(D[r][c] > maxi) {
						maxi = D[r][c];
						mr = r;
						mc = c;
					}
				}
			}

			if(maxi) {
				cnt[maxi]++;
				for(int r = mr - maxi + 1; r <= mr; r++) {
					for(int c = mc - maxi + 1; c <= mc; c++) {
						D[r][c] = 0;
					}
				}
			} else {
				break;
			}
		}

		int different = 0;
		for(int j = MAXN; j > 0; j--) {
			if(cnt[j]) {
				different++;
			}
		}

		printf("Case #%d: %d\n", i+1, different);
		for(int j = MAXN; j > 0; j--) {
			if(cnt[j]) {
				printf("%d %d\n", j, cnt[j]);
			}
		}

		/*for(int j = 0; j < M; j++) {
			for(int k = 0; k < N; k++) {
				//fprintf(stderr, "%c", white[j][k] ? '.' : '#');
				fprintf(stderr, "%d", D[j][k]);
			}
			fprintf(stderr, "\n");
		}*/
	}
	return 0;
}
