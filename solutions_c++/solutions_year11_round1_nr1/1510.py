#include<iostream>
#include<math.h>
#include<stdio.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int max=t;
	int n,pd,pn;
	do
	{
	int flash=0;
	int err=0;
	scanf("%d%d%d",&n,&pd,&pn);
	
	float temp=n;
	if(pn==100)
	{
		if(pd!=100)
			err=1;
		if(pd==100)
		{	err=0;flash=1;}
	}
	if(pn==0)
	{
		if(pd!=0)
			{err=1;flash=1;}
		
	}
	if(flash==0)
	{
	for(temp;temp>=0;temp--)
	{
		
		float pc=float(pd)/100;
		pc=pc*temp;
		//cout<<pd<<" "<<pc<<" "<<temp;
		float pc2=floor(pc);
		if(pc==pc2)
			break;

	}
	
	if(temp==0)
		err=1;

	}
	int i=float(pd)/100*temp;
	
	if(err!=1 && flash!=1)
	{
	
	for(i;i<=100;i++)
	{
		float pn=(pn/100)*i;
		float pn2=floor(pn);
		if(pn==pn2)
			break;	
	}
	}
		
	if(err==0)
		printf("Case #%d: Possible\n",max-t+1);
	else
		printf("Case #%d: Broken\n",max-t+1);



	
	

	t--;
	}while(t!=0);	


	return 0;
}
