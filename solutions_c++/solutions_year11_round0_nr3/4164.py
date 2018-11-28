#include<iostream>
using namespace std;

int main()
{
int num_test;
int num_candies;

cin>>num_test;

	for(int i=0;i<num_test;i++)
	{
		cin>>num_candies;
		long int candvalue[num_candies];
		long int checkxor=0;
		long int seanshare = 1000000L;
		long int maxsum =0;
		for(int j=0;j<num_candies;j++)
		{
			cin>>candvalue[j];
			checkxor = checkxor^candvalue[j];
			if(candvalue[j]<seanshare)
			seanshare=candvalue[j];
			maxsum += candvalue[j];
		}
	
	if(checkxor)
	cout<<"Case #"<<i+1<<": "<<"NO\n";
	else
	cout<<"Case #"<<i+1<<": "<<maxsum-seanshare<<"\n";
	}
}

