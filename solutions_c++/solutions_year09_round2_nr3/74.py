#include <iostream>
#include <algorithm>
#include <fstream>
#include <queue>
#include <sstream>
#include <string>
#include <set>
#include <cmath>
#include <cctype>
using namespace std;

struct Node {
	int x, y;
	int c;
	string rt;
	Node(const int _x, const int _y, const int _c, const string &_rt)
		: x(_x), y(_y), c(_c)
		, rt(_rt)
	{}
	bool operator<(const Node &n) const {
		if (rt.length() != n.rt.length()) return rt.length()>n.rt.length();
		return rt > n.rt;
	}
};

bool isSafe(const int x, const int y, const int w)
{
	return (0<=x && x<w && 0<=y && y<w);
}

const int W = 21;
const int V = 1000;
bool visit[W][W][V];

int main()
{
	fstream fin("in.txt");
	fstream fout("out.txt");

	int T;
	fin >> T;
	for (int q=0; q < T; ++q) {
		fout << "Case #" << q+1 << ":" << endl;

		string field[21];
		int w, m;
		fin >> w >> m;
		for (int i=0; i < w; ++i) {
			fin >> field[i];
		}

		priority_queue<Node> que;
		for (int i=0; i < w; ++i) {
			for (int j=0; j < w; ++j) {
				if (isdigit(field[i][j])) {
					que.push(Node(j, i, field[i][j]-'0', string(1, field[i][j])));
				}
			}
		}

		const int dx[9] = { 0, -1, 1, -2, 2, -1, 1, 0, 0 };
		const int dy[9] = { -2, -1, -1, 0, 0, 1, 1, 2, 0 };
		const int mx[4] = { 0, -1, 1, 0 };
		const int my[4] = { -1, 0, 0, 1 };

		vector<int> dir[9];

		dir[0].push_back(0);

		dir[1].push_back(0);
		dir[1].push_back(1);

		dir[2].push_back(0);
		dir[2].push_back(2);

		dir[3].push_back(1);

		dir[4].push_back(2);

		dir[5].push_back(1);
		dir[5].push_back(3);

		dir[6].push_back(2);
		dir[6].push_back(3);

		dir[7].push_back(3);

		dir[8].push_back(0);
		dir[8].push_back(1);
		dir[8].push_back(2);
		dir[8].push_back(3);

		string ans[300];
		vector<int> query(m);
		bool f[300] = { 0 };
		for (int i=0; i < m; ++i) {
			fin >> query[i];
			f[query[i]] = true;
		}

		int ct = 0;

		fill(&visit[0][0][0], &visit[W-1][W-1][V], false);

		while (que.empty()==false) {
			Node now = que.top();
			que.pop();
			//cout << now.c << " " << now.rt << endl;

			if (now.c >= V-100) continue;
			if (now.c < -100) continue;
			if (visit[now.y][now.x][now.c+100]) continue;
			visit[now.y][now.x][now.c+100] = true;

			if (now.c >0 && f[now.c]) {
				++ct;
				ans[now.c] = now.rt;
				f[now.c] = false;
				cout << now.rt << endl;
			}
			if (ct == m) break;

			for (int i=0; i < 9; ++i) {
				const int nx = now.x + dx[i];
				const int ny = now.y + dy[i];
				if (isSafe(nx, ny, w)==false) continue;
				int val = field[ny][nx]-'0';

				for (int j=0; j < dir[i].size(); ++j) {
					const int tx = now.x + mx[dir[i][j]];
					const int ty = now.y + my[dir[i][j]];
					if (isSafe(tx, ty, w)==false) continue;

					const char t = field[ty][tx];
					const int c = (t=='+'?1:-1) * val;
					que.push(Node(nx, ny, now.c + c, now.rt+t+(char)(val+'0')));
				}
			}
		}
		
		for (int i=0; i < query.size(); ++i) {
			fout << ans[query[i]] << endl;
		}
	}
	return 0;
}