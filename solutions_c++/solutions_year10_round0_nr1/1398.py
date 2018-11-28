#include <iostream>
using namespace std;

int t, n , k, x;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	cin >> t;
	for(int i=1;i<=t;++i)
	{
		cout<<"Case #"<<i<<": ";
		cin >> n >> k;
		x = 1 << n;
		k = k % x;
		if(k + 1 == x)
			cout << "ON";
		else
			cout << "OFF";
		cout << endl;
	}
	return 0;
}
