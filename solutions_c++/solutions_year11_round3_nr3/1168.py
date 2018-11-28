#include <iostream>
#include <stdio.h>
#include <memory.h>
using namespace std;

int num[11000];

int main()
{
	freopen("111.in","r",stdin);
	freopen("111.out","w",stdout);
	int t,n,i,j,l,h,ca=0;
	scanf("%d",&t);
	while(t--)
	{
		++ca;
		scanf("%d%d%d",&n,&l,&h);
		for(i=1;i<=n;i++) scanf("%d",&num[i]);
		for(i=l;i<=h;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(num[j]%i!=0&&i%num[j]!=0) break;
			}
			if(j>n) break;
		}
		printf("Case #%d: ",ca);
		if(i>h) printf("NO\n");
		else printf("%d\n",i);
	}
	return 0;
}
