#include <stdafx.h>
#include <stdio.h>

const long maxn=10005;
long a[maxn];
long lower,upper,q,n,test,t,k,choice;

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	scanf("%ld",&t);
	for (test=1;test<=t;test++)
	{
		scanf("%ld%ld%ld",&n,&lower,&upper);
		for (q=1;q<=n;q++)
			scanf("%ld",&a[q]);
		bool found=false;
		for (choice=lower;choice<=upper;choice++)
		{
			bool norm=true;
			for (k=1;k<=n;k++)
				if ((choice % a[k]!=0)&&(a[k] % choice!=0))
				{
					norm=false;
					break;
				}
			if (norm==true)
			{
				found=true;
				break;
			}
		}

		printf("Case #%ld: ",test);
		if (found==false)
			printf("NO\n");
		else printf("%ld\n",choice);
	}
}