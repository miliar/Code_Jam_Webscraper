#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	long t,n,k,i,j,flag,c=1;
	char str[35];
	scanf("%ld",&t);
	while(t--)
	{
		scanf("%ld %ld",&n,&k);
		
		for(i=0;i<n;i++)
			str[i]='0';
		i=0;
		while(k)
		{
			str[i++]=k%2 + '0';
			k=k/2;
		}
		flag=0;
		for(j=0;j<n;j++)
		{
			if(str[j]=='0')
			{
				flag=1;
				break;
			}
		}
		if(flag)
			printf("Case #%ld: OFF\n",c);
		else
			printf("Case #%ld: ON\n",c);
		c++;
	}
	return 0;
}