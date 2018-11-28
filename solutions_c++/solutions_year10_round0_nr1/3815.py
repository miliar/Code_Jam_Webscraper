#include<stdio.h>

int is_on(int n,int k)
{
	int i;
	for(i=0;i<n;i++)
	{
		if(k%2==0)
			return 0;
		k = k /2;
	}
	return 1;
}

int main(void)
{
	int t,k,n,i;

	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%d",&t);

	for(i=1;i<=t;i++)
	{
		scanf("%d %d",&n,&k);

		if(is_on(n,k)==1)
		{
			printf("Case #%d: ON\n",i);
		}
		else
		{
			printf("Case #%d: OFF\n",i);	
		}
	}
	
	return 0;		
}