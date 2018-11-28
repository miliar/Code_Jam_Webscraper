#include <iostream>

using namespace std;

int a[50];

int main()
{
	freopen("output.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	int i;
	a[1] = 1;
	for(i=2;i<=30;++i)
		a[i] = 2*a[i-1]+1;
	int t;
	cin>>t;
	int n,k;
	for(i=1;i<=t;++i)
	{
		cin>>n>>k;
		cout<<"Case #"<<i<<": ";
		if(k%(a[n]+1) == a[n])
			cout<<"ON\n";
		else
			cout<<"OFF\n";
	}
	return 0;
}