#include<iostream>

using namespace std;

typedef unsigned long UL;

int main()
{
	UL ntests;
	cin>>ntests;
	for(UL tt=1; tt<=ntests; ++tt)
	{
		UL N, K;
		cin>>N>>K;
		cout<<"Case #"<<tt<<": "<<( ((K+1)%(1UL<<N))?"OFF\n":"ON\n");
	}
}