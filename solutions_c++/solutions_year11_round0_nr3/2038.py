#include <iostream>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		int n;
		cin >> n;
		int xo = 0, sum = 0, min = 1e6;
		while (n--)
		{
			int c;
			cin >> c;
			xo ^= c;
			sum += c;
			if (min > c) min = c;
		}
		if (xo != 0) cout << "NO" << endl;
		else cout << sum - min << endl;
	}
	return 0;
}