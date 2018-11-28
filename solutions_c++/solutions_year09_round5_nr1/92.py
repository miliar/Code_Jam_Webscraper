#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

long long compress(pair<int, int> *arr, int sz)
{
	pair<int, int> a[10];
	for (int i = 0; i < sz; ++i) a[i] = arr[i];
	sort(a, a + sz);
	int minx = 1024, miny = 1024;
	for (int i = 0; i < sz; ++i) {
		minx = min(minx, a[i].first);
		miny = min(miny, a[i].second);
	}
	long long ret = 0;
	ret = minx;
	ret <<= 4;
	ret |= miny;
	for (int i = 0; i < sz; ++i) {
		ret <<= 3;
		ret |= (a[i].first - minx);
		ret <<= 3;
		ret |= (a[i].second - miny);
	}
	return ret;
}

void decompress(long long now, int sz, pair<int, int> *arr)
{
	for (int i = 0; i < sz; ++i) {
		arr[i].second = now & 7;
		now >>= 3;
		arr[i].first = now & 7;
		now >>= 3;
	}
	int miny = now & 15;
	now >>= 4;
	int minx = (int)now;
	for (int i = 0; i < sz; ++i) {
		arr[i].first += minx;
		arr[i].second += miny;
	}
}

char maze[16][16];
int n, m;
pair<int, int> initial[10];
pair<int, int> target[10];
int isize, tsize;

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

bool conn(pair<int, int> a, pair<int, int> b)
{
	if (a.first == b.first) return abs(a.second - b.second) == 1;
	if (a.second == b.second) return abs(a.first - b.first) == 1;
	return false;
}

bool isstable(int sz, pair<int, int> *arr)
{
	bool ved[10] = {false};
	queue<int> q;
	q.push(0);
	int left = sz - 1;
	ved[0] = true;
	while (!q.empty()) {
		int now = q.front();
		q.pop();
		for (int i = 0; i < sz; ++i) {
			if (ved[i]) continue;
			if (conn(arr[now], arr[i])) {
				--left;
				ved[i] = true;
				q.push(i);
			}
		}
	}
	return left == 0;
}

bool isok(int nx, int ny, int isize, pair<int, int> *xy)
{
	if (nx < 0 || nx >= n || ny < 0 || ny >= m) return false;
	if (maze[nx][ny] != '.') return false;
	for (int i = 0; i < isize; ++i) {
		if (xy[i].first == nx && xy[i].second == ny) return false;
	}
	return true;
}

int run()
{
	scanf("%d %d", &n, &m);
	isize = tsize = 0;
	for (int i = 0; i < n; ++i) {
		scanf("%s", maze[i]);
		for (int j = 0; j < m; ++j) {
			if (maze[i][j] == 'x') {
				target[tsize].first = i;
				target[tsize++].second = j;
				maze[i][j] = '.';
			}
			else if (maze[i][j] == 'o') {
				initial[isize].first = i;
				initial[isize++].second = j;
				maze[i][j] = '.';
			}
			else if (maze[i][j] == 'w') {
				initial[isize].first = i;
				initial[isize++].second = j;
				target[tsize].first = i;
				target[tsize++].second = j;
				maze[i][j] = '.';
			}
		}
	}
	queue<long long> q;
	map<long long, int> mp;
	long long now = compress(initial, isize);
	long long tt = compress(target, tsize);
	if (now == tt) return 0;
	q.push(now);
	mp[now] = 0;
	while (!q.empty()) {
		long long now = q.front();
		q.pop();
		int curstep = mp[now];
		pair<int, int> xy[10];
		decompress(now, isize, xy);
		bool flag = isstable(isize, xy);
		for (int i = 0; i < isize; ++i) {
			int cx = xy[i].first, cy = xy[i].second;
			for (int k = 0; k < 4; ++k) {
				int nx = cx + dx[k], ny = cy + dy[k];
				int lx = cx - dx[k], ly = cy - dy[k];
				if (isok(nx, ny, isize, xy) && isok(lx, ly, isize, xy)) {
					xy[i].first = nx, xy[i].second = ny;
					long long next = compress(xy, isize);
					if (flag || isstable(isize, xy)) {
						if (next == tt) {
							return curstep + 1;
						}
						if (mp.find(next) == mp.end()) {
							mp[next] = curstep + 1;
							q.push(next);
						}
					}
					xy[i].first = cx, xy[i].second = cy;
				}
			}
		}
	}
	return -1;
}

int main()
{
	freopen("Ain2.txt", "r", stdin);
	freopen("Aout2.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, run());
	}
	return 0;
}
