#include<iostream>
using namespace std;
int t,n;
long long l,p,c;
long long ans;
long long  temp;
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin >> t;
	for (int test = 1; test <= t; test++)
	{
	 	cin >> l >> p >> c;   
	 	temp = 0;
	 	l = l*c;
	 	while (l<p)
	 	{
			temp++;
			l*=c;
		}
		long long a = 1;
		for (int i = 1; i <= 1000; i++ )
		{
			a = a * 2;
			if ( a > temp )
			{
				ans = i;
				break;
			}
		}
		if (temp == 0 ) ans = 0;
		cout <<"Case #"<<test<<": "<<ans<<endl;
	}
	return 0;
}
