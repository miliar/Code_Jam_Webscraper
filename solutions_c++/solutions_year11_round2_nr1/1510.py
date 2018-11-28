#include <cstdio>
#include <cstring>
using namespace std;

int cases, n;
char board[105][105];
double wp[105], owp[105], oowp[105];
int win[105], total[105];

int main() {
	scanf("%d", &cases);
	for (int test = 0; test < cases; test++) {
		scanf("%d", &n);
		getchar();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++)
				scanf("%c", &board[i][j]);
			getchar();
		}

		memset(win, 0, sizeof(win));
		memset(total, 0, sizeof(total));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (board[i][j] != '.')
					++total[i];
				if (board[i][j] == '1')
					++win[i];
			}
			wp[i] = (double)win[i] / (double)total[i];
			//printf("wp[%d]=%lf\n", i, wp[i]);
		}

		for (int i = 0; i < n; i++) { // for a team
			int twin[105], ttotal[105];
			memcpy(twin, win, sizeof(win));
			memcpy(ttotal, total, sizeof(total));
			double temp = 0.0;
			int count = 0;
			for (int j = 0; j < n; j++) {
				if (board[i][j] != '.') { // an oppo
					++count;
					if (board[j][i] == '1')
						--twin[j];
					--ttotal[j];
					temp += (double)twin[j] / (double)ttotal[j];
				}
			}
			//printf("for %d: wintemp=%f  totaltemp=%f\n", i, wintemp, totaltemp);
			owp[i] = temp / (double)count;
		}

		for (int i = 0; i < n; i++) { // for a team
			double count = 0.0;
			int times = 0;
			for (int j = 0; j < n; j++) {
				if (board[i][j] != '.') { // an oppo
					++times;
					count += owp[j];
				}
			}
			oowp[i] = count / (double)times;
			//printf("oowp[%d]=%lf\n", i, oowp[i]);
		}

		printf("Case #%d:\n", test + 1);
		for (int i = 0; i < n; i++)
			printf("%.12g\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
	}
	return 0;
}
