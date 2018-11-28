#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

int cl[2000500];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int tt, T;
	scanf("%d", &T);
	for (tt = 0; tt < T; ++tt)
	{
		int a, b;
		int i, j;
		scanf("%d%d", &a, &b);
		for (i = 10, j = 1; i <= 10000000 && a >= i; i *= 10, j++);
		int l = j;
		int m = i/10;
		int ans = 0;
		for (i = a; i <= b; ++i)
			cl[i] = 0;
		for (i = a; i <= b; ++i)
		{
			if (cl[i] == 0)
			{
				cl[i] = i;
				int cnt = 1;
				int u = i;
				for (j = 0; j < l - 1; ++j)
				{
					u = u/10 + u%10*m;
					if (a <= u && u <= b && cl[u] == 0)
					{
						cl[u] = i;
						cnt++;
					}
				}
//				printf("%d %d\n", i, cnt);
				ans += (cnt - 1)*cnt/2;
			}
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	return 0;
}