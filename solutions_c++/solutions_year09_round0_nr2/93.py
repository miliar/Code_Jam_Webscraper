
#include <iostream>
#include <cstdio>

using namespace std;

int d[100][100];
char ans[100][100];
int n, m;
int filln;

void Input() {
	cin >> n >> m;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> d[i][j];
		}
	}
}

void Output() {
	for (int i = 0; i < n; ++i) {
		cout << ans[i][0];
		for (int j = 1; j < m; ++j) {
			cout << " " << ans[i][j];
		}
		cout << endl;
	}
}

// NWES
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

char Where(int a, int b) {
	while (true) {
		int min = (int)1e9;
		int mini = -1;
		for (int i = 0; i < 4; ++i) {
			int ni = a + dx[i];
			int nj = b + dy[i];
			if (ni < n && ni >= 0 && nj < m && nj >= 0) {
				if (d[ni][nj] < d[a][b]) {
					if (d[ni][nj] < min) {
						min = d[ni][nj];
						mini = i;
					}
				}
			}
		}
		if (mini == -1) {
			return ans[a][b];
		}
		a = a + dx[mini];
		b = b + dy[mini];
	}
}	

void Fill(int a, int b, char c) {
	while (true) {
		ans[a][b] = c;
		int min = (int)1e9;
		int mini = -1;
		for (int i = 0; i < 4; ++i) {
			int ni = a + dx[i];
			int nj = b + dy[i];
			if (ni < n && ni >= 0 && nj < m && nj >= 0) {
				if (d[ni][nj] < d[a][b]) {
					if (d[ni][nj] < min) {
						min = d[ni][nj];
						mini = i;
					}
				}
			}
		}
		if (mini == -1) {
			return;
		}
		a = a + dx[mini];
		b = b + dy[mini];
	}
}

void Process() {
	memset(ans, 0, sizeof(ans));
	Input();
	char nc = 'a';
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (ans[i][j] == 0) {
				char c = Where(i, j);
				if (c == 0) {
					Fill(i, j, nc);
					++nc;
				} else {
					Fill(i, j, c);
				}
			}
		}
	}
	Output();
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		printf("Case #%d:\n", i + 1);
		Process();
	}
	return 0;
}
