#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<cstring>
#include<cmath>
#include<math.h>

void main()

{	
	
	float n,f,t;
	float no,pd,pt;
	//int won;
	freopen("A-small-attempt3.in","r",stdin);
    freopen("A-small.out","w",stdout);

	cin>>n;

	for(int i=0;i<n;i++)
	{	f=0;
		cin>>no>>pd>>pt;
		while(no)
		{
			if(f==1)
				break;
		for(int j=1;j<=no;j++)
		{
			if(((j*100)/no)==pd)
			{
				//won=j;
				f=1;
				break;
				
			}
		}
		no--;
		}
		if(pd!=0&&pt==0)
			f=0;
		else if(pd==0&& pt==0)
			f=1;
		if(pd!=100&&pt==100)
			f=0;
		else if(pd==100&&pt==100)
			f=1;

		if(f==1)
			cout<<"Case #"<<i+1<<": Possible"<<endl;
		else
			cout<<"Case #"<<i+1<<": Broken"<<endl;

	}	
}