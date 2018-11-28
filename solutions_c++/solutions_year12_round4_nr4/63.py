#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define foreach(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i) 

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef unsigned long long ll;

using namespace std;

char maze[10][10];
int cx[10];
int cy[10];

struct point
{
	int x, y;
	point(int x, int y) : x(x), y(y) { }
};

char visited[10][10];

void findPoints(int x, int y, vector<point>& ret) {
	queue<point> pq;

	memset(visited, 0, sizeof(visited));

	pq.push(point(x, y));

	while(!pq.empty()) {
		point c = pq.front();
		pq.pop();
		y = c.y; x = c.x;
		if (visited[y][x])
			continue;
		ret.push_back(c);
		visited[y][x] = 1;

		if (!visited[y-1][x] && maze[y-1][x] == '.')
			pq.push(point(x, y-1));
		if (!visited[y][x-1] && maze[y][x-1] == '.')
			pq.push(point(x-1, y));
		if (!visited[y][x+1] && maze[y][x+1] == '.')
			pq.push(point(x+1, y));
	}
}

set<ll> vis;
int dx, dy;

ll target_pts;

bool dfs(ll mask)
{
	ll t;
	ll newmask;
	bool ok = true;

	vis.insert(mask);

	if ((mask & (mask-1)) == 0) {
		return mask & target_pts;
	}

	t = mask;
	newmask = 0;
	while (t) {
		int p = __builtin_ctzl(t);
		t &= (t-1);
		int y = p / 8;
		int x = p % 8;
		if (maze[y+2][x+1] == '.') {
			if (y > dy) {
				ok = false;
				break;
			}
			newmask |= ((ll)1 << (p+8));
		} else {
			newmask |= ((ll)1 << p);
		}
	}

	if (ok && vis.find(newmask) == vis.end()) {
		if (dfs(newmask))
			return true;
	}

	t = mask;
	newmask = 0;
	while (t) {
		int p = __builtin_ctzl(t);
		t &= (t-1);
		int y = p / 8;
		int x = p % 8;
		if (maze[y+1][x+2] == '.') {
			newmask |= ((ll)1 << (p+1));
		} else {
			newmask |= ((ll)1 << p);
		}
	}

	if (vis.find(newmask) == vis.end()) {
		if (dfs(newmask))
			return true;
	}

	t = mask;
	newmask = 0;
	while (t) {
		int p = __builtin_ctzl(t);
		t &= (t-1);
		int y = p / 8;
		int x = p % 8;
		if (maze[y+1][x] == '.') {
			newmask |= ((ll)1 << (p-1));
		} else {
			newmask |= ((ll)1 << p);
		}
	}

	if (vis.find(newmask) == vis.end()) {
		if (dfs(newmask))
			return true;
	}

	return false;
}

bool solve(int cx, int cy, const vector<point>& pts)
{
	vis.clear();
	ll mask = 0;
	for (int i = 0; i < pts.size(); i++)
		mask |= ((ll)1 << ((pts[i].x - 1) + (pts[i].y - 1) * 8));
	dx = cx - 1;
	dy = cy - 1;
	target_pts = mask;
	return dfs(mask);
}

int main(int argc, const char* argv[])
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++) {
		int R, C;
		string str;
		int nc = 0;
		memset(cx, -1, sizeof(cx));
		memset(cy, -1, sizeof(cy));
		cin >> R >> C;
		getline(cin, str);
		//cerr << "Rows: " << R << " Cols: " << C << endl;
		for (int i = 0; i < R; i++) {
			getline(cin, str);
		//	cerr << str << endl;
			for (int j = 0; j < C; j++) {
				maze[i][j] = str[j];
				if (str[j] >= '0' && str[j] <= '9') {
					cx[str[j] - '0'] = j;
					cy[str[j] - '0'] = i;
					maze[i][j] = '.';
					nc = max<int>(nc, str[j] - '0' + 1);
				}
			}
		}
		cout << "Case #" << c << ": " << endl;
		for (int cave = 0; cave < nc; cave++) {
			vector<point> points;
			cout << cave << ": ";
			findPoints(cx[cave], cy[cave], points);
			cout << points.size() << " ";
			cout << (solve(cx[cave], cy[cave], points) ? "Lucky" : "Unlucky") << endl;
		}
	}
    return 0;
}
