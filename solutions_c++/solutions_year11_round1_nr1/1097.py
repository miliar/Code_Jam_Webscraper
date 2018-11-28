#include <iostream>
using namespace std;
// gcd
int gcd(int a, int b)
{
	int c;
	while ((c = a % b) != 0)
	{
		a = b;
		b = c;
	}
	return b;
}
int main()
{
	int t;
	cin >> t;
	long long n;
	int pd, pg;
	for (int i = 1; i <= t; ++i)
	{
		cin >> n >> pd >> pg;
		cout << "Case #" << i << ": ";
		if ((pg == 0 && pd != 0) || (pg == 100 && pd != 100))
		{
			cout << "Broken" << endl;
			continue;
		}
		int cc = gcd(pd, 100);
		//cout << cc << endl;
		int maxt = 100 / cc;
		if (maxt > n)
		{
			cout << "Broken" << endl;
		}
		else
		{
			cout << "Possible" << endl;
		}
	}
	return 0;
}