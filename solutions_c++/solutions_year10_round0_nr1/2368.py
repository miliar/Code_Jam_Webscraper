#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int t,n,k;
	int c,flag,m;
	cin>>t;
	c=0;
	while(c++<t)
	{
		flag=0;
		cin>>n>>k;

		m = (int) pow(2.0,n);

		if(k > m)
			k = k%m;

		if(k == m-1)
			flag=1;

		if(flag)
		cout<<"Case #"<<c<<": "<<"ON"<<endl;
		else
		cout<<"Case #"<<c<<": "<<"OFF"<<endl;


	}

	return 0;
}
