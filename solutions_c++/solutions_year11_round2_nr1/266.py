#include <iostream>
#include <iomanip>
using namespace std;

char board[110][110];
double wp[110];
double owp[110];
double oowp[110];
int n;

void solve(int case_index) {
	scanf("%d", &n);
	for (int i = 0; i < n; i ++)
		scanf("%s", board[i]);
	for (int i = 0; i < n; i ++) {
		int cnt = 0, tot = 0;
		for (int j = 0; j < n; j ++)
			if (board[i][j] != '.') {
				tot ++;
				if (board[i][j] == '1')
					cnt ++;
			}
			wp[i] = (double)cnt / (double)tot;
	}
	for (int i = 0; i < n; i ++) {
		int op = 0;
		owp[i] = 0.0;
		for (int j = 0; j < n; j ++)
			if (board[i][j] != '.') {
				op ++;
				int cnt = 0, tot = 0;
				for (int k = 0; k < n; k ++)
					if (k != i && board[j][k] != '.') {
						tot ++;
						if (board[j][k] == '1')
							cnt ++;
					}
				owp[i] += (double)cnt / (double) tot;
			}
		owp[i] /= (double) op;
	}
	for (int i = 0; i < n; i ++) {
		int op = 0;
		oowp[i] = 0.0;
		for (int j = 0; j < n; j ++) {
			if (board[i][j] != '.') {
				op ++;
				oowp[i] += owp[j];
			}
		}
		oowp[i] /= (double) op;
	}
	cout << "Case #" << case_index << ":" << endl;
	for (int i = 0; i < n; i ++) {
		cout << wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25 << endl;
	}
}

int main() {
	cout << fixed << setprecision(12) ;
	int case_count;
	scanf("%d", &case_count);
	for (int i = 1; i <= case_count; i ++)
		solve(i);
	return 0;
}