#include <cstdio>
#include <cstring>
#include <cmath>

#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>

using namespace std;


int nt, n, m, K;

char s[100][100];
char ss[100][100];
char sss[100][100];

struct State
{
	vector< pair<int, int> > boxes;

	bool operator<(const State &s) const
	{
		return boxes < s.boxes;
	}

	void prep()
	{
		sort(boxes.begin(), boxes.end());
	}

	void clear()
	{
		boxes.clear();
	}

	void add(int x, int y)
	{
		boxes.push_back(make_pair(x, y));
	}

	bool finish()
	{
		for(int i = 0; i < boxes.size(); i++)
		{
			int x = boxes[i].first;
			int y = boxes[i].second;

			if (s[x][y] == 'x') continue;
			return false;
		}

		return true;
	}

	int rec(int x, int y)
	{
		if (x < 0 || y < 0 || x >= n || y >= m || sss[x][y] != 'o') return 0;
		sss[x][y] = '.';
		int res = 1;
		res += rec(x - 1, y);
		res += rec(x + 1, y);
		res += rec(x, y + 1);
		res += rec(x, y - 1);
		return res;
	}

	bool stable()
	{
		for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++) sss[i][j] = '.';

		for(int i = 0; i < K; i++)
		{
			int x = boxes[i].first;
			int y = boxes[i].second;
			sss[x][y] = 'o';
		}
		
		for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
		if (sss[i][j] == 'o')
		{
			if (rec(i, j) == K) return true;
			return false;
		}
		return true;
	}

} init;

queue<State> Q;
map<State, int> S;

void freeMove(State now)
{
    State ns;
	
	for(int i = 0; i < n; i++)
	for(int j = 0; j < m; j++) ss[i][j] = '.';

	for(int i = 0; i < K; i++)
	{
		int x = now.boxes[i].first;
		int y = now.boxes[i].second;
		ss[x][y] = 'o';
	}


	for(int i = 0; i < K; i++)
	{
		int x = now.boxes[i].first;
		int y = now.boxes[i].second;

		// RL

		if (y > 0 && s[x][y - 1] != '#' && ss[x][y - 1] == '.' && y + 1 < m && s[x][y + 1] != '#' && ss[x][y + 1] == '.')
		{
			ns = now;
			ns.boxes[i].second++;
			ns.prep();
			if (!S.count(ns)) { S[ns] = S[now] + 1; Q.push(ns); }

			ns = now;
			ns.boxes[i].second--;
			ns.prep();
			if (!S.count(ns)) { S[ns] = S[now] + 1; Q.push(ns); }
		}                                                 

		// UD

		if (x > 0 && s[x - 1][y] != '#' && ss[x - 1][y] == '.' && x + 1 < n && s[x + 1][y] != '#' && ss[x + 1][y] == '.')
		{
			ns = now;
			ns.boxes[i].first++;
			ns.prep();
			if (!S.count(ns)) { S[ns] = S[now] + 1; Q.push(ns); }

			ns = now;
			ns.boxes[i].first--;
			ns.prep();
			if (!S.count(ns)) { S[ns] = S[now] + 1; Q.push(ns); }
		}
	}
}

void stableMove(State now)
{
    State ns;
	
	for(int i = 0; i < n; i++)
	for(int j = 0; j < m; j++) ss[i][j] = '.';

	for(int i = 0; i < K; i++)
	{
		int x = now.boxes[i].first;
		int y = now.boxes[i].second;
		ss[x][y] = 'o';
	}


	for(int i = 0; i < K; i++)
	{
		int x = now.boxes[i].first;
		int y = now.boxes[i].second;

		// RL

		if (y > 0 && s[x][y - 1] != '#' && ss[x][y - 1] == '.' && y + 1 < m && s[x][y + 1] != '#' && ss[x][y + 1] == '.')
		{
			ns = now;
			ns.boxes[i].second++;
			ns.prep();
			if (ns.stable() && !S.count(ns)) { S[ns] = S[now] + 1; Q.push(ns); }

			ns = now;
			ns.boxes[i].second--;
			ns.prep();
			if (ns.stable() && !S.count(ns)) { S[ns] = S[now] + 1; Q.push(ns); }
		}

		// UD

		if (x > 0 && s[x - 1][y] != '#' && ss[x - 1][y] == '.' && x + 1 < n && s[x + 1][y] != '#' && ss[x + 1][y] == '.')
		{
			ns = now;
			ns.boxes[i].first++;
			ns.prep();
			if (ns.stable() && !S.count(ns)) { S[ns] = S[now] + 1; Q.push(ns); }

			ns = now;
			ns.boxes[i].first--;
			ns.prep();
			if (ns.stable() && !S.count(ns)) { S[ns] = S[now] + 1; Q.push(ns); }
		}
	}
}

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d %d", &n, &m);

		for(int i = 0; i < n; i++) scanf("%s", s[i]);

		init.clear();

		for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
		if (s[i][j] == 'o' || s[i][j] == 'w')
		{
			init.add(i, j);
			if (s[i][j] == 'o') s[i][j] = '.';
			if (s[i][j] == 'w') s[i][j] = 'x';
		}

		K = init.boxes.size();

		init.prep();

		S.clear();
		//Q.clear();
		while(!Q.empty()) Q.pop();

		S[init] = 0;
		Q.push(init);

		bool ok = false;

		while(!Q.empty())
		{
			State now = Q.front();
			Q.pop();

			if (now.finish())
			{
				printf("%d\n", S[now]);
				ok = true;
				break;
			}

			if (now.stable()) freeMove(now); else stableMove(now);
		}

		if (!ok) puts("-1");
	}

	return 0;	
}