#include "stdio.h"
int a[2000];
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
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	int min,max;
	scanf("%d",&n);
	int i,j,k;
	int bnum;
	int count,kk;
	for(i=0;i<n;i++)
	{
		
		scanf("%d %d",&min,&max);
	
		count=0;
		int tenle=1;
		bnum=cal(min,tenle);
	//	printf("bum:%d,tenle:%d\n",bnum,tenle);
	
		for(k=min;k<max;k++)
		{	
			int ten=1;
			int temptenle=tenle*10;
			for(kk=min;kk<=max;kk++)
			{
				a[kk]=0;
			}
			for(j=0;j<bnum;j++)
			{
				ten=ten*10;
				temptenle=temptenle/10;
				int num=k%ten*temptenle+k/ten;
			
				if(num>k && num<=max && num>min)
				{
				//	printf("%d %d\n",k,num);
					if(a[num]==0)
					{	
						count++;
						a[num]=1;
					}
				
				}
				
			}
		}
		printf("Case #%d: %d\n",i+1,count);

	}
}