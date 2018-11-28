#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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

const int MAX=1000;
vector<pair<int,int> > G[MAX][MAX];
bool vis[MAX][MAX];
char ch[MAX][MAX];

void dfs(int x, int y, char c) {
	if (vis[x][y]) return;
	vis[x][y] = 1;
	ch[x][y] = c;
	for (int i=0;i<G[x][y].size();++i)
		dfs(G[x][y][i].first, G[x][y][i].second, c);
}

void solve() {
	int h,w;
	cin >> h >> w;
	vector<vector<int> > b(h, vector<int>(w));
	for (int i=0;i<h;++i) {
		for (int j=0;j<w;++j) {
			cin >> b[i][j];
			G[i][j].clear();
			vis[i][j] = 0;
			ch[i][j] = ' ';
		}
	}

	for (int i=0;i<h;++i) {
		for (int j=0;j<w;++j) {
			const int dx[]={-1,0,0,1};
			const int dy[]={ 0,-1,1,0};
			const int INF = 1<<29;
			pair<int,int> best(INF,INF);
			for (int k=0;k<4;++k) {
				int ni = i + dx[k];
				int nj = j + dy[k];
				if (0 <= ni && ni < h && 0 <= nj && nj < w) {
					best = min(best, make_pair(b[ni][nj],k));
				}
			}
			if (best.first<b[i][j]) {
				G[i][j].push_back(make_pair(i+dx[best.second], j+dy[best.second]));
				G[i+dx[best.second]][j+dy[best.second]].push_back(make_pair(i,j));
			}
		}
	}

	char next = 'a';
	for (int i=0;i<h;++i) {
		for (int j=0;j<w;++j) if (!vis[i][j]) {
			dfs(i,j,next);
			++next;
		}
	}

	for (int i=0;i<h;++i) {
		for (int j=0;j<w;++j) {
			if (j!=0) printf(" ");
			printf("%c", ch[i][j]);
		}
		printf("\n");
	}
}

int main() {
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z) {
		printf("Case #%d:\n", z);
		solve();
	}
}
