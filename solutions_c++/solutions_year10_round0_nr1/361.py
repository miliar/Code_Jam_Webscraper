#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
int main()
{
	int t,n,i;
	long long int k,p,r,q;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n>>k;
		p=pow(2,n);
		r=p-1;
		q=k-r;;
		if(q<0)
		cout<<"Case #"<<i<<": OFF\n";
		else
		{
			if(q%p==0)
				cout<<"Case #"<<i<<": ON\n";
			else
				cout<<"Case #"<<i<<": OFF\n";
		}
	}
	return 0;
}
