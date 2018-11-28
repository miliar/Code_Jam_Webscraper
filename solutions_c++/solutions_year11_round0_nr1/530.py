#include<cstdio>
#include<cstring>
#include<queue>
#include<utility>
using namespace std;

const int MAXN = 111;
#define MP make_pair
#define X first.first
#define Y first.second
#define P second

queue< pair<pair<int, int>, int> > q;
char s[MAXN][2];
int b[MAXN];
int f[MAXN][MAXN][MAXN];
int n;

void update(int x, int y, int p, int step)
{
	if (x < 1 || y < 1 || x > 100 || y > 100 || f[x][y][p] != -1) return;
	f[x][y][p] = step;
	q.push(MP(MP(x, y), p));
}

int go(int x, int y, int p)
{
	memset(f, -1, sizeof(f));
	f[x][y][p] = 0;
	pair<pair<int, int>, int> tmp;
	while (!q.empty()) q.pop();
	q.push(MP(MP(x, y), p));
	while (!q.empty()) {
		x = q.front().X;
		y = q.front().Y;
		p = q.front().P;
		int step = f[x][y][p] + 1;
		q.pop();
		if (s[p][0] == 'O' && x == b[p]) {
			if (p + 1 == n) return step;
			update(x, y - 1, p + 1, step);
			update(x, y, p + 1, step);
			update(x, y + 1, p + 1, step);
		} else
		if (s[p][0] == 'B' && y == b[p]) {
			if (p + 1 == n) return step;
			update(x - 1, y, p + 1, step);
			update(x, y, p + 1, step);
			update(x + 1, y, p + 1, step);
		} else {
			for (int tx = x - 1; tx <= x + 1; ++tx)
				for (int ty = y - 1; ty <= y + 1; ++ty)
					update(tx, ty, p, step);
		}
	}	
}

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	int T, tt = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%1s %d", s[i], &b[i]);
		printf("Case #%d: %d\n", ++tt, go(1, 1, 0));
	}
	return 0;
}
