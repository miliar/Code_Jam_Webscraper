#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
//#include <vector>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

char square[22][22];

int encode(int x, int y) {
	return (x << 8) + y;
}

void decode(int p, int &x, int &y) {
	x = (p >> 8) & 0xff;
	y = p & 0xff;
}

bool valid(int W, int x1, int y1, int x2, int y2) {
	return
	  	x1 >= 0 && x1 < W &&
	  	y1 >= 0 && y1 < W &&
	  	x2 >= 0 && x2 < W &&
	  	y2 >= 0 && y2 < W;
}

const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};

string bfs(const int W, int target) {
	map<pair<int, int>, string> best;
	queue<pair<int, int> > q;

	for(int i = 0; i < W; ++i) {
		for(int j = 0; j < W; ++j) {
			if(isdigit(square[i][j])) {
				int npos = encode(i,j);
				best[make_pair(npos, square[i][j] - '0')] = square[i][j];
				q.push(make_pair(npos, square[i][j] - '0'));
			}
		}
	}

	while(!q.empty()) {
		pair<int, int> node = q.front();
		q.pop();

		int x, y;
		decode(node.first, x, y);
//		printf("Popped (%d,%d) %d = %s\n", x, y, node.second, best[node].c_str());

		if(node.second == target) {
			string ret = best[node];
			for(map<pair<int, int>, string>::iterator it = best.begin(); it != best.end(); ++it) {
				if(it->first.second == target) {
					if(it->second.size() == ret.size())
						ret = min(ret, it->second);
				}
			}
			return ret;
		}

		const string &curstr = best[node];
		const size_t curstrlen = curstr.size() + 2;

		for(int d = 0; d < 16; ++d) {
			int nx1 = x + dx[d % 4];
			int ny1 = y + dy[d % 4];
			int nx2 = nx1 + dx[d / 4];
			int ny2 = ny1 + dy[d / 4];

			if(valid(W, nx1, ny1, nx2, ny2)) {
				int npos = encode(nx2, ny2);
				int nval;
				if(square[nx1][ny1] == '+') {
					nval = node.second + (square[nx2][ny2] - '0');
				} else {
					nval = node.second - (square[nx2][ny2] - '0');
				}
				pair<int, int> npair = make_pair(npos, nval);

				if(best.find(npair) == best.end()) {
					best[npair] = curstr + square[nx1][ny1] + square[nx2][ny2];
					q.push(npair);
				} else {
					assert(best[npair].size() <= curstrlen);
					if(best[npair].size() == curstrlen) {
						best[npair] = min(best[npair], curstr + square[nx1][ny1] + square[nx2][ny2]);
					}
				}
			}
		}
	}
	assert(!"No solution found");
}

bool solve(int P) {
	printf("Case #%d:\n", P+1);
	int W, Q;
	if(scanf("%d%d", &W, &Q) != 2) {
		assert(!"Failed to read size");
	}

	for(int i = 0; i < W; ++i) {
		scanf("%s", square[i]);
	}

	for(int i = 0; i < Q; ++i) {
		int target;
		scanf("%d", &target);
		printf("%s\n", bfs(W, target).c_str());
	}

	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
