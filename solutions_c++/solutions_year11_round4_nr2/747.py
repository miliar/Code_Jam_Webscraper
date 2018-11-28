#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;
const int MAXN = 12;
int data[MAXN][MAXN];
bool check(int x, int y, int k, int d){
	//cout << "===" << x << " " << y << " " << k << endl;
	double cx = 0, cy = 0;
	int t = 0;
	for (int i = x; i < x + k; ++i){
		for (int j = y; j < y + k; ++j){
			if (i == x && j == y || i == x + k -1 && j == y ||
				i == x && j == y + k - 1 || i == x + k - 1 && j == y + k - 1) continue;
		//	cout << i << " " << j << endl;
			cx += (i + 0.5) * (d + data[i][j]);
			cy += (j + 0.5) * (d + data[i][j]);
			t += d + data[i][j];
		}
	}
	cx /= t; cy /= t;
	//cout << cx << " " << cy << " " << t <<  endl;
	return (fabs(cx - x - k / 2.0) < 1e-6 && fabs(cy - y - k / 2.0) < 1e-6);
}
int main(){
	int cases;
	scanf("%d", &cases);
	for (int tt = 0; tt < cases; ++tt){
		int r, c, d;
		memset(data, 0, sizeof(data));
		scanf("%d%d%d", &r, &c, &d);
		getchar();
		for (int i = 0; i < r; ++i){
			for (int j = 0; j < c; ++j){
				char ch = getchar();
				data[i][j] = ch - '0';
			}
			getchar();
		}
		int res = 2;
		for (int i = 0; i < r; ++i){
			for (int j = 0; j < c; ++j){
				for (int k = res + 1; k <= min(r, c); ++k){
					if (i + k <= r && j + k <= c && check(i, j, k, d) && k > res){
						res = k;
					}
				}
			}
		}
		printf("Case #%d: ", tt + 1);
		if (res >= 3){
			printf("%d\n", res);
		} else {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}