#include <iostream>
#include <cstdio>

int n, m;
int count;
int cc[5][5];
char map[5][5];
int g[5][5];

void search(int x, int y)
{
	if (x == n) {
		bool check = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (cc[i][j] != 1) check = false;
	    if (check) 
			count++;
		return;
	}
	if (y == m) {
		search(x + 1, 0);
		return;
	}
	int x1, y1, x2, y2;
	if (map[x][y] == '-') {
		x1 = x;
		y1 = (y + m - 1) % m;
		x2 = x;
		y2 = (y + 1) % m;
	}
	if (map[x][y] == '|') {
		x1 = (x + n - 1) % n;
		y1 = y;
		x2 = (x + 1) % n;
		y2 = y;
	}
	if (map[x][y] == '/') {
		x1 = (x + n - 1) % n;
		y1 = (y + 1) % m;
		x2 = (x + 1) % n;
		y2 = (y + m - 1) % m;
	}
	if (map[x][y] == '\\') {
		x1 = (x + n - 1) % n;
		y1 = (y + m - 1) % m;
		x2 = (x + 1) % n;
		y2 = (y + 1) % m;
	}
	cc[x1][y1]++;
	g[x][y] = 0;
	search(x, y + 1);
	cc[x1][y1]--;
	cc[x2][y2]++;
	g[x][y] = 1;
	search(x, y + 1);
	cc[x2][y2]--;
}

int main() 
{
	freopen("p3.in", "r", stdin);
	freopen("p3.out", "w", stdout);
	int T;
	std::cin >> T;
	for (int t = 0; t < T; t++) {
		std::cin >> n >> m;
		for (int i = 0; i < n; i++)
			std::cin >> map[i];
		count = 0;
		search(0, 0);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				cc[i][j] = 0;
		std::cout << "Case #" << t + 1 << ": ";
		std::cout << count;
		std::cout << std::endl;
	}
	return 0;
}