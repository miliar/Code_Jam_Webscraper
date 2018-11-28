#include "stdio.h"
//int a[2000005];
int cal(int num,int & tenle)
{
	int cou=1;
	while(num/10>0)
	{
		cou++;
		num=num/10;
		tenle*=10;
	}
	return cou;
}
int overlap(int num,int cou)
{
	int i,j;

	for(i=2;i<=cou/2;i++)
	{
		if(cou%i==0)
		{
			int a=1;
			int temp=1;
			for(j=1;j<=i;j++)
			{
				temp=temp*10;
			}
			a=num%temp;
			int b=a;
			for(j=1;j<cou/i;j++)
			{
				a=a*temp+b;
			}
			if(a==num)
			{
				return cou/i;
			}
		}
	}
	return 0;
   
}

int main()
{
	freopen("input1.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int n;
	int min,max;
	scanf("%d",&n);
	int i,j,k,kk;
	int bnum;
	int count;
	for(i=0;i<n;i++)
	{
		
		scanf("%d %d",&min,&max);

		//printf("%d\n",overlap(min,9));
		//printf("%d\n",overlap(max,9));

	
		count=0;
		int tenle=1;
		bnum=cal(min,tenle);
		//printf("bum:%d,tenle:%d\n",bnum,tenle);

		for(k=min;k<max;k++)
		{	
			int ten=1;
			int temptenle=tenle*10;
			int over=overlap(k,bnum);
			int tempov=0;
			for(j=0;j<bnum;j++)
			{
				ten=ten*10;
				temptenle=temptenle/10;
				int num=k%ten*temptenle+k/ten;
			
				if(num>k && num<=max && num>min)
				{
				//	printf("%d %d\n",k,num);
						
						count++;
					if(overlap>0)
					{
						tempov++;
					}
				}
				
			}
			if(over>0)
			{
				count=count-tempov/over*(over-1);
			}
		}
		
		printf("Case #%d: %d\n",i+1,count);
	}
}