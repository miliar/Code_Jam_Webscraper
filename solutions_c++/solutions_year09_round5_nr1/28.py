#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cassert>
#include <set>
#include <iostream>
#include <queue>

using namespace std;

typedef pair<int,int>	PII;

int m, n, b;
char board[16][16];

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};

int vis[5];
void dfs(int p, PII t[])
{
	if (vis[p])
		return;
	vis[p] = 1;
	for (int d = 0; d < 4; d++)
	{
		int nx = t[p].first + dx[d];
		int ny = t[p].second + dy[d];
		for (int i = 0; i < b; i++)
			if (nx == t[i].first && ny == t[i].second)
				dfs(i, t);
	}
}

struct state
{
	PII pos[5];
	int dist, stab;
	void normalize()
	{
		sort(pos, pos+b);
	}
	void stable()
	{
		for (int i = 0; i < b; i++)
			vis[i] = 0;
		dfs(0, pos);
		stab = 1;
		for (int i = 0; i < b; i++)
			if (!vis[i])
			{
				stab = 0;
				return;
			}
	}
};

bool operator< (const state &x, const state &y)
{
	for (int i = 0; i < b; i++)
		if (x.pos[i] != y.pos[i])
			return x.pos[i] < y.pos[i];
	return false;
}

bool operator== (const state &x, const state &y)
{
	for (int i = 0; i < b; i++)
		if (x.pos[i] != y.pos[i])
			return false;
	return true;
}

int main()
{
	int kases;
	scanf("%d", &kases);
	for (int kase = 1; kase <= kases; kase++)
	{
		state act, fin;
		act.dist = fin.dist = 0;
		act.stab = fin.stab = 1;
		int finp = 0;
		scanf("%d%d", &m, &n);
		b = 0;
		for (int i = 0; i < m; i++)
		{
			scanf("%s", board[i]);
			for (int j = 0; j < n; j++)
				switch (board[i][j])
				{
				case 'o':
					act.pos[b].first = i;
					act.pos[b].second = j;
					b++;
					board[i][j] = '.';
					break;
				case 'x':
					fin.pos[finp].first = i;
					fin.pos[finp].second = j;
					finp++;
					board[i][j] = '.';
					break;
				case 'w':
					act.pos[b].first = i;
					act.pos[b].second = j;
					b++;
					fin.pos[finp].first = i;
					fin.pos[finp].second = j;
					finp++;
					board[i][j] = '.';
					break;
				}
		}
		assert(b == finp);

		fin.normalize();
		act.normalize();
		
		queue<state> q;
		set<state> vis;
		q.push(act);
		vis.insert(act);
		while (!q.empty())
		{
			act = q.front();

/*
			char board2[16][16];
			memcpy(board2, board, sizeof(board));
			for (int i = 0; i < b; i++)
				board2[act.pos[i].first][act.pos[i].second] = 'x';
			for (int i = 0; i < m; i++)
				cout << board2[i] << endl;
			cout << endl;
*/

			if (act == fin)
				break;
			q.pop();

			for (int i = 0; i < b; i++)
				for (int d = 0; d < 4; d++)
				{
					const int nx = act.pos[i].first + dx[d];
					const int ny = act.pos[i].second + dy[d];
					const int nx2 = act.pos[i].first - dx[d];
					const int ny2 = act.pos[i].second - dy[d];
					if (nx < 0 || nx >= m || ny < 0 || ny >= n || board[nx][ny] != '.')
						continue;
					if (nx2 < 0 || nx2 >= m || ny2 < 0 || ny2 >= n || board[nx2][ny2] != '.')
						continue;
					bool bad = false;
					for (int j = 0; j < b; j++)
						if ((nx == act.pos[j].first && ny == act.pos[j].second)
							|| (nx2 == act.pos[j].first && ny2 == act.pos[j].second))
						{
							bad = true;
							break;
						}
					if (bad)
						continue;

					state nact = act;
					nact.pos[i].first = nx;
					nact.pos[i].second = ny;
					nact.normalize();
					if (vis.find(nact) != vis.end())
						continue;

					nact.stable();
					nact.dist = act.dist + 1;
					if (!nact.stab && !act.stab)
						continue;

					q.push(nact);
					vis.insert(nact);
					next:;
				}
		}

		cout << "Case #" << kase << ": ";
		if (q.empty())
			cout << -1;
		else
			cout << q.front().dist;
		cout << endl;
	}
	return 0;
}
