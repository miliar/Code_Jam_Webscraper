#include <cstdio>
#include <cstdlib>
#include <string>
#include <map>
#include <set>
#include <sstream>
using namespace std;
#define PI 3.14159265358979323846264338327950288
int T, Na, Nb;
int C;
int all[2][105][2];
int mark[2][105];
int getTime(int *x) {
	int i, j;
	scanf("%d:%d", &i, &j);
	(*x) = i * 60 + j;
	return 0;
}
int main() {
	int Case = 1, i, j;
	scanf("%d", &C);
	while (C --) {
		scanf("%d", &T);
		scanf("%d%d", &Na, &Nb);
		for (i = 0; i < Na; i ++) {
			getTime(&all[0][i][0]);
			getTime(&all[0][i][1]);
		}
		for (i = 0; i < Nb; i ++) {
			getTime(&all[1][i][0]);
			getTime(&all[1][i][1]);
		}
		memset(mark, 0, sizeof(mark));
		int reta = Na, retb = Nb;
		for (i = 0; i < Na; i ++) {
			int least = -1, id;
			for (j = 0; j < Nb; j ++)
				if (all[1][j][1] + T <= all[0][i][0] && !mark[1][j])
					if (least < all[1][j][1]) {
						least = all[1][j][1];
						id = j;
					}
			if (least != -1) {
				reta --;
				mark[1][id] = 1;
			}
		}
		for (i = 0; i < Nb; i ++) {
			int least = -1, id;
			for (j = 0; j < Na; j ++)
				if (all[0][j][1] + T <= all[1][i][0] && !mark[0][j])
					if (least < all[0][j][1]) {
						least = all[0][j][1];
						id = j;
					}
			if (least != -1) {
				retb --;
				mark[0][id] = 1;
			}
		}
		printf("Case #%d: %d %d\n", Case ++, reta, retb);
	}
	return 0;
}

