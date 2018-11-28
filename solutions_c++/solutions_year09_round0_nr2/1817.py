#include <queue>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
int n, m;
int r, c;

const int N = 109;
int a[N][N];
char b[N][N];

void bfs(int x, int y) {
	queue<int>qx, qy;
	qx.push(x);
	qy.push(y);
	int col;
	while (!qx.empty()) {
		int tmpx = -1, tmpy = -1, key = a[x][y]-1;
		if (x+1<r && a[x+1][y]<=key) {
			key = a[x+1][y];
			tmpx = x+1;
			tmpy = y;
		}
		if (y+1<c && a[x][y+1]<=key) {
			key = a[x][y+1];
			tmpx = x;
			tmpy = y+1;
		}
		if (y>0 && a[x][y-1]<=key) {
			key = a[x][y-1];
			tmpx = x;
			tmpy = y-1;
		}
		if (x>0 && a[x-1][y]<=key) {
			key = a[x-1][y];
			tmpx = x-1;
			tmpy = y;
		}
		if (tmpx==-1) {
			col = m++;
			break;
		}
		if (b[tmpx][tmpy]=='.') {
			x = tmpx;
			y = tmpy;
			qx.push(x);
			qy.push(y);
			continue;
		}
		col = b[tmpx][tmpy]-'a';
		break;
	}
	while (!qx.empty()) {
		b[qx.front()][qy.front()] = 'a' + col;
		qx.pop();
		qy.pop();
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas, cass = 0;
	for (scanf("%d", &cas); cas--; ) {
		scanf("%d %d", &r, &c);
		for (int i=0; i<r; ++i) for (int j=0; j<c; ++j) {
			scanf("%d", &a[i][j]);
			b[i][j] = '.';
		}
		m = 0;
		for (int i=0; i<r; ++i) for (int j=0; j<c; ++j) if (b[i][j]=='.') bfs(i, j);
		printf("Case #%d:\n", ++cass);
		for (int i=0; i<r; ++i,puts("")) {
			for (int j=0; j<c; ++j) {
				if (j) printf(" ");
				printf("%c", b[i][j]);
			}
		}
	}
	return 0;
}

