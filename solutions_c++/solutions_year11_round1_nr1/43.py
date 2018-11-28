#include<iostream>
using namespace std;

const char win[] = "Possible";
const char lose[] = "Broken";

int gcd( int x,int y )
{
	if( y==0 ) return x;else return gcd(y,x%y);
}
long long n;
int pd,pg;
bool work()
{
	if( pg==100 ) return pd==100;else
	if( pg==0 ) return pd==0;else
		return 100 / gcd(100,pd) <= n;
}
int main()
{
	int T,TT=0;
	for(cin>>T;T;T--)
	{
		cout << "Case #"<< ++TT << ": ";
		cin >> n >> pd >> pg;
		if( work() )
			cout << "Possible" << endl;else
			cout << "Broken" << endl;
	}
	return 0;
}
