#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int gcd (int a, int b)
{
	if (b == 0) return a;
	return gcd(b,a%b);
}

int main ()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		int n;
		cin >> n;
		
		int v[3];
		for (int i = 0; i < n; i++) cin >> v[i];

		sort(v,v+n);
		int g = -1;
		for (int i = 0; i < n; i++)
		{
			for (int j = i+1; j < n; j++)
			{
				if (g == -1) g = abs(v[i]-v[j]);
				else g = gcd (g,abs(v[i]-v[j]));
			}
		}

		int y = v[n-1]/g;
		if (v[n-1] % g != 0) y++;
		y = g*y - v[n-1];
		
		cout << "Case #" << T << ": " << y << "\n";
		
	}
	return 0;
}
				
		
