#include <iostream>
using namespace std;

int n,t,x,k,m;
int fun(int n)
{
	if(n==1)
		return 1;
	return fun(n-1)*2+1;
}

int main()
{
	

	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>t;
	for(x=1;x<=t;x++)
	{
		cin>>n>>k;
		m=fun(n);
		if(k%(m+1)==m)
			cout<<"Case #"<<x<<": ON\n";
		else 
			cout<<"Case #"<<x<<": OFF\n";
	}
	return 0;
}