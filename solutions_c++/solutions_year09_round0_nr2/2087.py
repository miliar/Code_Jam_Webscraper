#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include<iostream>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<list>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<string>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define INF  ((1 << 31) - 1)
#define LLINF  ((ll)((1LL << 63) - 1))
#define eps 0.00000001
#define million 1000000
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;

char cur;

char dfs(int x, int y,  vector<vector<bool> > & used, vector<string> & ans, vector<vector<int> > & plan) {
	if (used[x][y]) return ans[x][y];
	used[x][y] = true;
	int dx [] = {-1, 0, 0, +1};	
	int dy [] = {0, -1, +1, 0};	
	int min_ = INF;
	int dir = -1;
	for (int d = 0; d < 4; ++d)
		if (x + dx[d] >= 0 && y + dy[d] >= 0 && x + dx[d] < used.size() && y + dy[d] < used[0].size() && min_ > plan[x + dx[d]][y + dy[d]] && plan[x][y] > plan[x + dx[d]][y + dy[d]]) {
			min_ = plan[x + dx[d]][y + dy[d]];
			dir = d;
		}
	if (dir >= 0) {
		return ans[x][y] = dfs(x + dx[dir], y + dy[dir], used, ans, plan);
	} else 
		return ans[x][y] = cur++;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int id = 0; id < T; ++id) {
		cout << "Case #" << id + 1 << ":\n";
		int h, w;
		cin >> h >> w;
		vector<vector<int> > plan(h, vector<int> (w, -1));
		vector<vector<bool> > used(h, vector<bool> (w, false));
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				scanf("%d", &plan[i][j]);
			}
		}
		cur = 'a';
		vector<string> ans(h, string(w, '#')); 
		for (int i = 0; i < h; ++i)
			for(int j = 0; j < w; ++j) {
				if (!used[i][j]) {
					dfs(i, j, used, ans, plan);
				}
			}
		for (int i = 0; i < h; ++i) {
			for(int j = 0; j < w; ++j) {
				printf("%c ", ans[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}