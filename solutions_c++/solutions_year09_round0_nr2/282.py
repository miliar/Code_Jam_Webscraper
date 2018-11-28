#include <iostream>
#include <fstream>

using namespace std;

int map[101][101];
int no[101][101];
int visited[101][101];
int parent[10005];
bool nov[10005];
char mapping[10005];
int m, n;

const int dirrr[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int ufind(int t) {
	if (parent[t] == t) 
		return t;
	else 
		return ufind(parent[t]);
}

void seedColor(int x, int y) {
	int tx = -1;
	int ty = 0;
	int bh = map[x][y];

	for (int dd = 0; dd < 4; ++dd) {
		int bx = x + dirrr[dd][0];
		int by = y + dirrr[dd][1];

		if (bx >= 0 && bx < m && by >=0 && by < n && map[bx][by] < bh) {
			bh = map[bx][by];
			tx = bx;
			ty = by;
		}
	}

	if (tx != -1) {
		parent[no[x][y]] = no[tx][ty];
		no[x][y] = ufind(no[tx][ty]);
		no[tx][ty] = no[x][y];
	}
}


int main(int argc, _TCHAR* argv[])
{
	ifstream cin("test.in");
	ofstream fout("test.out");

	int t;
	cin >> t;

	for (int i = 0; i < t; ++i) {
		cin >> m >> n;
		
		for (int j = 0; j < 10005; ++j) {
			nov[j] = true;
			parent[j] = j;
		}

		for (int j = 0; j < m; ++j) {
			for (int k = 0; k < n; ++k) {
				cin >> map[j][k];
				visited[j][k] = false;
				no[j][k] = j * n + k;
				cout << no[j][k] << ' ';
			}
			cout << endl;
		}

		for (int j = 0; j < m; ++j) 
			for (int k = 0; k < n; ++k) 
				seedColor(j, k);

		for (int j = 0; j < m; ++j) 
			for (int k = 0; k < n; ++k) 
				no[j][k] = ufind(no[j][k]);

		char ttttt = 'a';

		for (int j = 0; j < m; ++j) {
			for (int k = 0; k < n; ++k) {
				if (nov[no[j][k]]) {
					mapping[no[j][k]] = ttttt;
					ttttt++;
					nov[no[j][k]] = false;
				}
				cout << no[j][k] << ' ';
			}
			cout << endl;
		}
		fout << "Case #" << i+1 << ':' << endl;
		for (int j = 0; j < m; ++j) {
			for (int k = 0; k < n-1; ++k) {
				cout << mapping[no[j][k]] << ' ';
				fout << mapping[no[j][k]] << ' ';
			}
			cout << mapping[no[j][n-1]] << endl;
			fout << mapping[no[j][n-1]] << endl;
		}
		
	}
	
	return 0;
}

