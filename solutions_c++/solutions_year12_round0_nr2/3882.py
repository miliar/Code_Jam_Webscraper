#include<iostream>
#include<cstdio>
using namespace std;
#define MAX 110
int main()
{
int t,p,s,n;
int count,temp;
int a[MAX];
scanf("%d",&t);
for(int i=1;i<=t;i++)
{
	count=0;
	scanf("%d%d%d",&n,&s,&p);
	
	
	while(n--)
	{	
			
		scanf("%d",&temp);
	
		if(p==0) count++;
		else if( temp >= 3*p-2 )
		{
			count++;
		}
		else if( s>0 && p>1 && temp >= 3*p-4  ) 
		{
			s--;
			count++;
	
		} 

	}
printf("Case #%d: %d\n",i,count);
}
return 0;
}
