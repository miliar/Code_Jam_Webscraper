#include <iostream>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i=1; i<=t; i++)
	{
		int n, k;
		cin >> n >> k;
		cout << "Case #" << i << ": ";
		if( ((k+1) % (1 << n)) == 0)
			cout << "ON";
		else
			cout << "OFF";
//		cout << k << " " << n << endl;
//		cout << (k+1)  <<" " <<  (1<<n) << endl;
		cout << endl;
	}
	return 0;
}
