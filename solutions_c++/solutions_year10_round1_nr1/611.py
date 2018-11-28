#include <cstdio>

using namespace std;

void rotate(char A[55][55], int N)
{
	char B[55][55];
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			B[j][N-1-i] = A[i][j];
		}
	}
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			A[i][j] = B[i][j];
		}
	}
	
	// fall
	for (int j = 0; j < N; ++j) {
		for (int i = N - 1; i >= 0; --i) {
			if (A[i][j] != '.') {
				int k;
				for (k = i + 1; k< N; ++k) {
					if (A[k][j] != '.') {
						break;
					}
				}
				--k;
				if (k == i) continue;
				A[k][j] = A[i][j];
				A[i][j] = '.';
			}
		}
	}
//		for(int i=0;i<N;++i){
//			for(int j=0;j<N;++j)
//				putchar(A[i][j]);
//			putchar('\n');
//		}
}

bool connect(char A[55][55], int N, int K, char cur)
{
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			if (A[i][j] == cur && i + K -1 < N) {
				int k;
				for (k = 1; k < K; ++k) {
					if (A[i+k][j] != cur) break;
				}
				if (k == K) return true;
			}
			if (A[i][j] == cur && j + K -1 < N) {
				int k;
				for (k = 1; k < K; ++k) {
					if (A[i][j+k] != cur) break;
				}
				if (k == K) return true;
			}
			if (A[i][j] == cur && j + K -1 < N && i + K -1 < N) {
				int k;
				for (k = 1; k < K; ++k) {
					if (A[i+k][j+k] != cur) break;
				}
				if (k == K) return true;
			}
			if (A[i][j] == cur && j - K +1 < N && i + K -1 < N) {
				int k;
				for (k = 1; k < K; ++k) {
					if (A[i+k][j-k] != cur) break;
				}
				if (k == K) return true;
			}
		}
	}
	return false;
}

int main()
{
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int cas,re;
	scanf("%d", &cas);
	for (re = 1; re <= cas; ++re) {
		int N;
		int K;
		scanf("%d%d", &N, &K);
		char A[55][55];
		char s[128];
		gets(s);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				A[i][j] = getchar();
			}
			gets(s);
		}
		rotate(A, N);
		
	
		
		bool redWin = connect(A, N, K, 'R');
		bool blueWin = connect(A, N, K, 'B');
		printf("Case #%d: ", re);
		if (redWin && blueWin) {
			printf("Both\n");
		}
		else if (redWin) {
			printf("Red\n");	
		}
		else if (blueWin) {
			printf("Blue\n");
		}
		else {
			printf("Neither\n");
		}
	}
}
