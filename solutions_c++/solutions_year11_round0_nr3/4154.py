#include<iostream>
#include <algorithm>
using namespace std;
main()
{
	int test,n,i,res,least,num,xorr,cas=1;
	cin>>test;
	while(test--)
	{
		cin>>n;
		xorr=res=0;
		for(i=0;i<n;i++)
		{
			cin>>num;
			if(i==0)
				least = num;
			else
				least = min(least,num);
			res+=num;
			xorr^=num;
		}
		if(xorr==0)
			cout<<"Case #"<<cas<<": "<<res-least<<endl;
		else
			cout<<"Case #"<<cas<<": NO"<<endl;
		cas++;
	}
}
			
		
			
		
