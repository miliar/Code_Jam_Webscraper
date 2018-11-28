/*
'From each cell, water flows down to at most one of its 4 neighboring cells.
'For each cell, if none of its 4 neighboring cells has a lower altitude than the current cells, then the water does not flow, and the current cell is called a sink.
'Otherwise, water flows from the current cell to the neighbor with the lowest altitude.
'In case of a tie, water will choose the first direction with the lowest altitude from this list: North, West, East, South.
'Every cell that drains directly or indirectly to the same sink is part of the same drainage basin. 
'Each basin is labeled by a unique lower-case letter, in such a way that, when the rows of the map are concatenated from top to bottom, the resulting string is lexicographically smallest. (In particular, the basin of the most North-Western cell is always labeled 'a'.)
*/

#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int maxn = 110;
const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int tasks;
int n,m;
int h[maxn][maxn];

int f[maxn][maxn];
char ans[maxn][maxn];

void init() {
	cin >> n >> m;
	memset(h, 0, sizeof(h));
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++) {
			f[i][j] = i*m+j;
			cin >> h[i][j];
		}
}

int father(int x) {
	if (f[x/m][x%m] == x)
		return x;
	else {
		int ret = father(f[x/m][x%m]);
		f[x/m][x%m] = ret;
		return ret;
	}
}

void merge(int x1, int y1, int x2, int y2) {
	int f1 = father(f[x1][y1]);
	int f2 = father(f[x2][y2]);
	if (f1 != f2)
		f[f1/m][f1%m] = f2;
}

void work() {
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++) {
			int d = -1;
			int curh = h[i][j];

			for (int t=0; t<4; t++)
				if (i+dx[t]>=0&&i+dx[t]<n&&j+dy[t]>=0&&j+dy[t]<m
					&&h[i+dx[t]][j+dy[t]]<curh) {
						curh = h[i+dx[t]][j+dy[t]];
						d = t;
				}
			
			if (d != -1) {
				int x = i + dx[d];
				int y = j + dy[d];
				merge(i, j, x, y);
			}
		}
}

int link[maxn*maxn];

void print() {
	int cur = 0;
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
			f[i][j] = father(f[i][j]);
	for (int i=0; i<maxn*maxn; i++)
		link[i] = -1;
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++) {
			int c = link[f[i][j]];
			if (c==-1) {
				link[f[i][j]] = cur;
				c = link[f[i][j]];
				cur++;
			}
			ans[i][j] = (char)('a'+c);
		}
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> tasks;
	for (int i=0; i<tasks; i++) {
		init();
		work();
		print();
		cout << "Case #" << i+1 << ":" << endl;
		for (int i=0; i<n; i++) {
			cout << ans[i][0];
			for (int j=1; j<m; j++)
				cout << " " << ans[i][j];
			cout << endl;
		}
	}
}