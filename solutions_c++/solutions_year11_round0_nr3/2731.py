#include<cstdio>
int main()
{
	int i,j,sum,testing=1,num,a[1000]={0};
	int test;
	scanf("%d",&test);
	while(test--)
	{
		int temp,t,flag=0,max=0;
		scanf("%d",&num);
		t=num;
		for(i=0;i<num;i++)
			scanf("%d",&a[i]);
		num=2<<(num-1);
		for(i=1;i<num;i++)
		{
			int sum3=0,sum1=0,sum2=0;
			temp=0;
			for(j=0;j<t;j++)
			{
				if((i & (1<<j)))
				{
					sum1+=a[j];
					sum3=sum3^a[j];
				}
				else
					sum2=sum2^a[j];
			}
			if(sum3==sum2 && sum2!=0)
			{
				flag=1;
				if(sum1>max)
					max=sum1;
			}
		}
		if(flag==1)
			printf("Case #%d: %d\n",testing++,max);
		else
			printf("Case #%d: NO\n",testing++);
	}
	return 0;
}