#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int Min(int a, int b)
{
	return a<b?a:b;
}
int main()
{
	freopen("ans.txt","w",stdout);
	int n, t, i, a, ans;
	int cas = 1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		int cnt = 100000000, sum = 0;
		scanf("%d",&ans);
		sum += ans;
		cnt = Min(cnt, ans);
		for(i=2;i<=n;i++)
		{
			scanf("%d",&a);
			sum += a;
			cnt = Min(cnt, a);
			ans ^= a;
		}
		if(ans != 0) printf("Case #%d: NO\n",cas++);
		else printf("Case #%d: %d\n",cas++,sum-cnt);
	}
	return 0;
}