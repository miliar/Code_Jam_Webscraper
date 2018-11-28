#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
	freopen("ans.txt","w",stdout);
	int n, t, i, a;
	int cas = 1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		int cnt = 0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a);
			if(a!=i) cnt++;
		}
		printf("Case #%d: %.6lf\n",cas++,cnt+0.0);
	}
	return 0;
}