#include<iostream>
#include<string>
using namespace std;

typedef unsigned long long int lli;

lli pow(lli N)
{
	if(N==0)
		return 1;
	if(N%2==0)
	{
		lli pw = pow(N/2);
		return pw*pw;
	}
	else
		return 2*pow(N-1);
}

int main()
{
	lli T,N,K;

	cin>>T;
	for(lli it=0;it<T;it++)
	{
		cin>>N>>K;
		lli i;
		lli pw = pow(N);
		i=(K+1)%pw;		
		//cout<<i<<endl;
		if(i==0)
			cout<<"Case #"<<it+1<<": "<<"ON"<<endl;
		else
			cout<<"Case #"<<it+1<<": "<<"OFF"<<endl;			
	}
	return 0;
}
