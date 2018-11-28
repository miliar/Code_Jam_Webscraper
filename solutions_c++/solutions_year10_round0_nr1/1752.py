#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int test,n,k;
	cin>>test;
	for(int i=1;i<=test;++i)
	{
		cin>>n>>k;
		int times=(1<<n);
		k%=times;
		cout<<"Case #"<<i<<": ";
		if(k==times-1)
			cout<<"ON\n";
		else
			cout<<"OFF\n";
			
	}

}