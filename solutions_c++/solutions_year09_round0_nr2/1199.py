#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <string>
#include <list>
#include <map>
#include <cmath>

using namespace std;

const int INF = (1<<29);
const int dx[] = {0, -1, 1, 0};
const int dy[] = {-1, 0, 0, 1};

int H, W;

int m[100][100];
int visited[100][100];

int n;

inline int getAltitude(int x, int y) {
	if(x < 0 || x >=W || y < 0 || y >= H) return INF;
	return m[x][y];
}


int dfs(int x, int y) {
	if(visited[x][y] != -1) return visited[x][y];
	int d, min = INF;
	for(int i = 0; i < 4; i++) {
		int c = getAltitude(x+dx[i], y+dy[i]);		
		if(c < min) {
			min = c;
			d = i;
		}
	}
	return visited[x][y] = (min >= m[x][y])?n++:dfs(x+dx[d], y+dy[d]);
}

void solve() {
	cin >> H >> W;
	for(int y = 0; y < H; y++) 
		for(int x = 0; x < W; x++) 
			cin >> m[x][y];

	memset(visited, -1, sizeof(visited));
	n = 0;

	
	for(int y = 0; y < H; y++) 
		for(int x = 0; x < W; x++) 
			if(visited[x][y] == -1) dfs(x, y);		


	int h[26];
	n = 0;
	memset(h, -1, sizeof(h));

	for(int y = 0; y < H; y++) {
		for(int x = 0; x < W; x++) { 
			if(h[visited[x][y]] == -1) h[visited[x][y]] = n++;
			cout << char('a' + h[visited[x][y]]) << " ";
		}
		cout << endl;
	}
}


int main() {		
	int C;
	cin >> C;
	for(int i = 1; i <= C; i++) {
		cout << "Case #" << i << ": " << endl;
		solve();
	}
}