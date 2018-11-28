#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int t;
int n, m;
char maps[100][100];
bool ans;

void init()
{
	scanf("%d%d\n", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%s", maps[i]);
}

void work()
{
	ans = true;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (maps[i][j] == '#')
			{
				if (i + 1 < n && j + 1 < m && maps[i + 1][j] == '#' && maps[i][j + 1] == '#' && maps[i + 1][j + 1] == '#')
				{
					maps[i][j] = '/';
					maps[i][j + 1] = '\\';
					maps[i + 1][j] = '\\';
					maps[i + 1][j + 1] = '/';
				}
				else
					ans = false;
			}
}
  


int main()
{
	freopen("A-large.in" ,"r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);
		init();
		work();
		if (!ans)
			printf("Impossible\n");
		else
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < m; j++)
					printf("%c", maps[i][j]);
				printf("\n");
			}
	}
	return 0;
}