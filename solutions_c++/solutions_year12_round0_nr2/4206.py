// Author: Sridhar Krishnan (sridharkritha@gmail.com)

#include "stdafx.h" // Needed only for Visual studio IDE

#include<iostream>
#include<vector>
#include<map>
#include<string>
#include <limits>
using namespace std;



int main()
{
	freopen("q1.in", "r", stdin);
    freopen("a1.out", "w", stdout);
	int t=0, p=0,comp=0,s=0,test=0,td=0,ntd=0;
	int n =0;
	int NN=0;
    cin>>test;
	for(int y=1;y<=test;y++)
	{
	cin>>NN;
	cin>>s;
    cin>>p;
	cout<<"Case #"<<y<<": ";
	
	for(int x=0;x<NN;x++)
	{
cin>>n;
	for(int i=10; i>=0; i--)
	{
		if(comp == 1)
			break;
		for(int j=10; j>=0; j--)
	{
		if(comp == 1)
			break;
		if(abs(i-j) >2)
			continue;
		for(int k=10; k>=0; k--)
	{
		if(comp == 1)
			break;
		if((abs(j-k) >2)|| (abs(i-k) >2))
			continue;
		if(n == i+j+k)
			if((p<=i)||(p<=j)||(p<=k))
			{
				
				if((abs(i-j)==2)||(abs(i-k)==2)||(abs(j-k)==2))
				{	
					if(td == 0)
					{
					td= 1;
					//t = t+1;
					}
					if(ntd == 1)
					 comp = 1;					
				}
				else
				{
					if(ntd == 0)
					{
					ntd= 1;
					//t = t+1;
					}
					if(td == 1)
					comp = 1;
				}			
				
			}

	}

	}

	}

	if((td==1)&&(ntd ==1))
		t = t+1;
	else if ((td==1)&&(ntd ==0)&&(s!=0))
	{
		t = t+1;
		if(s>0)
		s = s-1;
	}
	else if((td==0)&&(ntd ==1))
	{
		t = t+1;
	}
	comp = 0;
	ntd =0;
	td =0;
	}
	cout<<t<<endl;
	t=0;
	}
	
	return 0;	
}