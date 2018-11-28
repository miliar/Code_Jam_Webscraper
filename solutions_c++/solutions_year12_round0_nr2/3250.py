#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int n,s,p;
	int count;
	scanf("%d", &count);
	int j = 1;
	while(count--)
	{
		printf("Case #%d: ",j++);
		scanf("%d%d%d",&n,&s,&p);		

		int lev1 = p * 3 - 2;
		int lev2 = lev1 - 2;
		int count1 = 0; 
		int count2 = 0;
		int num;
		for ( int i =0; i< n ; ++i)
		{
			scanf("%d",&num);
			if ( num >= lev1)
			{
				count1 ++;
			}
			else if ( num >= lev2)
			{
				count2 ++;
			}
		}
		if ( p == 0 )
		{
			printf("%d\n",n);
		}
		else if ( p == 1 )
		{
			printf("%d\n",count1);
		}
		else
		{
			int min = (count2 > s ? s:count2);
			printf("%d\n",count1 + min);
		}
	}
	return 0;
}