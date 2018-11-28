#include<stdio.h>
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("test.out","w",stdout);
	int t,n,s,p,d,c,cnt,temp;
	scanf("%d",&t);
	for(c=1;c<=t;c++)
	{
		cnt=temp=0;
		printf("Case #%d: ",c);
		scanf("%d%d%d",&n,&s,&p);
		while(n--)
		{
			scanf("%d",&d);
			if(d>=3*p-2) cnt++;
			else if(d>=3*p-4)
			{
				if(d>0||p!=1) temp++;
			}
		}
		temp=temp<s?temp:s;
		printf("%d\n",cnt+temp);
	}
	return 0;
}