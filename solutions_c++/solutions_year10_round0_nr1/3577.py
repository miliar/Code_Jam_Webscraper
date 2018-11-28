#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main()
{
	int num,n,k;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	scanf("%d",&num);
	for(int i=0;i<num;i++)
	{
		scanf("%d %d",&n,&k);
		if((k+1)%(int)(pow(2.0,n)+0.1)==0)
		{
			printf("Case #%d: ON\n",i+1);
		}
		else 
		{
			printf("Case #%d: OFF\n",i+1);
		}
	}
}