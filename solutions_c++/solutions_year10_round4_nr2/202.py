#include <iostream>

using namespace std;

long long A[12][600][12];
long long M[1100];
long long MIN[12][600];
long long C[12][600];

int main() {
	freopen("b-large.in", "r", stdin);
	freopen("b-large-out.txt", "w", stdout);
	long long tt, ttt, p, i, j, k;
	cin >> tt;
	for (ttt = 1; ttt <= tt; ttt++) {
		memset(A, 0, sizeof(A));
		cin >> p;
		for(i = 0; i < (1 << p); i++)
			cin >> M[i];
		for(i = 0; i < p; i++) {
			for(j = 0; j < (1 << (p - 1 - i)); j++) {
				cin >> C[i][j];
				if (i == 0)
					MIN[i][j] = min(M[j * 2], M[j * 2 + 1]);
				else {
					MIN[i][j] = min(MIN[i - 1][j * 2], MIN[i - 1][j * 2 + 1]);
				}
				for(k = 0; k <= MIN[i][j]; k++) {
					if (i > 0) {
						A[i][j][k] = C[i][j] + A[i-1][j*2][k] + A[i-1][j*2+1][k];
						if (k < MIN[i][j]) {
							A[i][j][k] = min(A[i][j][k],
								A[i-1][j*2][k+1] + A[i-1][j*2+1][k+1]);
						}
					} else {
						if (k == MIN[i][j])
							A[i][j][k] += C[i][j];
					}
//					cout << i << " " << j << " " << k << " " << A[i][j][k] << endl;
				}
			}
		}
		cout << "Case #" << ttt << ": " << A[p-1][0][0] << endl;
	}
//	system("pause");
	return 0;
}
