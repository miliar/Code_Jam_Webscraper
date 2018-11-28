#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main() {
	int move[4][2] = {{0,1}, {1,0}, {1,1}, {1,-1}};
	char state[4][5];
	int cases, cn=0;
	scanf("%d", &cases);
	while(cases--) {
		for (int i=0; i < 4; ++i) scanf("%s",state[i]);
		bool A = false;
		bool B = false;
		bool F = true;
		for (int i=0; i < 4; ++i) {
			for (int j=0; j < 4; ++j) {
				if (state[i][j] == '.') F = false;
				for (int d = (i==0) ? 3 : 1; d >= 0; --d) {
					int ii = i, jj = j, a = 0, b = 0;
					for (int k = 0; k < 4; ++k) {
						if (state[ii][jj] == 'X') ++a;
						else if (state[ii][jj] == 'O') ++b;
						else if (state[ii][jj] == 'T') { ++a; ++b; }
						ii += move[d][0];
						jj += move[d][1];
						if (min(ii,jj) < 0 || max(ii,jj) > 3) break;
					}
					if (a == 4) A = true;
					if (b == 4) B = true;
				}
			}
		}
		printf("Case #%d: ", ++cn);
		if (A) printf("X won\n");
		else if (B) printf("O won\n");
		else if (F) printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;
}