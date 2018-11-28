#include<iostream>

using namespace std;

int main()
{
	int n,T,N,K,i,j,k;
	cin>>n;
	for(i=1;i<=n;i++)
	{
		cin>>N>>K;
		k=1;
		for(j=1;j<=N;j++)
			k*=2;
		if(K%k==k-1)
		{
			cout<<"Case #"<<i<<": ON"<<endl;
		}
		else
			cout<<"Case #"<<i<<": OFF"<<endl;
	}

}