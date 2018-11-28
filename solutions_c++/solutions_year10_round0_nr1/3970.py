#include<iostream>
#include <fstream>
using namespace std;

main()
{
	ofstream myfile ("output.txt");
	ifstream inFile("input", ios::in);
	unsigned long count[41], N,K, T, i, cas=1;
	count[1]=1;
	for(i=2;i<31;i++)
	{
		count[i]=2*count[i-1]+1;
	}
	cin>>T;
	while(T--)
	{
		cin>>N>>K;
		N=count[N]+1;
		myfile<<"Case #"<<cas<<": ";
		if(K%N==N-1)
		{
			myfile<<"ON"<<endl;
		}
		else
		{
			myfile<<"OFF"<<endl;
		}
		cas++;
	}
	return 0;
}


		
