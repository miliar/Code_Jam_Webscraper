#include <cstdio>
#include <iostream>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <functional>
#include <set>
#include <map>
#include <cstring>
#include <string>

using namespace std;

int R, C;
int N;
char data[13][13];

struct state_s
{
	pair<int, int> pos[5];
	int dangerous;

	state_s()
	{
		dangerous = 0;
	}

	state_s(long long ev)
	{
		dangerous = ev & 1;
		ev >>= 1;
		int i;
		for (i = N - 1;i >= 0;i--)
		{
			int dv = ev % (R * C);
			pos[i] = make_pair(dv / C, dv % C);
			ev /= (R * C);
		}
	}

	void normalize()
	{
		sort(pos, pos + N);
	}

	long long encode()
	{
		long long v = 0;
		int i;
		for (i = 0;i < N;i++)
		{
			v *= (R * C);
			v += pos[i].first * C + pos[i].second;
		}
		v *= 2;
		v += dangerous;
		return v;
	}
};

set<long long> did;

int ans = 0;

void draw_map(state_s &cur)
{
	int i;
	for (i = 0;i < N;i++)
	{
		char &c = data[cur.pos[i].first][cur.pos[i].second];
		if (c == 'x')
			c = 'w';
		else if (c == '.')
			c = 'o';
	}
}

void undraw_map(state_s &cur)
{
	int i;
	for (i = 0;i < N;i++)
	{
		char &c = data[cur.pos[i].first][cur.pos[i].second];
		if (c == 'w')
			c = 'x';
		else if (c == 'o')
			c = '.';
	}
}

inline int is_allowed(pair<int, int> &dest)
{
	return 0 <= dest.first && dest.first < R && 0 <= dest.second && dest.second < C;
}

inline int is_allowed(int r, int c)
{
	return 0 <= r && r < R && 0 <= c && c < C;
}

int is_adj(pair<int, int> &p, pair<int, int> &q)
{
	int dx = p.first - q.first;
	if (dx < 0) dx *= -1;
	int dy = p.second - q.second;
	if (dy < 0) dy *= -1;
	return dx + dy == 1;
}

int is_dangerous(state_s &cur)
{
	int m[5] = {0, 1, 2, 3, 4};

	int i, j, k;
	for (i = 0;i < N;i++)
	{
		for (j = i + 1;j < N;j++)
		{
			if (is_adj(cur.pos[i], cur.pos[j]))
			{
				int dv = m[j];
				for (k = 0;k < 5;k++)
					if (m[k] == dv)
						m[k] = m[i];
			}
		}
	}
	for (i = 1;i < N;i++)
		if (m[i] != m[0])
			return true;
	return false;
}

const int ways[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0}};

int is_terminal(const state_s &cur)
{
	int i;
	for (i = 0;i < N;i++)
		if (data[cur.pos[i].first][cur.pos[i].second] != 'w')
			return false;
	return true;
}

void process(long long enc)
{
	did.clear();
	queue<long long> que[2];
	int i, j;
	que[0].push(enc);
	did.insert(enc);
	for (ans = 0;;ans++)
	{
		queue<long long> &cur = que[ans & 1];
		queue<long long> &ncur = que[!(ans & 1)];
		if (cur.empty())
		{
			ans = -1;
			return;
		}
		for (;!cur.empty();)
		{
			state_s now(cur.front());
			cur.pop();

			draw_map(now);

			if (is_terminal(now))
				return;

			for (i = 0;i < N;i++)
			{
				int r = now.pos[i].first;
				int c = now.pos[i].second;
				for (j = 0;j < 4;j++)
				{
					int nr = r + ways[j][0];
					int nc = c + ways[j][1];

					int dr = r - ways[j][0];
					int dc = c - ways[j][1];

					if (!is_allowed(nr, nc))
						continue;
					if (!is_allowed(dr, dc))
						continue;

					if (data[dr][dc] != '.' && data[dr][dc] != 'x')
						continue;

					if (data[nr][nc] != '.' && data[nr][nc] != 'x')
						continue;

					state_s next = now;
					next.pos[i] = make_pair(nr, nc);
					next.normalize();
					next.dangerous = is_dangerous(next);

					if (now.dangerous && next.dangerous)
						continue;

					long long enc = next.encode();

					if (did.find(enc) == did.end())
					{
						did.insert(enc);
						ncur.push(enc);
					}
				}
			}

			undraw_map(now);
		}
	}
	cerr << endl << endl << endl;
}

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		scanf("%d %d", &R, &C);
		int i, j;
		for (i = 0;i < R;i++)
			scanf("%s", data[i]);

		state_s first;
		N = 0;
		for (i = 0;i < R;i++)
		{
			for (j = 0;j < C;j++)
			{
				if (data[i][j] == 'o')
				{
					first.pos[N++] = make_pair(i, j);
					data[i][j] = '.';
				}
				else if (data[i][j] == 'w')
				{
					first.pos[N++] = make_pair(i, j);
					data[i][j] = 'x';
				}
			}
		}

		process(first.encode());

		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}
