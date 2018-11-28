#include <cstdio>
#include <cstring>
#include <algorithm>

#define FOR(i, n) for(int i = 0; i < n; i++)

using namespace std;

char board[100][100];
char rboard[100][100];

int di[] = {-1, 0, 1, 1, 1, 0, -1, -1};
int dj[] = {1, 1, 1, 0, -1, -1, -1, 0};
const char *dw = "BR";

int main() {
	int T, N, K, win[2];
	
	scanf("%d\n", &T);
	
	for(int nCase = 1; nCase <= T; nCase++) {
		scanf("%d %d\n", &N, &K);
		
		FOR(i, N) {
			scanf("%s\n", board[i]);
		}
		
		win[0] = win[1] = 0;
		

		memset(rboard, '.', sizeof(rboard));
		FOR(i, N) {
			int k = N-1;
			for(int j = N-1; j >= 0; j--) {
				if(board[i][j] != '.') rboard[i][k--] = board[i][j];
			}
		}
		FOR(i, N) {
			FOR(j, N) {
				FOR(color, 2) {
					if(rboard[i][j] != dw[color]) continue;
				
					FOR(k, 8) {
						int cnt = 0;
						
						for(int pi = i, pj = j; cnt < K && pi >= 0 && pj >= 0 && pi < N && pj < N && rboard[pi][pj] == dw[color]; pi+= di[k], pj += dj[k]) {
							++cnt;
						}
					
						if(cnt == K) {
							win[color] = true;
						}
					}
				}
			}
		}
		
		if(!win[0] && !win[1])
			printf("Case #%d: Neither\n", nCase);
		else if(win[0] && !win[1])
			printf("Case #%d: Blue\n", nCase);
		else if(!win[0] && win[1])
			printf("Case #%d: Red\n", nCase);
		else if(win[0] && win[1])
			printf("Case #%d: Both\n", nCase);
	}
}
