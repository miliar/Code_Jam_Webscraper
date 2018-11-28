#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int caso = 1; caso<=T; caso++)
	{
		cout << "Case #" << caso << ": ";
		int x = 0;
		int n;
		cin >> n;
		int mn = 2000000;
		int sm = 0;
		for (int i=0;i<n;i++)
		{
			int a;
			cin >> a;
			mn = min (a,mn);
			x ^= a;
			sm+=a;
		}
		if (x==0)
			cout << sm-mn << endl;
		else
			cout << "NO" << endl;
	}
}
