#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>

using namespace std;

char sheet[1000][1000];
long long DP[1000][1000];
long long DPii[1000][1000];
long long DPjj[1000][1000];

#define ODDWI(i, j, ii, jj) sheet[ii][jj] * ((ii) - (i))
#define EVENWI(i, j, ii, jj) sheet[ii][jj] * ((ii) - (i - 0.5))
#define ODDWJ(i, j, ii, jj) sheet[ii][jj] * ((jj) - (j))
#define EVENWJ(i, j, ii, jj) sheet[ii][jj] * ((jj) - (j - 0.5))

int main() {
	int T;
	int R, C, D;
	
	scanf("%d\n", &T);
	
	for(int nCase = 1; nCase <= T; nCase++) {
		scanf("%d %d %d\n", &R, &C, &D);
		
		memset(DP, 0, sizeof(DP));
		memset(DPii, 0, sizeof(DPii));
		memset(DPjj, 0, sizeof(DPjj));
		
		for(int i = 0; i < R; i++) {
			scanf("%s\n", sheet[i]);
			
			for(int j = 0; j < C; j++) {
				sheet[i][j] -= '0';
				
				DP[i+1][j+1] = sheet[i][j] + DP[i+1][j] + DP[i][j+1] - DP[i][j];
				DPii[i+1][j+1] = sheet[i][j] * i + DPii[i+1][j] + DPii[i][j+1] - DPii[i][j];
				DPjj[i+1][j+1] = sheet[i][j] * j + DPjj[i+1][j] + DPjj[i][j+1] - DPjj[i][j];
			}
		}
		
		int K = 2;
		
		for(K = min(R, C); K >= 3; K--) {
			for(int i = 0; i < R; i++) {
				for(int j = 0; j < C; j++) {
					int i0 = i-K/2, i1 = i-(K/2)+K-1;
					int j0 = j-K/2, j1 = j-(K/2)+K-1;
					
					if(i0 < 0 || j0 < 0 || i1 >= R || j1 >= C) continue;
					
					double bali;
					double balj;
					
					if(K&1) {
						bali = 
							(DPii[i1+1][j1+1] - DPii[i0][j1+1] - DPii[i1+1][j0] + DPii[i0][j0]) -
							(DP[i1+1][j1+1] - DP[i0][j1+1] - DP[i1+1][j0] + DP[i0][j0]) * i;
						bali -= ODDWI(i, j, i0, j0);
						bali -= ODDWI(i, j, i0+K-1, j0);
						bali -= ODDWI(i, j, i0, j0+K-1);
						bali -= ODDWI(i, j, i0+K-1, j0+K-1);
						
						balj = 
							(DPjj[i1+1][j1+1] - DPjj[i0][j1+1] - DPjj[i1+1][j0] + DPjj[i0][j0]) -
							(DP[i1+1][j1+1] - DP[i0][j1+1] - DP[i1+1][j0] + DP[i0][j0]) * j;
						balj -= ODDWJ(i, j, i0, j0);
						balj -= ODDWJ(i, j, i0+K-1, j0);
						balj -= ODDWJ(i, j, i0, j0+K-1);
						balj -= ODDWJ(i, j, i0+K-1, j0+K-1);
					} else {
						bali = 
							(DPii[i1+1][j1+1] - DPii[i0][j1+1] - DPii[i1+1][j0] + DPii[i0][j0]) -
							(DP[i1+1][j1+1] - DP[i0][j1+1] - DP[i1+1][j0] + DP[i0][j0]) * (i-0.5);
						bali -= EVENWI(i, j, i0, j0);
						bali -= EVENWI(i, j, i1, j0);
						bali -= EVENWI(i, j, i0, j1);
						bali -= EVENWI(i, j, i1, j1);
						
						balj = 
							(DPjj[i1+1][j1+1] - DPjj[i0][j1+1] - DPjj[i1+1][j0] + DPjj[i0][j0]) -
							(DP[i1+1][j1+1] - DP[i0][j1+1] - DP[i1+1][j0] + DP[i0][j0]) * (j-0.5);
						balj -= EVENWJ(i, j, i0, j0);
						balj -= EVENWJ(i, j, i1, j0);
						balj -= EVENWJ(i, j, i0, j1);
						balj -= EVENWJ(i, j, i1, j1);
					}
					
					if(fabs(bali) < 1e-6 && fabs(balj) < 1e-6) {
						goto end;
					}
				}
			}
		}
		
		end:
		if(K == 2) {
			printf("Case #%d: IMPOSSIBLE\n", nCase);
		} else {
			printf("Case #%d: %d\n", nCase, K);
		}
	}
}
