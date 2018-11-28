#include <iostream>
#include <math.h>
using namespace std;

int t,n,k;
bool on;

int main()
{
	int i,n1;
	cin>>t;
	for (i=1; i<=t; i++)
	{
		cin>>n>>k;
		if ((k+1)%(int)pow(2,n)==0) on=true;
		else on=false;
		if (on) cout<<"Case #"<<i<<": ON"<<endl;
		else cout<<"Case #"<<i<<": OFF"<<endl;
	}
	return 0;
}


