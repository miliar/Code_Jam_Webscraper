#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int n,num[1000+10],zor=0,sum=0,small=100000000;
	
	for(int z=1;z<=t;z++)
	{
		zor=0,sum=0,small=100000000;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>num[i];
			zor^=num[i];
			sum+=num[i];
			small=min(small,num[i]);
		}
		if(zor)
		{
			cout<<"Case #"<<z<<": NO"<<endl;
			continue;
		}
		else
		{
			cout<<"Case #"<<z<<": "<<sum-small<<endl;
		
		}
	}
}
