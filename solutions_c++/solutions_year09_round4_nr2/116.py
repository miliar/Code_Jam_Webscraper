#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <string>

using namespace std;

typedef pair<int, int> pos;
typedef vector<string> cave;
typedef pair<cave, pos> state;

cave m;
map<state, int> st;

int r, c, f;

void dig(queue<state>& q, state cur, int dx, int ct)
{
	int x = cur.second.first + dx;
	if (x < 0 || c-1 < x)
		return;

	if (cur.first[cur.second.second][x] == '.' && cur.first[cur.second.second+1][x] == '#')
	{
		cur.first[cur.second.second+1][x] = '.';

		map<state, int>::iterator it = st.find(cur);
		if (it == st.end() || it->second > ct + 1)
		{
			q.push(cur);
			st[cur] = ct + 1;
		}
	}
}

void move(queue<state>& q, state cur, int dx, int ct)
{
	int x = cur.second.first + dx;

	if (0 <= x && x < c && cur.first[cur.second.second][x] == '.')
	{
		int deep = 0;
		while(cur.second.second+deep+1 < r && cur.first[cur.second.second+deep+1][x] == '.') ++deep;
		if (deep > f)
			return;

		cur.second.first = x;
		cur.second.second += deep;
		map<state, int>::iterator it = st.find(cur);
		if (it == st.end() || it->second > ct)
		{
			q.push(cur);
			st[cur] = ct;
		}
	}
}

int solve()
{
	int ret = -1;

	queue<state> q;
	state init = make_pair(m, make_pair(0, 0));
	q.push(init);
	st[init] = 0;

	while(!q.empty())
	{
		state cur = q.front();
		q.pop();

		int ct = st[cur];

		if (ret != -1 && ret <= ct)
			continue;

		if (cur.second.second == r-1 && (ret == -1 || ret > ct))
		{
			ret = ct;
			continue;
		}

		dig(q, cur, -1, ct);
		dig(q, cur, 1, ct);
		move(q, cur, -1, ct);
		move(q, cur, 1, ct);
	}

	return ret;
}

int main()
{
	int z;
	scanf("%d", &z);
	for(int i = 1; i <= z; ++i)
	{
		scanf("%d%d%d", &r, &c, &f);
		char inp[1024] = {0};
		m.clear();
		st.clear();
		for(int j = 0; j < r; ++j)
		{
			scanf("%s", inp);
			m.push_back(inp);
		}
		int res = solve();
		if (res == -1)
			printf("Case #%d: No\n", i);
		else
			printf("Case #%d: Yes %d\n", i, res);
	}
}