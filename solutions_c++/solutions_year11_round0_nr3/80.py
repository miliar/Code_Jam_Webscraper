#include <iostream>
using namespace std;

int main()
{
	int t,c,i,j,n,sum,xo,mi;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		mi=9999999;
		cin>>n;
		xo=0;sum=0;
		for(i=0;i<n;i++)
		{
			cin>>c;
			xo^=c;
			sum+=c;
			if(c<mi) mi=c;
		}
		cout<<"Case #"<<j<<": ";
		if(xo)
			cout<<"NO\n";
		else
			cout<<sum-mi<<endl;
	}
}
