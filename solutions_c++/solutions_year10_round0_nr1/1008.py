#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;


int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	long long t,n,k;
	cin>>t;
	long long i;
	for (i = 0 ; i < t ; i++)
	{
		cin>>n>>k;
		if ((k+1)%(long long)pow((double)2,(double)n) == 0)
		{
			cout<<"Case #"<< i+1 << ": ON"<<endl;

		}
		else
		{
			cout<<"Case #"<< i+1 << ": OFF"<<endl;
		}
	}
	
	return 0;
}