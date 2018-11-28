#include <cstdio>
#include <cstring>

const int MAXN = 110 * 110;
const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

struct DSet{

	int n, father[MAXN], tot;
	char ret[MAXN];
	
	void init(int m) {
		n = m;
		for (int i = 0; i < n; i++) father[i] = i, ret[i] = '.';
		tot = 0;
	}
	
	int getFather(int x) {
		int tx = x;
		while (father[x] != x) x = father[x];
		while (father[tx] != x) {
			int t = father[tx];
			father[tx] = x;
			tx = t;
		}
		return x;
	}

	int isFreind(int x, int y) {
		x = getFather(x), y = getFather(y);
		return x == y;
	}
	
	void setFriend(int x, int y) {
		x = getFather(x), y = getFather(y);
		father[x] = y;
	}
	
	char query(int x) {
		x = getFather(x);
		if (ret[x] == '.') {
			ret[x] = tot + 'a';
			tot++;
		}
		return ret[x];
	}

}ds;

int h[110][110];

void solve() {

	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) 
			scanf("%d", &h[i][j]);
	ds.init(n * m);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) {
			int curx = -1, cury = -1;
			for (int k = 0; k < 4; k++) {
				int x = i + dx[k], y = j + dy[k];
				if (x < 0 || x >= n || y < 0 || y >= m) continue;
				if (h[x][y] < h[i][j]) {
					if (curx == -1 || h[x][y] < h[curx][cury]) 
						curx = x, cury = y;
				}
			}
			if (curx != -1) {
				ds.setFriend(i * m + j, curx * m + cury);	
			}		
		}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m - 1; j++) {
			printf("%c ", ds.query(i * m + j));
		}
		printf("%c\n", ds.query(i * m + m - 1));
	}
}

int main() {

	int test;
	scanf("%d", &test);
	for (int i = 1; i <= test; i++) {
		printf("Case #%d:\n", i);
		solve();
	}
	return 0;
}

