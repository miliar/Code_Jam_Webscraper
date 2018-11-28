#include <iostream>
using namespace std;
__int64 gcd(__int64 a,__int64 b)
{
	if (b==0)
		return a;
	return gcd(b,a%b);
}
int main()
{
	int t;
	__int64 n,d,g;
	__int64 b=100;
	__int64 gcdd,gcdg;

	char result[2][10]={"Broken","Possible"};
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		bool flag=1;
		cin>>n>>d>>g;
		if (g==0 && d!=0)
		{
			flag=0;
		}
		else if (g==100 && d!=100)
		{
			flag=0;
		}
		else
		{
			gcdd=gcd(d,b);
			if (b/gcdd>n)
				flag=0;
		}

		cout<<"Case #"<<i<<": "<<result[flag]<<endl;
	}
	return 0;
}