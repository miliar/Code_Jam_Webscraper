#include<cstdio>
#include<cstdlib>
#include<climits>
#include<iostream>
#include<memory.h>
#include<algorithm>
#define LL long long
#define _min(a,b) ((a) < (b) ? (a) : (b))
#define _max(a,b) ((a) > (b) ? (a) : (b))
using namespace std;

int T, n, s, q;
char c;
int main(){
/*
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
//*/
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &n);
		int x = 1, y = 1, tl1 = 0, tl2 = 0, ans = 0;
		for (int i = 1; i <= n; i++)
		{
			cin>> c>> q;
			if (c == 'O')
			{
				s = abs(q - x);
				s = _max(0, s - tl1);
				++s;
				tl1 = 0, tl2 += s;
				ans += s, x = q;
			}
			else
			{
				s = abs(q - y);
				s = _max(0, s - tl2);
				++s;
				tl2 = 0, tl1 += s;
				ans += s, y = q;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
