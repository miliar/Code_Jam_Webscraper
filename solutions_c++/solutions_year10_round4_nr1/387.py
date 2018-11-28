#include <iostream>
#define MAXN 128
#define INF 1000000000
using namespace std;
int dia[MAXN][MAXN];
int k;
bool isOK(int i, int j) {
	for(int ii = 0; ii < 2 * k - 1; ++ii) {
		for(int jj = 0; jj < 2 * k - 1; ++jj) {
			if(dia[ii][jj] == -1)
				continue;
			int x = 2 * i - ii;
			int y = 2 * j - jj;
			if(x >= 0 && x < 2 * k - 1 && dia[x][jj] != -1) {
				if(dia[ii][jj] != dia[x][jj])
					return false;
			}
			if(y >= 0 && y < 2 * k - 1 && dia[ii][y] != -1) {
				if(dia[ii][jj] != dia[ii][y])
					return false;
			}
			if(x >= 0 && x < 2 * k - 1 && y >= 0 && y < 2 * k - 1 && dia[x][y] != -1) {
				if(dia[ii][jj] != dia[x][y])
					return false;
			}
		}
	}
	return true;
}
int getSize(int i, int j) {
	int dx = abs(i - k + 1);
	int dy = abs(j - k + 1);
	return k + dx + dy;
}
int main() {
	int T, cs = 1;
	scanf("%d", &T);
	while(T--){
		scanf("%d", &k);
		memset(dia, -1, sizeof(dia));
		for(int i = 0; i < k; ++i) {
			for(int j = 0; j < i + 1; ++j) {
				scanf("%d", &dia[i][k - i - 1 + 2 * j]);
			}
		}
		for(int i = k - 2; i >= 0; --i) {
			for(int j = 0; j < i + 1; ++j) {
				scanf("%d", &dia[2 * k - 2 - i][k - i - 1 + 2 * j]);
			}
		}
		int mink = INF;
		for(int i = 0; i < 2 * k - 1; ++i)
			for(int j = 0; j < 2 * k - 1; ++j) {
				if(isOK(i, j) && getSize(i, j) < mink)
					mink = getSize(i, j);
			}
		//printf("%d\n", mink);
		printf("Case #%d: %d\n", cs, mink * mink - k * k);
		++cs;
	}
	return 0;
}
