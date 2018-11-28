#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
using namespace std;

struct portal_s
{
	int nil;
	int r;
	int c;
	int dir;

	inline bool friend operator == (const portal_s &p, const portal_s &q)
	{
		return (p.nil && q.nil) || (!p.nil && !q.nil && p.r == q.r && p.c == q.c && p.dir == q.dir);
	}

	inline bool friend operator < (const portal_s &p, const portal_s &q)
	{
		if (p.nil != q.nil)
			return p.nil < q.nil;
		if (p.nil)
			return false;
		if (p.r != q.r)
			return p.r < q.r;
		if (p.c != q.c)
			return p.c < q.c;
		return p.dir < q.dir;
	}
};

struct state_s
{
	int r;
	int c;
	struct portal_s blue, yellow;
	int step;

	inline bool friend operator == (const state_s &p, const state_s &q)
	{
		return p.r == q.r && p.c == q.c && ((p.blue == q.blue && p.yellow == q.yellow) || (p.blue == q.yellow && p.yellow == q.blue));
	}

	inline bool friend operator < (const state_s &p, const state_s &q)
	{
		if (p.r != q.r)
			return p.r < q.r;
		if (p.c != q.c)
			return p.c < q.c;
		if (!(p.blue == q.blue))
			return p.blue < q.blue;
		return p.yellow < q.yellow;
	}
};

map<state_s, int> did;
queue<state_s> que, nque;

int R, C;
char data[16][16];

const int ways[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

int invalid(int r, int c)
{
	return !(0 <= r && r < R && 0 <= c && c < C && data[r][c] != '#');
}

void go(state_s &s, queue<state_s> &que)
{
	if (did.find(s) == did.end())
	{
		did.insert(make_pair(s, s.step));
		que.push(s);
	}
}

void move(state_s &s, int dir)
{
	int r = s.r;
	int c = s.c;
	if (s.blue.r == r && s.blue.c == c && s.blue.dir == dir)
	{
		r = s.yellow.r;
		c = s.yellow.c;
	}
	else if (s.yellow.r == r && s.yellow.c == c && s.yellow.dir == dir)
	{
		r = s.blue.r;
		c = s.blue.c;
	}
	else
	{
		r += ways[dir][0];
		c += ways[dir][1];
	}
	if (invalid(r, c))
		return;
	state_s nex = s;
	nex.step++;
	nex.r = r;
	nex.c = c;
	go(nex, nque);
}

void shoot(state_s &s, int dir)
{
	int r = s.r;
	int c = s.c;
	for (;;)
	{
		r += ways[dir][0];
		c += ways[dir][1];
		if (invalid(r, c))
		{
			r -= ways[dir][0];
			c -= ways[dir][1];
			break;
		}
	}

	{
		state_s nex = s;
		nex.blue.nil = false;
		nex.blue.r = r;
		nex.blue.c = c;
		nex.blue.dir = dir;

		if (!(nex.blue == nex.yellow))
			go(nex, que);
	}

	{
		state_s nex = s;
		nex.yellow.nil = false;
		nex.yellow.r = r;
		nex.yellow.c = c;
		nex.yellow.dir = dir;

		if (!(nex.blue == nex.yellow))
			go(nex, que);
	}
}

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		did.clear();
		for (;!que.empty();)
			que.pop();
		for (;!nque.empty();)
			nque.pop();
		scanf("%d %d", &R, &C);
		int i, j;
		for (i = 0;i < R;i++)
			scanf("%s", data[i]);

		int rs, cs;
		int re, ce;
		for (i = 0;i < R;i++)
		{
			for (j = 0;j < C;j++)
			{
				switch (data[i][j])
				{
				case 'O':
					rs = i;
					cs = j;
					break;
				case 'X':
					re = i;
					ce = j;
					break;
				}
			}
		}

		state_s cur;
		cur.r = rs;
		cur.c = cs;
		cur.blue.nil = true;
		cur.yellow.nil = true;
		cur.step = 0;
		
		que.push(cur);
		
		did.insert(make_pair(cur, true));

		int ex = 0;

		for (;;)
		{
			for (;!que.empty();)
			{
				state_s now;
				now = que.front();
				que.pop();

				if (now.r == re && now.c == ce)
				{
					printf("Case #%d: %d\n", ti, now.step);
					ex = true;
					break;
				}

				int dir;
				for (dir = 0;dir < 4;dir++)
					shoot(now, dir);
				for (dir = 0;dir < 4;dir++)
					move(now, dir);
			}
			
			if (ex)
				break;

			if (nque.empty())
				break;

			que = nque;

			for (;!nque.empty();)
				nque.pop();
		}
		if (!ex)
			printf("Case #%d: THE CAKE IS A LIE\n", ti);
		fprintf(stderr, "%d", ti);
	}
	return 0;
}
