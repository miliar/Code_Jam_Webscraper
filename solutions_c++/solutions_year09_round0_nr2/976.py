#include <iostream>
#include <cstring>
#include <vector>
#include <map>
using namespace std;


int t, h, w;
int field[100][100];
char ans[100][100];

char maxid;

int dx[] = { 0,-1,1,0 }, dy[] = {-1,0,0,1};

int flowto(int x, int y) {
	int minv = 10000, mind = -1;
	for (int d = 0; d < 4; d++) {
		int nx = x+dx[d], ny = y+dy[d];
		if (nx < 0 || nx >= w || ny < 0 || ny >= h) continue;
		if (field[ny][nx] < field[y][x] && field[ny][nx] < minv) {
			minv = field[ny][nx];
			mind = d;
		}
	}
	return mind;
}

char go(int x, int y) {
	if (ans[y][x] != '*') return ans[y][x];
	int to = flowto(x, y);
	if (to == -1) return ans[y][x] = maxid++;
	else return ans[y][x] = go(x+dx[to], y+dy[to]);
}

int main() {
	cin>>t;
	for (int tc = 1; tc <= t; tc++) {
		cin>>h>>w;
		for (int y = 0; y < h; y++)
			for (int x = 0; x < w; x++)
				cin>>field[y][x];
		
		maxid = 'a';
		memset(ans,'*',sizeof(ans));
		for (int y = 0; y < h; y++) {
			for (int x = 0; x < w; x++) {
				go(x, y);
			}
		}
		
		cout << "Case #" << tc << ":" << endl;
		for (int y = 0; y < h; y++) {
			for (int x = 0; x < w; x++) {
				if (x) cout << ' ';
				cout << ans[y][x];
			}
			cout << endl;
		}
	}
	return 0;
}