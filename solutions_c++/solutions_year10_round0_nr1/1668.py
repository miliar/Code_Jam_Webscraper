#include<iostream>
using namespace std;
int main()
{
	freopen("c:\\2.in","r",stdin);
	freopen("c:\\out2.txt","w",stdout);
	long long a[40];
	int i;
	a[1]=1;
	for(i=2;i<=30;i++)
		a[i]=a[i-1]*2+1;
	long long t;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		long long n,k;
		cin>>n>>k;
		if((k+1)%(a[n]+1)==0)
			cout<<"Case #"<<i<<": ON"<<endl;
		else
			cout<<"Case #"<<i<<": OFF"<<endl;
	}
return 0;
}