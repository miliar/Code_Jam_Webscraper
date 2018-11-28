#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


int dxy[4][2] = { {-1,0}, {0,-1}, {0,1}, {1,0} };

int n, m, a[100][100];
char ans[100][100], next;

char get (int x, int y) {
	if (ans[x][y])  return ans[x][y];
	int sel = -1,  sx, sy;
	for (int i=0; i<4; ++i) {
		int nx = x + dxy[i][0],
			ny = y + dxy[i][1];
		if (nx >= 0 && ny >= 0 && nx < n && ny < m)
			if (a[nx][ny] < a[x][y] && (sel == -1 || a[nx][ny] < a[sx][sy]))
				sel = i,  sx = nx,  sy = ny;
	}
	if (sel == -1)
		return ans[x][y] = next++;
	return ans[x][y] = get (sx, sy);
}

int main() {
	freopen ("B.in", "rt", stdin);
	freopen ("B.out", "wt", stdout);

	int ts;
	cin >> ts;
	for (int t=0; t<ts; ++t) {
		cin >> n >> m;
		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j)
				scanf ("%d", &a[i][j]);
		memset (ans, 0, sizeof ans);
		next = 'a';
		printf ("Case #%d:\n", t+1);
		for (int i=0; i<n; ++i) {
			for (int j=0; j<m; ++j)
				printf ("%c ", get (i, j));
			puts("");
		}
	}

}