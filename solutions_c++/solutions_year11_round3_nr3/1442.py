#include<iostream>
using namespace std;
#include<stdio.h>
#define S 100

int lcmul(int a,int b,int m)
{
	if(a*m%b==0)
		return a*m;
	return lcmul(a,b,m+1);
}

main()
{//int x,b,l;
	int l,h,n,i,lcm,j,k,num,flag;
	int a[S];
int t,ic=1;
scanf("%d\n",&t);
while(t--)
{
	lcm=1;
	printf("Case #%d: ",ic++);
	
	scanf("%d%d%d",&n,&l,&h);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
		lcm=lcmul(lcm,a[i],1);
	}
	flag=2;
	for(k=l;k<=h;k++)
	{
		if(lcm%k==0 || k%lcm==0)
		{	flag=0;
			for(i=0;i<n;i++)
			{
				if(a[i]%k==0 || k%a[i]==0)
				{
					continue;
				}
				else
				{
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				printf("%d\n",k);
				break;
			}
		}
	}
	if(flag==1 || flag==2)
		printf("NO\n");	
}
}

