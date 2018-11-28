#include <iostream>
#include <utility>
#include <vector>
using namespace std;
const int MAXS = 100;

const int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
bool valid(int y, int x, int h, int w) {
	return y>=0 && x>=0 && y<h && x<w;
}

pair<int, int> down(int tab[][MAXS], int y, int x, int h, int w) {
	pair<int, int> res = make_pair(y, x);
	for (int i=0; i<4; i++) {
		int yy = y + dir[i][0], xx = x + dir[i][1];
		if (valid(yy, xx, h, w) && tab[res.first][res.second] > tab[yy][xx])
			res = make_pair(yy, xx);
	}
	return res;
}

int main() {
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int T=1; T<=t; T++) {
		int h, w;
		cin >> h >> w;
		int tab[MAXS][MAXS];
		for (int y=0; y<h; y++)
			for (int x=0; x<w; x++)
				cin >> tab[y][x];

		int drain[MAXS][MAXS];
		int drain_cnt = 0;
		memset(drain, -1, sizeof(drain));
		vector<pair<int, int> > stack;
		//find sinks
		for (int y=0; y<h; y++)
			for (int x=0; x<w; x++) {				
				pair<int, int> pt = down(tab, y, x, h, w);
				if (pt.first == y && pt.second == x) {
					drain[y][x] = drain_cnt;
					drain_cnt++;
					stack.push_back(make_pair(y, x));
				}
			}

		//dfs over the map
		while(!stack.empty()) {
			int y = stack.back().first, x = stack.back().second;
			stack.pop_back();
			for (int i=0; i<4; i++) {
				int yy = y + dir[i][0], xx = x+dir[i][1];
				if (valid(yy, xx, h, w) && drain[yy][xx] == -1) {
					pair<int, int> pt = down(tab, yy, xx, h, w);
					if (pt.first == y && pt.second == x) {
						drain[yy][xx] = drain[y][x];
						stack.push_back(make_pair(yy, xx));
					}
				}
			}
		}

		char conv[30];
		memset(conv, 0, sizeof(conv));
		char drain_name = 'a';
		for (int y=0; y<h; y++) 
			for (int x=0; x<w; x++)
				if (!conv[drain[y][x]]) {
					conv[drain[y][x]] = drain_name++;
				}

		cout << "Case #" << T << ":\n";
		for (int y=0; y<h; y++) {
			for (int x=0; x<w; x++)
				cout << conv[drain[y][x]] << " ";
			cout << "\n";
		}
	}
	return 0;
}
