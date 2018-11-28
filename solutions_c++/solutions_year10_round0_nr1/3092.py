#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int t,n,k,i,cnt,den;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n>>k;
		cnt = k+1;
		den = pow(2,n) ;
		if(cnt%den == 0)
		{
			cout<<"Case #"<<i+1<<": ON\n";
		}
		else
			cout<<"Case #"<<i+1<<": OFF\n";
	}
	return 0;
}
