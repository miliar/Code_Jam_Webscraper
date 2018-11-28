#include <iostream>
#include <cstring>
using namespace std;
const int MAXN = 102;
int f[MAXN][MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN], num[MAXN];
int n;

double calcOWP(int x, int y){
	double ret = 0;
	for (int i = 0; i < n; ++i){
		if (f[x][i] == 1 && i != y) ++ret;
	}
	return ret / (num[x] - (f[x][y] != -1));
}
int main(){
	int cases;
	scanf("%d", &cases);
	for (int tt = 0; tt < cases; ++tt){
		scanf("%d", &n);
		memset(f, -1, sizeof(f));
		memset(num, 0, sizeof(num));
		for (int i = 0; i < n; ++i){
			getchar();
			for (int j = 0; j < n; ++j){
				char ch = getchar();
				if (ch == '1' || ch == '0'){
					f[i][j] = ch - '0';
					++num[i];
				}
			}
		}
		for (int i = 0; i < n; ++i){
			int cnt = 0;
			for (int j = 0; j < n; ++j){
				if (f[i][j] != -1 && f[i][j] == 1) ++cnt;
			}
			wp[i] = (double)cnt / num[i];
		}
		for (int i = 0; i < n; ++i){
			double cnt = 0;
			for (int j = 0; j < n; ++j){
				if (f[i][j] != -1){
					cnt += calcOWP(j, i);
				}
			}
			owp[i] = cnt / num[i];
		}
		for (int i = 0; i < n; ++i){
			double cnt = 0;
			for (int j = 0; j < n; ++j){
				if (f[i][j] != -1){
					cnt += owp[j];
				}
			}
			oowp[i] = cnt / num[i];
		}
		printf("Case #%d:\n", tt + 1);
		for (int i = 0; i < n;  ++i){
			printf("%.9lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}