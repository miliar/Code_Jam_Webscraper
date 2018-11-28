#include <iostream>
#include <cmath>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	scanf("%d",&T);
	int cas = 0;
	while(T--)
	{
		int N;
		scanf("%d",&N);
		int mm = 999999999;
		int sum = 0;
		int xo = 0;
		int x;
		for(int i = 0 ;i< N;i++)
		{
			scanf("%d",&x);
			xo^=x;
			sum+=x;
			mm = min(mm,x);
		}
		++cas;
		if(xo != 0) printf("Case #%d: NO\n",cas);
		else printf("Case #%d: %d\n",cas,sum-mm);
	}
	return 0;
}
