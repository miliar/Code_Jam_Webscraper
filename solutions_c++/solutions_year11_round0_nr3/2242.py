#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int T=1; T<=t; T++)
	{
		int n, x = 0, s = 0, mn = 1<<29;
		cin >> n;
		for(int i=0; i<n; i++)
		{
			int d;
			cin >> d;
			x ^= d;
			mn = min(mn, d);
			s += d;
		}
		cout << "Case #" << T << ": ";
		if(x)
			cout << "NO";
		else
			cout << s - mn;
		cout << endl;
	}
	return 0;
}

