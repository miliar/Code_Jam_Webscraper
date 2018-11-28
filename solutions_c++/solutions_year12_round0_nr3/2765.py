#include<ctime>
#include<cstdio>
#include<vector>
#include<string>
#include<climits>
#include<cstdlib>
#include<cstddef>
#include<string.h>
#include<iostream>
#include<algorithm>
#define LL long long
#define _max(a, b) ((a) > (b) ? (a) : (b))
#define _min(a, b) ((a) < (b) ? (a) : (b))
using namespace std;

char s[13];
int len, a[11];
int main()
{
//*
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
//*/
	int t, l, r;
	cin>> t;
	for (int i = 1; i <= t; i++)
	{
		int ans = 0;
		scanf("%d%d", &l, &r);
		for (int x = l; x <= r; x++)
		{
			int n = 0;
			sprintf(s, "%d", x);
			len = strlen(s);
			for (int j = 0; j < len; j++)
			{
				char c = s[len - 1];
				memmove(s + 1, s, (len - 1) * sizeof(char));
				s[0] = c;
				int y = atoi(s);
				if (y > x && y <= r) a[++n] = y;
			}
			sort(a + 1, a + 1 + n);
			ans += unique(a + 1, a + 1 + n) - a - 1;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
