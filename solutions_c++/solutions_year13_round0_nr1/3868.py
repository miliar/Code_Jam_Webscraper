#include<cstdio>

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 0; t<T; ++t) {
		int c[4][4];
		int poc = 0;
		for (int i = 0; i<4; ++i) {
			for (int j = 0; j<4; ++j) {
				char x;
				scanf(" %c", &x);
				if (x == 'X') c[i][j] = 1;
				else if (x == 'O') c[i][j] = -1;
				else if (x == '.') {c[i][j] = 0; ++poc; }
				else c[i][j] = 42;
			}
		}
		bool b = true;
		for (int i = 0; i<4; ++i) {
			int suc = 0;
			int sur = 0;
			for (int j = 0; j<4; ++j) {
				suc+=c[i][j];
				sur+=c[j][i];
			}
			if (suc == -4 || suc == 39) {
				printf("Case #%d: O won\n", t+1);
				b = false;
			} else if (suc == 4 || suc == 45) {
				printf("Case #%d: X won\n", t+1);
				b = false;
			} else if (sur == -4 || sur == 39) {
				printf("Case #%d: O won\n", t+1);
				b = false;
			} else if (sur == 4 || sur == 45) {
				printf("Case #%d: X won\n", t+1);
				b = false;
			}
			if (!b) break;
		}
		if (b) {
			int suc = c[0][0] + c[1][1] + c[2][2] + c[3][3];
			int sur = c[0][3] + c[1][2] + c[2][1] + c[3][0];
			if (suc == -4 || suc == 39) {
				printf("Case #%d: O won\n", t+1);
				b = false;
			} else if (suc == 4 || suc == 45) {
				printf("Case #%d: X won\n", t+1);
				b = false;
			} else if (sur == -4 || sur == 39) {
				printf("Case #%d: O won\n", t+1);
				b = false;
			} else if (sur == 4 || sur == 45) {
				printf("Case #%d: X won\n", t+1);
				b = false;
			}
		}
		if (b && poc != 0) printf("Case #%d: Game has not completed\n", t+1);
		else if (b) printf("Case #%d: Draw\n", t+1);
	}
	return 0;
}
