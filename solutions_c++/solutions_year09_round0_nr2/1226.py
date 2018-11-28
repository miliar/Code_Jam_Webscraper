#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

const int N = 128;

int a[N][N];
int basin[N][N];
bool adj[N][N][4];
const int dr[] = {-1, 0, 0, 1};
const int dc[] = {0, -1, 1, 0};
int height, width;

void repaint() {
	int cur = 0;
	map<int, int> m;
	for (int r = 0; r < height; r++)
		for (int c = 0; c < width; c++)
			if (m.find(basin[r][c]) == m.end())
				m[basin[r][c]] = cur++;
	for (int r = 0; r < height; r++)
		for (int c = 0; c < width; c++)
			basin[r][c] = m[basin[r][c]];
}

void dfs(int r, int c, int cur) {
	if (basin[r][c] != -1) return;
	basin[r][c] = cur;
	for (int i = 0; i < 4; i++) {
		int nr = r + dr[i];
		int nc = c + dc[i];
		if (nr < 0 || nr >= height || nc < 0 || nc >= width)
			continue;
		for (int j = 0; j < 4; j++)
			if (adj[nr][nc][j] && nr + dr[j] == r && nc + dc[j] == c)
				dfs(nr, nc, cur);
	}
}

int solve() {	
	scanf("%d%d", &height, &width);
	for (int r = 0; r < height; r++)
		for (int c = 0; c < width; c++) {
			scanf("%d", &a[r][c]);
			basin[r][c] = -1;
			for (int i = 0; i < 4; i++)
				adj[r][c][i] = false;
		}

	vector<pair<int, int> > sinks;
	for (int r = 0; r < height; r++)
		for (int c = 0; c < width; c++) {
			vector<pair<int, int> > cand;			
			for (int dir = 0; dir < 4; dir++) {
				int nr = r + dr[dir];
				int nc = c + dc[dir];
				if (nr < 0 || nr >= height || nc < 0 || nc >= width)
					continue;
				if (a[nr][nc] < a[r][c])
					cand.pb(mp(a[nr][nc], dir));
			}
			sort(all(cand));
			if (cand.empty())
				sinks.pb(mp(r, c));
			else
				adj[r][c][cand[0].second] = true;
		}

	for (int i = 0; i < sinks.size(); i++)
		dfs(sinks[i].first, sinks[i].second, i);
	
	repaint();
	
	for (int r = 0; r < height; r++) {
		for (int c = 0; c < width; c++) {
			printf("%c", (char)(basin[r][c] + 'a'));
			if (c < width - 1)
				printf(" ");
		}
		printf("\n");
	}
}

int main () {
	freopen("b.in", "r", stdin); freopen("b.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++) {
		printf("Case #%d:\n", T);		
		solve();
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
