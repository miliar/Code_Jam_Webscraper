#include <iostream>
using namespace std;

long long gcd(long long a, long long b)
{
	if ((a % b) == 0) return b;
	else if (a>b) return gcd(a % b, b);
	else return gcd(b % a, a);
}

long long abs(long long x)
{
	return (x<0 ? -x : x);
}

int main()
{
	int c;
	cin >> c;
	for (int cc=1; cc<=c; cc++)
	{
		int n;
		long long *t;
		cin >> n;
		t = new long long[n];

		for (int i=0; i<n; i++)
			cin >> t[i];

		int g = 0;

		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++)
			{
				long long k = abs(t[i] - t[j]);
				if (k != 0)
				if (g == 0)
					g = k;
				else
					g = gcd(g, k);
			}

		long long min = g;
		for (int i=0; i<n; i++)
		{
			long long j = t[i] % g;
			if (j == 0)
			{
				min = 0;
				break;
			} else {
				if (g - j < min)
					min = g - j;
			}
		}

		cout << "Case #" << cc << ": " << min << endl;
	}
	return 0;
}



