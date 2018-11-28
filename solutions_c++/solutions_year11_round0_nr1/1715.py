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

int t, n, num;
int pos1, pos2, time, add;
int last;
char r;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		scanf("%d%*c", &n);
		pos1 = pos2 = 1;
		time = add = 0;
		for (int i = 0; i < n; i++)
		{
			int cnt = 0;
			scanf("%c%d%*c", &r, &num);
			if (i == 0)
			{
				last = (r == 'O') ? 1 : 2;
			}
			if (r == 'O')
			{
				cnt =  abs(pos1 - num) + 1;
				if (last == 2)
				{
					if (cnt <= add)
					{
						cnt = add + 1;
					}
					time += add;
					add = cnt - add;
				}
				else
				{
					add += cnt;
				}
				pos1 = num;
				last = 1;
			}
			else
			{
				cnt = abs(pos2 - num) + 1;
				if (last == 1)
				{
					if (cnt <= add)
					{
						cnt = add + 1;
					}
					time += add;
					add = cnt - add;
				}
				else
				{
					add += cnt;
				}
				pos2 = num;
				last = 2;
			}
		}
		printf("Case #%d: %d\n", q + 1, time + add);
	}
	return 0;
}