#include<stdio.h>
int main()
{
	int in,n;
	long long a,b;
	scanf("%d",&in);
	for(n=0;n<in;n++)
	{
		scanf("%lld %lld",&a,&b);
		a--;
		int c;
		c=(1<<a)-1;
		//printf("%d %d=%d\n",b,c,c&b);
		if((((1<<a)&b)!=0)&&((c&b)==c))
		{
			printf("Case #%d: ON\n",n+1);
		}
		else
			printf("Case #%d: OFF\n",n+1);
	}
}
