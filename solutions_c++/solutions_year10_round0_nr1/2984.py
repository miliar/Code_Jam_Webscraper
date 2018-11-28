// code jam 2010 Snapper Chain.cpp : Defines the entry point for the console application.
//

#include <iostream>
using namespace std;



int main(int argc, char* argv[])
{
	int T,N,K;
	int i;
	cin>>T;
	for(i=1; i<=T; ++i)
	{
		cin>>N>>K;
		if((K+1)%(1<<N) == 0)
		{
			cout<<"Case #"<<i<<": ON"<<endl;
		}
		else cout<<"Case #"<<i<<": OFF"<<endl;
	}
	return 0;
}
