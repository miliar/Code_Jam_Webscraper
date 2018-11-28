#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int t, c, d, n, len;
char comb[130][130];
int op[130][130];
char stack[1000];
string s;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		memset(comb, 0, sizeof(comb));
		memset(op, 0, sizeof(op));
		len = 0;
		scanf("%d", &c);
		for (int i = 0; i < c; i++)
		{
			char x, y, z;
			scanf("%*c%c%c%c", &x, &y, &z);
			comb[x][y] = comb[y][x] = z;
		}
		scanf("%d", &d);
		for (int i = 0; i < d; i++)
		{
			char x, y, z;
			scanf("%*c%c%c", &x, &y, &z);
			op[x][y] = op[y][x] = 1;
		}
		scanf("%d%*c", &n);
		cin >> s;
		for (int i = 0; i < n; i++)
		{
			stack[len++] = s[i];
			if (len == 1)
			{
				continue;
			}
			if (comb[stack[len - 1]][stack[len - 2]] > 0)
			{
				stack[len - 2] = comb[stack[len - 1]][stack[len - 2]];
				len--;
				continue;
			}
			for (int i = 0; i < len - 1; i++)
			{
				if (op[stack[i]][stack[len - 1]] > 0)
				{
					len = 0;
					break;
				}
			}
		}
		printf("Case #%d: [", q + 1);
		for (int i = 0; i < len; i++)
		{
			printf("%c", stack[i]);
			if (i < len - 1)
			{
				printf(", ");
			}
		}
		printf("]\n");
	}
	return 0;
}