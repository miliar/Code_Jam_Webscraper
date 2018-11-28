#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
using namespace std;

int main()
{
	freopen("example1.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	
	for(int z=1;z<=t;++z)
	{
		int n,s,p;
		scanf("%d%d%d",&n,&s,&p);
		
		int a[1001];
		for(int i=0;i<n;++i)scanf("%d",&a[i]);
            
		
		sort(a,a+n);
		
		
		int count=0;
		printf("Case #%d: ",z);
		for(int i=0;i<n;++i)
		{
			if(count>=s)break;
			if(a[i]!=0)
			{
			     int x=a[i];
			    
			     if((x+3)%3==0)if(((x+3)/3)>=p){++count;a[i]=-1;continue;}
			     if((x+4)%3==0)if(((x+4)/3)>=p){++count;a[i]=-1;continue;}
			     if((x+2)%3==0)if(((x+2)/3)>=p){++count;a[i]=-1;continue;}	
			}
		}
		
		for(int i=0;i<n;++i)
		{
			
			if(a[i]!=-1 && a[i]!=0)
			{
				int x=a[i];
				 if( (x)%3==0 )if((x)/3>=p){++count;continue;}
			if((x+1)%3==0)if((x+1)/3>=p){++count;continue;}
			if((x+2)%3==0)if((x+2)/3>=p){++count;continue;}	
			}
			if(a[i]==0)if(a[i]>=p)++count;
		}
		
		
		printf("%d\n",count);
				
		
		
	}
	
	return 0;
}
