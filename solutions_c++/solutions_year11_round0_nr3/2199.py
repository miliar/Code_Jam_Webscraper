#include <stdio.h>
#include <iostream>
using namespace std;

int n;
int num;

int main()
{
	int cas,T;
	freopen("C-large.in","r",stdin);
	freopen("3.out","w",stdout);
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		scanf("%d",&n);
		int i,tmin,sum,tmp=0;
		tmin=10000000;sum=0;
		for(i=1;i<=n;++i)
		{
			scanf("%d",&num);
			sum+=num;
			tmp^=num;
			if(tmin>num) tmin=num;
		}
		if(tmp==0) 
			printf("Case #%d: %d\n",cas,sum-tmin);
		else
			printf("Case #%d: NO\n",cas);
	}


	return 0;
}