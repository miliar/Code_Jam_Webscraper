#include<cstdio>
#include<vector>
#include<cstdlib>
#include<climits>
#include<iostream>
#include<memory.h>
#include<algorithm>
#define LL long long
#define _min(a, b) ((a) < (b) ? (a) : (b))
#define _max(a, b) ((a) > (b) ? (a) : (b))
using namespace std;

int tt, a, b, x;
LL n;
int main()
{
//*
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
//*/
	scanf("%d", &tt);
	for (int t = 1; t <= tt; t++)
	{
		x = 0;
		cin>> n>> a>> b;
		if (a == 0)
		{
			if (b < 100) printf("Case #%d: Possible\n", t);else printf("Case #%d: Broken\n", t);
			continue;
		}
		for (int i = 1; i <= n; i++) if ((i * a) % 100 == 0)
		{
			x = i * a / 100;
			break;
		}
		if (!x || !b || a < 100 && b == 100 || a == 100 && b == 0)
		{
			printf("Case #%d: Broken\n", t);
			continue;
		}
		printf("Case #%d: Possible\n", t);
	}
	return 0;
}
