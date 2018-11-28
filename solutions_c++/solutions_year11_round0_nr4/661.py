#include <iostream>
#include <stdio.h>
#include <memory.h>
using namespace std;

int main()
{
	freopen("44444.in","r",stdin);
	freopen("44444.out","w",stdout);
	int t,n,i,ca=0,x;
	double ans;
	scanf("%d",&t);
	while(t--)
	{
		++ca;
		scanf("%d",&n);
		ans=0.0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&x);
			if(x!=i) ans+=1.0;
		}
		printf("Case #%d: %.6lf\n",ca,ans);
	}
	return 0;
}
