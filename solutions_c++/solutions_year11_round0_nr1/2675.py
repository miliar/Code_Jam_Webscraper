#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;
struct MAN
{
	string c;
	int b;
}a[105];
int main()
{
	int t;
    freopen("2.txt","w",stdout);
	scanf("%d",&t);
	{
		int jj=1;
		while(t--)
		{
			int n,i;
			scanf("%d",&n);
			for(i=0;i<n;i++)
			{
				cin>>a[i].c;
				scanf("%d",&a[i].b);
			}
			int time1=a[0].b,time=a[0].b;		
			int step1=1,step2=1;
			if(a[0].c=="O")
				step1=a[0].b;
			if(a[0].c=="B")
				step2=a[0].b;


			int tt=0;
			for(i=1;i<n;i++)
			{
				if(a[i-1].c==a[i].c)
				{
					if(a[i].c=="O")
					{
						time1+=abs(a[i].b-step1)+1;
						time+=abs(a[i].b-step1)+1;
						step1=a[i].b;
					}
					if(a[i].c=="B")
					{
						time1+=abs(a[i].b-step2)+1;
						time+=abs(a[i].b-step2)+1;
						step2=a[i].b;
						
					}
				}
				else
				{
					int step;
					if(a[i].c=="B")
						step=step2;
					else
						step=step1;
					if(time1<abs(a[i].b-step))
					{
						time+=abs(a[i].b-step)-time1+1;
						time1=abs(a[i].b-step)-time1+1;
						
					}
					else
					{
						time++;
						time1=1;
					}
					if(a[i].c=="O")
						step1=a[i].b;
					else
						step2=a[i].b;
				}
			}
			printf("Case #%d: ",jj++);
			printf("%d\n",time);
		}
	}
	
	return 0;
}
