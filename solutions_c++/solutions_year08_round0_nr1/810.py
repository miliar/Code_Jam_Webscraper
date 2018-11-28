#include<stdio.h>
#include<string.h>
char a[101][101],b[1100][11001];
int main()
{
	freopen("1.txt","w",stdout);
	int cas,i,j,k,times,max,num1,num2,cass=1;
	scanf("%d",&cas);
	
	while(cas--)
	{
		times=0;
		scanf("%d",&num1);
		getchar();
		for( i = 0 ; i < num1 ; i ++ )
		{
			gets(a[i]);
		}
		scanf("%d",&num2);
		getchar();
		for( i = 0 ; i < num2 ; i ++ )
		{
			gets(b[i]);
		}
		k=0;max=0;
		while(1)
		{
			for( i = 0 ; i< num1 ; i ++ )
			{
				for( j = k ; j < num2 ; j ++ )
				{
					if(strcmp(a[i],b[j])==0)
						break;
				}
				if(j>max)
					max=j;
				if(j==num2)
					break;
			}
			k=max;
			if(j==num2)
				break;
			times++;
		}
		printf("Case #%d: ",cass);cass++;
		printf("%d\n",times);
	}
	return 0;
}