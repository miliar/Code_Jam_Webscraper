#include <iostream>
#include <cstring>
#include <map>
using namespace std;
const int MAXN = 110;
const int offset[][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int data[MAXN][MAXN], m, n;
int used[MAXN][MAXN], total;
map<int, int> mm;
inline bool inrange(int x, int y){
	if (x >= 0 && y >= 0 && x < m && y < n) return true; else return false;
}
inline bool ismin(int x, int y, int dir){
	int d = -1;
	int maxv = data[x][y];
	for (int i = 0; i < 4; ++i){
		int tx = x + offset[i][0];
		int ty = y + offset[i][1];
		if (inrange(tx, ty) && data[tx][ty] < maxv){
			maxv = data[tx][ty];
			d = i;
		}
	}
	return d == 3 - dir;
}
void dfs(int x, int y){
	if (used[x][y] != -1) return;
	used[x][y] = total;
	for (int i = 0; i < 4; ++i){
		int tx = x + offset[i][0];
		int ty = y + offset[i][1];
		if (inrange(tx, ty) && ismin(tx, ty, i)){
			dfs(tx, ty);
		}
	}
}
bool findmin(int &x, int &y){
	int ret = 99999999, id = -1;
	for (int i = 0; i < m; ++i){
		for (int j = 0; j < n; ++j){
			if (used[i][j] == -1 && data[i][j] < ret){
				ret = data[i][j];
				x = i; y = j;
			}
		}
	}
	return ret != 99999999;
}
inline int getId(int i, int j){
	int id = -1;
	if (mm.find(used[i][j]) == mm.end()){
		int temp = mm.size();
		mm[used[i][j]] = temp;
		return temp;
	} else {
		return mm[used[i][j]];
	}
}
int main(){
	int cases;
	scanf("%d", &cases);
	for (int tt = 0; tt < cases; ++tt){
		mm.clear();
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; ++i){
			for (int j = 0; j < n; ++j){
				scanf("%d", &data[i][j]);
			}
		}
		memset(used, -1, sizeof(used));
		total = -1;
		int x, y;
		while (findmin(x, y)){
			++total;
			dfs(x, y);
		}
		printf("Case #%d:\n", tt + 1);
		for (int i = 0; i < m; ++i){
			for (int j = 0; j < n - 1; ++j){
				putchar(getId(i, j) + 'a');
				putchar(' ');
			}
			putchar(getId(i, n - 1) + 'a');
			putchar('\n');
		}
	}
	return 0;
}
