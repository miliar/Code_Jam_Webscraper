#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <algorithm>
using namespace std;
int tot,aa,n;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&tot);
	for(int i=1;i<=tot;i++)
	{
		int ans=0;
		int min=10000000;
		int to=0;
		scanf("%d",&n);
		for(int j=0;j<n;j++)
		{
			scanf("%d",&aa);
			ans=ans xor aa; 
			to+=aa;
			if(aa<min)min=aa;
		}
		if(ans!=0)
		{
			printf("Case #%d: NO\n",i);
		}else
		{
			printf("Case #%d: %d\n",i,to-min);
		}
	}
	return 0;
}
