#include <iostream>
using namespace std;

int main()
{
	long long i, j, t, n, k, x;
	cin >> t;
	for (i=1LL;i<=t;i++)
	{
		x=1LL;
		cin >> n >> k;
		for (j=0LL;j<n;j++)
			x*=2LL;
		cout << "Case #" << i << ": ";
		if (((k+1LL)%x!=0LL)||(k==0LL))
			cout << "OFF";
		else
			cout << "ON";
		cout << endl;
	}
	return 0;
}
