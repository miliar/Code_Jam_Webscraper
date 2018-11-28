#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

#ifndef ONLINE_JUDGE
int poj();
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	poj();
	return 0;
}
#define main poj
#endif

#define clr(x) memset(x, 0, sizeof(x))
#define MAXINT 200000000
#define EPS 0.00000001
#define MAXN 300

int n, result;
string data[100];

bool can(int v, int lef)
{
	int i;
	for (i = n - 1; i > lef - 1; i--)
		if (data[v][i] == '1')
			return 0;
	return 1;
}

int main()
{
	int tcase, tno, i, j, k;
	char buf[100];
	string tt;
	
	scanf("%d", &tcase);
	for (tno = 1; tno <= tcase; tno++)
	{
		result = 0;
		scanf("%d", &n);
		for (i = 1; i <= n; i++)
		{
			scanf("%s", buf);
			data[i] = buf;
		}
		for (i = 1; i <= n; i++)
		{
			if (!can(i, i))
			{
				for (j = i + 1; j <= n; j++)
				{
					if (can(j, i))
					{
						result += j - i;
						break;
					}
				}
				tt = data[j];
				for (k = j; k > i; k--)
					data[k] = data[k - 1];
				data[i] = tt;
				
			}/*
			for (j = 1; j <= n; j++)
				printf("  %s\n", data[j].c_str());
				*/
		}
		printf("Case #%d: %d\n", tno, result);
	}
	
	return 0;
}
