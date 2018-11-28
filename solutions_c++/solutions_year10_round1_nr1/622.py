#include <cstdio>
#include <algorithm>

#define rep(i,n) for (int i = 0; i < n; i++)

using namespace std;

char board[100][100];
char board2[100][100];
int N, K;

bool wins(char c) {
	int maxv = -1;
	
	rep(i,N) {
		int count = 0;
		rep(j,N) {
			if (board2[i][j] == c) count++;
			else {
				maxv = max(maxv, count);
				count = 0;
			}
		}

		maxv = max(maxv,count);
	}

	rep(j,N) {
		int count = 0;
		rep(i,N) {
			if (board2[i][j] == c) count++;
			else {
				maxv = max(maxv, count);
				count = 0;
			}
		}

		maxv = max(maxv,count);
	}
	
	rep(i,N) {
		int count = 0;
		int ii = i;
		int jj = 0;
		
		while (ii >= 0 && jj >= 0 && ii < N && jj < N) {
			if (board2[ii][jj] == c) count++;
			else {
				maxv = max(maxv, count);
				count = 0;
			}

			ii++; jj++;
		}

		maxv = max(maxv, count);
		
		count = 0;
		ii = i;
		jj = 0;
		
		while (ii >= 0 && jj >= 0 && ii < N && jj < N) {
			if (board2[ii][jj] == c) count++;
			else {
				maxv = max(maxv, count);
				count = 0;
			}

			ii--; jj++;
		}

		maxv = max(maxv, count);


		ii = i;
		jj = N-1;
		count = 0;
		
		while (ii >= 0 && jj >= 0 && ii < N && jj < N) {
			if (board2[ii][jj] == c) count++;
			else {
				maxv = max(maxv, count);
				count = 0;
			}

			ii++; jj--;
		}

		maxv = max(maxv, count);

		ii = i;
		jj = N-1;
		count = 0;
		
		while (ii >= 0 && jj >= 0 && ii < N && jj < N) {
			if (board2[ii][jj] == c) count++;
			else {
				maxv = max(maxv, count);
				count = 0;
			}

			ii--; jj--;
		}

		maxv = max(maxv, count);

	}
	
	if (maxv >= K) return true;
	else return false;
}

int main() {
	int T;
	scanf("%d", &T);

	rep(t,T) {
		scanf("%d %d", &N, &K);

		rep(i,N) {
			scanf("%s", board[i]);
		}
		
		rep(i,N) {
			rep(j,N) {
				board2[j][N-i-1] = board[i][j];
			}
		}
	
		rep(j,N) {
			int currfree = -1;

			for (int i = N-1; i >= 0; i--) {
				if (board2[i][j] == '.' && currfree == -1) currfree = i;
				else if (board2[i][j] != '.' && currfree != -1) {
					board2[currfree][j] = board2[i][j];
					board2[i][j] = '.';
					currfree--;
				}
			}
		}

		bool winsB = wins('B');
		bool winsR = wins('R');
		
		printf("Case #%d: ", t+1);
		if (!winsB && !winsR) printf("Neither\n");
		else if (winsB && !winsR) printf("Blue\n");
		else if (winsR && !winsB) printf("Red\n");
		else printf("Both\n");
	}

	return 0;
}

