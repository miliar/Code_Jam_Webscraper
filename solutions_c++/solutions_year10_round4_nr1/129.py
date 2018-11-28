#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#define clr(a) memset(a, 0, sizeof(a))

#define DEBUG 0

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}


int ar[1000][1000];
std::vector<std::pair<int, int>  >ind;
int t[4];

bool check(int x, int y)
{
	for(int i = -200; i <= 0; i++)
		for(int j = -200; j <= 0; j++)
		{
			t[0] = ar[i+x][j+y];
			t[1] = ar[x-i][y+j];
			t[2] = ar[x+i][y-j];
			t[3] = ar[x-i][y-j];
			std::sort(t, t+4);
			int p = 0;
			while(p < 4 && t[p] == -1)
				p++;
			if (p < 4 && t[p] != t[3])
				return false;
		}
	return true;
}

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int n;
	scanf("%d", &n);
	n--;
	memset(ar, -1, sizeof(ar));
	for(int i = -n; i <= n; i++)
	{
		int l = n - abs(i);
		for(int j = -l; j <= l; j+=2)		
		{
			scanf("%d", &ar[i+500][j+500]);
		}
	}
	dbg("\n");
	for(int i = -n; i <= n; i++)
	{
		for(int j = -n; j <= n; j++)
			dbg("%3d ", ar[i+500][j+500]);
		dbg("\n");
	}
	int ans = 200;

	//for(int i = -60; i <= 60; i++)
	//	for(int j = -60; j <= 60; j++)
	for(int l = 0; l < ind.size(); l++)
		{
			int i = ind[l].first;
			int j = ind[l].second;
			if (std::max(abs(i-j), abs(i+j)) >= ans)
				continue;
			if (!check(500+i, 500+j))
				continue;
			ans = std::max(abs(i-j), abs(i+j));
		
		}
	n++;
	printf("%d\n", (n+ans)*(n+ans) - n*n);
}

bool cmp(std::pair<int, int> p1, std::pair<int, int> p2)
{
	int a = std::max(abs(p1.first + p1.second), abs(p1.first - p1.second));
	int b = std::max(abs(p2.first + p2.second), abs(p2.first - p2.second));
	return a < b;
}

int main()
{
	for(int i = -60; i <= 60; i++)
		for(int j = -60; j <= 60; j++)
			ind.push_back(std::make_pair(i, j));
	std::sort(ind.begin(), ind.end(), cmp);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
