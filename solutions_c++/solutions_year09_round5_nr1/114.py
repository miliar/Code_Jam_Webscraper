#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

int t, T;
int r, c;
char s[16][16];
typedef pair<int, int> ii;
typedef set<ii> state;
state v1, v2;
bool f[16][16];
int dx[] = { 1, 0, -1, 0 };
int dy[] = { 0, -1, 0, 1 };
map<state, ii> M; // state -> (step, connect)
state q[1000000];

void out(state &v)
{
	for (state::const_iterator it = v.begin(); it != v.end(); ++it) {
		printf("(%d, %d) ", it->first, it->second);
	}
	putchar('\n');
}

void dfs(char c, state &v, int x, int y)
{
	if (x < 0 || y < 0 || x >= r || y >= c || f[x][y] || (s[x][y] != c && s[x][y] != 'w'))
		return;
	v.insert(make_pair(x, y));
	f[x][y] = 1;
	for (int i = 0; i < 4; ++i)
		dfs(c, v, x + dx[i], y + dy[i]);
}

int dfs2(int x, int y, int a[16][16])
{
	if (x < 0 || y < 0 || x >= r || y >= c || f[x][y] || !a[x][y])
		return 0;
	int res = 1;
	f[x][y] = 1;
	for (int i = 0; i < 4; ++i)
		res += dfs2(x + dx[i], y + dy[i], a);
	return res;
}

int connect(state &v)
{
	int tmp[16][16] = { 0 };
	//for (int i = 0; i < v; ++i)
	for (state::const_iterator it = v.begin(); it != v.end(); ++it)
		tmp[it->first][it->second] = 1;
	memset(f, 0, sizeof(f));
	return dfs2(v.begin()->first, v.begin()->second, tmp) == v.size();
}

int check(int x, int y, state &v)
{
	if (x < 0 || y < 0 || x >= r || y >= c || s[x][y] == '#' || v.count(make_pair(x, y)))
		return 0;
	return 1;
}

int check(int x, int y, int ind, state &v)
{
	return check(x + dx[ind], y + dy[ind], v) && check(x + dx[(ind + 2) % 4], y + dy[(ind + 2) % 4], v);
}

int run()
{
	scanf("%d %d", &r, &c);
	for (int i = 0; i < r; ++i)
		scanf("%s", s[i]);
	memset(f, 0, sizeof(f));
	int flag = 1;
	for (int i = 0; i < r && flag; ++i) {
		for (int j = 0; j < c && flag; ++j) {
			if (s[i][j] == 'x' || s[i][j] == 'w') {
				dfs('x', v1, i, j);
				flag = 0;
			}
		}
	}
	//sort(v1.begin(), v1.end());
	memset(f, 0, sizeof(f));
	flag = 1;
	for (int i = 0; i < r && flag; ++i) {
		for (int j = 0; j < c && flag; ++j) {
			if (s[i][j] == 'o' || s[i][j] == 'w') {
				dfs('o', v2, i, j);
				flag = 0;
			}
		}
	}
	//sort(v2.begin(), v2.end());
	//out(v1);
	//out(v2);
	int rear = 0, head = 0;
	q[head++] = v2;
	M[v2] = make_pair(0, 1);
	while (rear < head) {
		state v = q[rear++];
		//out(v);
		//printf("{ %d, %d }\n", M[v].first, M[v].second);
		if (v == v1)
			return M[v].first;
		int connected = M[v].second;
		for (state::const_iterator it = v.begin(); it != v.end(); ++it) {
			state nv = v;
			ii cor = *it;
			nv.erase(cor);
			for (int i = 0; i < 4; ++i) {
				if (check(cor.first, cor.second, i, v)) {
					nv.insert(make_pair(cor.first + dx[i], cor.second + dy[i]));
					if (!M.count(nv)) {
						if (connected) {
							M[nv] = make_pair(M[v].first + 1, connect(nv));
							q[head++] = nv;
						}
						else if (connect(nv)) {
							M[nv] = make_pair(M[v].first + 1, 1);
							q[head++] = nv;
						}
					}
					nv.erase(make_pair(cor.first + dx[i], cor.second + dy[i]));
				}
			}
		}
	}
	return -1;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		v1.clear();
		v2.clear();
		M.clear();
		printf("Case #%d: %d\n", t, run());
	}
	return 0;
}
