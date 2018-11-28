#include <iostream>

using namespace std;

int n, m;
int map[111][111];
int mark[111][111];
const int dx[4] = {-1,0,0,1};
const int dy[4] = {0,-1,1,0};

void Load()
{
	cin >> n >> m;
	int i, j;
	memset(map, 0, sizeof(map));
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= m; j++) {
			cin >> map[i][j];
		}
	}
	memset(mark, 0, sizeof(mark));
}



int nb = 0;

void Mark(int i, int j)
{
	int k;
	int mk = -1;
	for (k = 0; k < 4; k++) {
		if (i + dx[k] < 1 || i + dx[k] > n) continue;
		if (j + dy[k] < 1 || j + dy[k] > m) continue;
		if (map[i + dx[k]][j + dy[k]] >= map[i][j]) continue;
		if (mk == -1 || map[i + dx[mk]][j + dy[mk]] > map[i + dx[k]][j + dy[k]]) mk = k;
	}
	if (mk == -1) {
		nb++;
		mark[i][j] = nb;
		return;
	}
	if (mark[i + dx[mk]][j + dy[mk]] == 0)
		Mark(i + dx[mk], j + dy[mk]);
	mark[i][j] = mark[i + dx[mk]][j + dy[mk]];
}


void Save()
{
    int i, j;
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= m; j++) {
			cerr << mark[i][j] << " ";
		}
		cerr << "\n";
	}
	cerr << "********************\n";

}

int id[28];

int nc = -1;
void Solve()
{
    nb = 0;
	int i, j;
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= m; j++) {
			if (mark[i][j] == 0) {
				Mark(i, j);
//				Save();
			}	
		}
	}
	nc = -1;
	memset(id, -1, sizeof(id));
	cout << "\n";
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= m; j++) {
			if (id[mark[i][j]] == -1) {
				nc++;
				id[mark[i][j]] = nc;
			}
			cout << (char)(id[mark[i][j]] + 'a') << " ";
		}
		cout << "\n";
	}
}



int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int T;
	cin >> T;
	for (int ii = 1; ii <= T; ii++) {
		cout << "Case #" << ii << ": ";
		Load();
		Solve();
	}	
	return 0;
}