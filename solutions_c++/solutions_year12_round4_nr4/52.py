#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#define clr(a) memset(a, 0, sizeof(a))

typedef long long ll;
typedef std::pair<int, int> pii;
#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}

char map[100][100];
int good[100][100];
ll hashmap[100][100];

int w,h;

void dfs(int a, int b)
{
	if (good[a][b])
		return;
	if (map[a][b] == '#')
		return;
	good[a][b] = 1;
	dfs(a, b - 1);
	dfs(a, b + 1);
	dfs(a - 1, b);
}


class state
{
public:
	char used[60][60];
	state()
	{
		clr(used);
	}
	state move(int x, int y)
	{
		state temp;
		for(int i = 0; i < w; i++)
			for(int j = 0; j < h; j++)
				if (used[i][j])
				{
					if (map[i + x][j + y] == '#')
						temp.used[i][j] = 1;
					else
						temp.used[i + x][j + y] = 1;
				}
		return temp;
	}
	bool good()	
	{
		for(int i = 0; i < w; i++)
			for(int j = 0; j < h; j++)
				if (used[i][j] && !::good[i][j])
					return false;
		return true;
	}
	ll hash()
	{
		ll ans = 0;
		for(int i = 0; i < w; i++)
			for(int j = 0; j < h; j++)
				if (used[i][j])
					ans ^= hashmap[i][j];
		return ans;
	}	
	int size()
	{
		int ans = 0;
		for(int i = 0; i < w; i++)
			for(int j = 0; j < h; j++)
				if (used[i][j])
					ans++;
		return ans;
	}
	void print()
	{
		for(int i = 0; i < w; i++)
		{
			for(int j = 0; j < h; j++)
			{
				if (map[i][j] == '#')
					printf("#");
				else
					printf("%c", used[i][j] ? '*' : '.');
			}
			printf("\n");
		}
		printf("\n");
	}
};

std::set<ll> used_states;

const int dx[] = {1, 0, 0};
const int dy[] = {0, 1, -1};

bool rec(state s)
{
	//s.print();
	if (!s.good())
		throw 42;
	if (s.size() == 1)
		return true;
	ll h = s.hash();
	if (used_states.find(h) != used_states.end())
		return false;
	used_states.insert(h);
	state s1 = s.move(1,0);
	if (s1.good() && s1.hash() != h)
	{
		for(int i = 0; i < w; i++)
			s1 = s1.move(0, 1);
		return rec(s1);
	}
	s1 = s.move(0,1);
	if (rec(s1))
		return true;
	s1 = s.move(0,-1);
	if (rec(s1))
		return true;
	return false;
}
		

void solve_map(int test_case)
{
	for(int i = 0; i < w; i++)
		for(int j = 0; j < h; j++)
		{
			good[i][j] = false;
		}
	for(int i = 0; i < w; i++)
		for(int j = 0; j < h; j++)
			if (map[i][j] == test_case + '0')
				dfs(i, j);
	state init;
	for(int i = 0; i < w; i++)
		for(int j = 0; j < h; j++)
			init.used[i][j] = (char) good[i][j];
	used_states.clear();
	int ans = rec(init);
	printf("%d: %d %s\n", test_case, init.size(), ans ? "Lucky" : "Unlucky");
}

void solve(int test_case)
{
	printf("Case #%d:\n", test_case);
	scanf("%d%d", &w, &h);
	int count = -1;
	for(int i = 0; i < w; i++)
	{
		scanf("%s", map[i]);
		for(int j = 0; j < h; j++)
			if (map[i][j] >= '0' && map[i][j] <= '9')
				count = std::max(count, map[i][j] - '0');
	}
	count++;
	for(int i = 0; i < count; i++)
		solve_map(i);

}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 0; i < 60; i++)
		for(int j = 0; j < 60; j++)
			hashmap[i][j] = (((ll)rand()) << 32) ^ rand();
	for(int i = 1; i <= n; i++)
		solve(i);
	
	return 0;
}
