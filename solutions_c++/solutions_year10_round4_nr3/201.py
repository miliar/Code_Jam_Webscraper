#include <iostream>

using namespace std;

int A[110][110];// small
int B[110][110];// small
int X1[1100], X2[1100], Y1[1100], Y2[1100];

int main() {
	freopen("c-small.in", "r", stdin);
	freopen("c-small-out.txt", "w", stdout);
	int tt, ttt, i, R, j, k, t;
	bool done;
	scanf("%d", &tt);
	for(ttt = 1; ttt <= tt; ttt++) {
		scanf("%d", &R);
		for(i = 0; i < R; i++) {
			scanf("%d%d%d%d", &Y1[i], &X1[i], &Y2[i], &X2[i]);
			X1[i]--; X2[i]--; Y1[i]--; Y2[i]--;
		}
		memset(A, 0, sizeof(A));
		done = true;
		for(i = 0; i < R; i++) {
			for(j = X1[i]; j <= X2[i]; j++)
			for(k = Y1[i]; k <= Y2[i]; k++) {
				A[j][k] = 1;
				done = false;
			}
		}
		t = 0;
		while (done == false) {
			done = true;
			for(i = 0; i <= 100; i++)
			for(j = 0; j <= 100; j++) {
				B[i][j] = A[i][j];
				if (A[i][j] == 0) {
					if (i > 0 && j > 0 && A[i-1][j] == 1 && A[i][j-1] == 1)
						B[i][j] = 1;
				} else {
					if ((i == 0 || A[i-1][j] == 0) && (j == 0 || A[i][j-1] == 0))
						B[i][j] = 0;
				}
				if (B[i][j] == 1)
					done = false;
			}
			for(i = 0; i <= 100; i++)
			for(j = 0; j <= 100; j++)
				A[i][j] = B[i][j];
			t++;
		}
		printf("Case #%d: %d\n", ttt, t);
	}
//	system("pause");
	return 0;
}
