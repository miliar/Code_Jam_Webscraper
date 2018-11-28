#include <iostream>
#include<stdio.h>
using namespace std;

int main()
{
 int T,N,Pd,Pg,count=0;
 int w,l,t;
 scanf("%d",&T);
 while(T--)
 {
	count++;
	scanf("%d %d %d",&N,&Pd,&Pg);
	bool p=false;
	int i;
//	if(Pd==0)
//	i=0;
//	else
	i=1;
	
	for(;i<=N;i++)
	{
		if(Pd*i%100==0)
		{
			w=Pd*i/100;
			l=(100-i)-(Pg-w);
			if(l>=0&&l<=100&&(Pg-w)>=0)
			{
				p=true;
				break;
			}
		}
	}
	if(p)
	printf("Case #%d: Possible\n",count);
	else
	printf("Case #%d: Broken\n",count);
		
 }
}
