#include<stdio.h>
int gcd(int a,int b)
{
	while((a%=b)&&(b%=a));
	return a+b;
}
main()
{
	int abc,ab,i,j,m,k,ans,pd,pg;
	long long n;
	freopen("LA.in","r",stdin);
	freopen("LA.out","w",stdout);
	scanf("%d",&abc);
	for(ab=1;ab<=abc;ab++)
	{
		scanf("%I64d %d %d",&n,&pd,&pg);
		if(pd!=0&&pg==0)printf("Case #%d: Broken\n",ab);
		else if(pd==0)
		{
			if(pg==0)printf("Case #%d: Possible\n",ab);
			else printf("Case #%d: Broken\n",ab);
		}
		else if((n<100)&&(100/gcd(100,pd))>n)printf("Case #%d: Broken\n",ab);
		else if(pd!=100&&pg==100)printf("Case #%d: Broken\n",ab);
		else printf("Case #%d: Possible\n",ab);
		/*if(pd!=100&&pg==100)printf("Case #%d: Broken\n",ab);
		else if(pd!=0&&pg==0)printf("Case #%d: Broken\n",ab);
		else printf("Case #%d: Possible\n",ab);*/
	}
}
