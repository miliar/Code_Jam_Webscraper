#include <iostream>

#include <string.h>

using namespace std;

int t, h, w, visine[100][100];
char res[100][100], nc, cset;

void flow(int x, int y) {
	if (res[x][y] != 0) {
		//cout << "----" << x << " " << y << endl;
		cset = res[x][y];
		return;
	}
	int m = visine[x][y], mx = x, my = y;
	if (x - 1 >= 0 && visine[x - 1][y] < m) {
		m = visine[x - 1][y];
		mx = x - 1;
		my = y;
	}
	if (y - 1 >= 0 && visine[x][y - 1] < m) {
		m = visine[x][y - 1];
		mx = x;
		my = y - 1;
	}
	if (y + 1 < w && visine[x][y + 1] < m) {
		m = visine[x][y + 1];
		mx = x;
		my = y + 1;
	}
	if (x + 1 < h && visine[x + 1][y] < m) {
		m = visine[x + 1][y];
		mx = x + 1;
		my = y;
	}
	if (m == visine[x][y]) {
		//cout << "++++" << x << " " << y << endl;
		cset = nc++;
		res[x][y] = cset;
		return;
	}
	flow(mx, my);
	res[x][y] = cset;
}

int main() {
	cin >> t;
	for (int ti = 0; ti < t; ti++) {
		printf("Case #%d:\n", ti + 1);
		cin >> h >> w;
		nc = 'a';
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				cin >> visine[i][j];
		memset(res, 0, sizeof(res));
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				if (res[i][j] == 0)
					flow(i, j);
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				if (j == w - 1)
					cout << res[i][j] << "\n";
				else
					cout << res[i][j] << " ";
	}
}

