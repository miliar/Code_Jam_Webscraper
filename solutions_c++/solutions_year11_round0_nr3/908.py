#include <stdio.h>
#include <algorithm>
using namespace std;
int T,n;
int ar[1009];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int test=1;test<=T;test++)
	{
		scanf("%d",&n);
		int S = 0,GS=0;
		int Min = 1000000009;
		for (int i=0;i<n;i++)
		{
			scanf("%d",&ar[i]);
			S= S ^ ar[i];
			GS+=ar[i];
			Min = min(Min,ar[i]);
		}
		printf("Case #%d: ",test);
		if (S != 0)
		{
			printf("NO\n");
			continue;
		}
		printf("%d\n",GS-Min);
	}
	return 0;
}