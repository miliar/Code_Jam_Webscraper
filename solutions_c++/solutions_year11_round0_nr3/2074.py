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

int T, a[1111], n;
int main(){
/*
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
//*/
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &n);
		int s = 0, m = INT_MAX, x = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
			x ^= a[i], s += a[i];
			m = _min(m, a[i]);
		}
		printf("Case #%d: ", t);
		if (x) puts("NO");else printf("%d\n", s - m);
	}
	return 0;
}
