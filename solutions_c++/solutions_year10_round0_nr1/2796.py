#include<iostream>
using namespace std;

int main()
{
	
	int i,j,t,k,n,temp;
	cin>>t;
	for(i=0;i<t;i++)
	{
		temp=1;
		cin>>n>>k;
		for(j=1;j<=n;j++)
			temp*=2;
		if(k%temp==temp-1)
			cout<<"Case #"<<i+1<<": ON"<<endl;
		else
			cout<<"Case #"<<i+1<<": OFF"<<endl;
	}
}