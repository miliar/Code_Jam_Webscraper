#include <cstring>
#include <iostream>
const int MAXN = 310;
using namespace std;
#define _clr(x) memset(x, 0xff, sizeof(int) * MAXN)
int price[MAXN][30];
bool mat[MAXN][MAXN];

int hungary(int m, int n, const bool mat[][MAXN]) {
	int s[MAXN + 1], t[MAXN], p, q, ret = 0, i, j, k, match1[MAXN], match2[MAXN];
	_clr(match1);
	_clr(match2);
	for (i = 0; i < m; ret += (match1[i++] >= 0)) {
		_clr(t);
		for (s[p = q = 0] = i; p <= q && match1[i] < 0; p++) {
			k = s[p];
			for (j = 0; j < n && match1[i] < 0; j++) {
				if (mat[k][j] && t[j] < 0) {
					s[++q] = match2[j];
					t[j] = k;
					if (s[q] < 0) {
						for (p = j; p >= 0; j = p) {
							match2[j] = k = t[j];
							p = match1[k];
							match1[k] = j;
						}
					}
				}
			}
		}
	}
	return ret;
}
int n, k;
inline bool check(int x, int y){
	for (int i = 0; i < k; ++i){
		if (price[x][i] >= price[y][i]) return false;
	}
	return true;
}
int main(){
	int cases;
	cin >> cases;
	for (int tt = 0; tt < cases; ++tt){
		
		cin >> n >> k;
		for (int i = 0; i < n; ++i){
			for (int j = 0; j < k; ++j){
				cin >> price[i][j];
			}
		}
		memset(mat, 0, sizeof(mat));
		for (int i = 0; i < n; ++i){
			for (int j = 0; j < n; ++j){
				if (check(i, j)){
	//				cout << "sdf" << endl;
					mat[i][j] = true;
				} else mat[i][j] = false;
			}
		}
		printf("Case #%d: %d\n", tt + 1, n - hungary(n, n, mat));
	}
	return 0;
}