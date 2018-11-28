#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <assert.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <iostream>
#include <sstream>

#define int64 long long

using namespace std;

string taskname = "bb";

#define MAXN 128

int v[MAXN][MAXN];
int maxx, maxy;
int h[MAXN][MAXN];

int dy[4] = {0, -1, 1, 0};
int dx[4] = {-1, 0, 0, 1};

#define INF 1000000000

int dfs(int x, int y, char c) {
	if (v[x][y]) {
		return v[x][y];
	}
	v[x][y] = c;
	int curmin = INF;
	int dir = -1;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx >= 0 && ny >= 0 && nx < maxx && ny < maxy && h[nx][ny] < h[x][y] && h[nx][ny] < curmin) {
			dir = i;
			curmin = h[nx][ny];
		}
	}
	if (curmin == INF) {
		return 0;
	}
	int nx = x + dx[dir];
	int ny = y + dy[dir];
	if (dfs(nx, ny, c)) {
		v[x][y] = dfs(nx, ny, c);
		return v[x][y];
	} else {
		return 0;
	}
}

int main() 
{
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cin >> maxx >> maxy;
		memset(v, 0, sizeof(v));
		for (int i = 0; i < maxx; i++) {
			for (int j = 0; j < maxy; j++) {
				cin >> h[i][j];
			}
		}
		char cur = 'a';
		for (int i = 0; i < maxx; i++) {
			for (int j = 0; j < maxy; j++) {
				if (!v[i][j]) {
					if (!dfs(i, j, cur)) {
						cur++;
					}
				}
			}
		}
		cout << "Case #" << test << ":" << endl;
		for (int i = 0; i < maxx; i++) {
			for (int j = 0; j < maxy; j++) {
				cout << (char)v[i][j] << " ";
			}
			cout << endl;
		}
	}

	return 0;
}
