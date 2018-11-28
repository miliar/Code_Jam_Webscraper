#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	int t,i,d,n,k,ans;
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&t);
	for(d = 0; d < t; d++)
	{
		scanf("%d%d",&n,&k);
		for(ans = 1,i = 0; i < n; i++)
		{
			ans = ans*2;
		}
		k = k%ans;
		if(k != ans-1) printf("Case #%d: OFF\n",d+1);
		else
		{
			printf("Case #%d: ON\n",d+1);
		}
	}
	return 0;
}