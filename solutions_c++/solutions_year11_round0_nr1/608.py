#include<iostream>
using namespace std;
int main()
{
	int T;
	freopen("A-large.in","r",stdin);
	freopen("hhh.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int n,num;
		char tt[10];
		scanf("%d",&n);
		int sum=0;
		int a1,a2;
		int b1,b2;
		b1=b2=1;
		a1=a2=0;
		for(int i=0;i<n;i++)
		{
			scanf("%s %d",tt,&num);
			if(!strcmp(tt,"O"))
			{
				int temp=abs(num-b1);
				temp-=a1;
				if(temp<0)temp=0;
				sum+=temp;
				b1=num;
				sum++;
				a2+=temp+1;
				a1=0;
			}
			else 
			{
				int temp=abs(num-b2);
				temp-=a2;
				a2=0;
				if(temp<0)temp=0;
				sum+=temp;
				b2=num;
				sum++;
				a1+=temp+1;
			}
		}
		printf("Case #%d: %d\n",t,sum);
	}


	return 0;
}