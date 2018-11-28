#include <iostream>
using namespace std;
int gcd(int a,int b)
{
	int t;
	if(a<b) t=a,a=b,b=t;
	while(b)
	{
		t=a;a=b;b=t%b;
	}
	return a;
}
int main()
{
	int t,pd,pg,i,j;
	long long n;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>n>>pd>>pg;
		cout<<"Case #"<<j<<": ";
		if((pg==0 && pd!=0) || (pg==100 && pd!=100))
			cout<<"Broken\n";
		else if(n<100/gcd(100,pd))
			cout<<"Broken\n";
		else cout<<"Possible\n";
	}
	//cout<<gcd(6,8)<<endl;
//	system("pause");
}
