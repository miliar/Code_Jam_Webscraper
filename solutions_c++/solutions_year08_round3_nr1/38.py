#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <time.h>
#include <set>
using namespace std;

int a[1002];
bool cmp(int a, int b) {return a > b;}

int main()
{
	int i, k, l, n, p, c, ca = 0; __int64 ans, t;
	freopen("c:\\B.in", "r", stdin);
	freopen("c:\\test2.out", "w+", stdout);
	scanf("%d", &n);
	while(n--)
	{
		scanf("%d%d%d", &p, &k, &l);
		for(i = 1;i <= l; i++) scanf("%d", &a[i]);
		if(p*k < l) {printf("Impossible\n"); continue;}
		sort(a+1, a+l+1, cmp);
		c = 1;
		ans = 0;
		for(i = 1;i <= l;i++)
		{
			t = c; t *= a[i]; ans += t;
			if(i%k == 0) c++;
		}
		printf("Case #%d: %I64d\n", ++ca, ans);
	}
	return 0;
}