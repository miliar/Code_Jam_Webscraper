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

int move[10000][2];
int in[10000];
int prev[10000];
bool use[10000];
bool use2[10000];

char map[100][101];
int n,m;

int code(int x, int y)
{
	x = (x + n) % n;
	y = (y + m) % m;
	return x * m + y;
}

class set
{
public:
	int p[10000];
	void clear()
	{
		for(int i = 0; i < 10000; i++)
			p[i] = i;
	}
	int find(int x)
	{
		if (x != p[x])
			p[x] = find(p[x]);
		return p[x];
	}
	void join(int a, int b)
	{
		a = find(a); b = find(b);
		p[a] = b;
	}
} ss;

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; i++)
		scanf("%s", map[i]);
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
		{
			if (map[i][j] == '-')
			{
				move[code(i,j)][0] = code(i, j+1);
				move[code(i,j)][1] = code(i, j-1);
			}
			if (map[i][j] == '|')
			{
				move[code(i,j)][0] = code(i+1, j);
				move[code(i,j)][1] = code(i-1, j);
			}
			if (map[i][j] == '\\')
			{
				move[code(i,j)][0] = code(i+1, j+1);
				move[code(i,j)][1] = code(i-1, j-1);
			}
			if (map[i][j] == '/')
			{
				move[code(i,j)][0] = code(i-1, j+1);
				move[code(i,j)][1] = code(i+1, j-1);
			}
		}
	bool f = 1;
	n *= m;
	clr(in); clr(prev); clr(use); clr(use2);
	for(int i = 0; i < n; i++)
	{
		in[move[i][0]] ++;
		in[move[i][1]] ++;
	}
	while(f)
	{
		f = 0;
		for(int i = 0; i < n; i++)
		{		
			int u = move[i][0], v = move[i][1];
			if (!use[u] && !use2[i] && in[u] == 1)
			{
				use[u] = 1;
				in[u] --;
				in[v] --;
				use2[i] = 1;
				f = 1;
			}
			if (!use[v] && !use2[i] && in[v] == 1)
			{
				use[v] = 1;
				in[v] --;
				in[u] --;
				use2[i] = 1;
				f = 1;
			}
		}
	}
	int ans = 1;
	ss.clear();
/*	printf("\n");
	for(int i = 0; i < n; i++)
		printf("%d %d\n", use[i], in[i]);*/

	for(int i = 0; i < n; i++)
	{
		if (use[i])
			continue;
		if (in[i] == 0)
		{
			printf("0\n");
			return;
		}
	}
	for(int i = 0; i < n; i++)
	{
		if (use2[i])
			continue;
		if (ss.find(move[i][0]) == ss.find(move[i][1]))
			ans = (ans * 2) % 1000003;
		else
			ss.join((move[i][0]), move[i][1]);
	}
	printf("%d\n", ans);
}



int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
