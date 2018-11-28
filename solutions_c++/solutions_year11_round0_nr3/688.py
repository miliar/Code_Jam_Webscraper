#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int max(int a,int b)
{
	return (a>b)?a:b;
}

//int hehe[1048576];
//int hehe2[1048576];

int main()
{
	int pos;
	char cc;
	int cas,asd;
	int n,ins,i,total,val,j;
	int sum;

	int max = 1048576,large;
	
	freopen("C-large.in","r",stdin);

	freopen("C-large.out","w",stdout);

	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{


		scanf("%d",&n);
		max= 10000000;
		total =sum=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&val);
			if(val < max)
				max = val;
			total = total ^ val;
			sum += val;
		}
		printf("Case #%d: ",asd+1);
		if(total!=0)
			printf("NO\n");
		else
			printf("%d\n",sum - max);
	}
	return 0;
}
