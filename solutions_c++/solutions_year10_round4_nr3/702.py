#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN = 110;
bool f[MAXN][MAXN], g[MAXN][MAXN];
bool inrange(int x, int y){
	return x >= 0 && y >= 0 && x < MAXN && y < MAXN;
}

void show(){
	for (int i = 0; i < 5; ++i){
		for (int j = 0; j < 5; ++j){
			cout << f[i][j];
		}
		cout << endl;
	}
	getchar(); getchar();
}
int main(){
	int cases;
	cin >> cases;
	for (int tt = 0; tt < cases; ++tt){
		int n;
		cin >> n;
		memset(f, 0, sizeof(f));
		memset(g, 0, sizeof(g));
		for (int i = 0; i < n; ++i){
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			--x1; --y1; --x2; --y2;
			swap(x1, y1); swap(x2, y2);
			for (int i = x1; i <= x2; ++i){
				for (int j = y1; j <= y2; ++j){
					f[i][j] = true;
				}
			}
		}
		int ans = 0;
		memcpy(g, f, sizeof(g));
		while (true){
		//	show();
			++ans;
			bool in = false;
			for (int i = 0; i < MAXN; ++i){
				for (int j = 0; j < MAXN; ++j){
					if (f[i][j] && (!inrange(i - 1, j) || !f[i - 1][j]) && (!inrange(i, j - 1) || !f[i][j - 1])){
						g[i][j] = false;
					}
					if (!f[i][j] && inrange(i - 1, j) && f[i - 1][j] && inrange(i, j - 1) && f[i][j - 1]){
						g[i][j] = true;
					}
					in = in || g[i][j];
				}
			}
			memcpy(f, g, sizeof(f));
			if (!in) break;
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	return 0;
}