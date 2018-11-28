#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<cstdlib>
int main()
{
	int k,T,min,x,i,s,sum,n;
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A.txt","w",stdout);
    scanf("%d",&T);
	for(k=1;k<=T;k++)
	{
		scanf("%d",&n);
		sum=0;min=1000010;s=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&x);
			s+=x;
		    if(x<min) min=x;
			sum=sum^x;
			
		}
		if(sum!=0) printf("Case #%d: NO\n",k);
		else printf("Case #%d: %d\n",k,s-min);
	}
   return 0;
}