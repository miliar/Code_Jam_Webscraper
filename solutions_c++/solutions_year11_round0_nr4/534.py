#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef vector<int>		VI;

const int MAX = 1000;
double res[MAX+1];
double D[1024];
double fac[1024];

int main()
{
	fac[0] = fac[1] = 1;
	D[0] = 1;
	D[1] = 0;
	for (int n = 0; n <= MAX; n++)
	{
		D[n+2] = ( (n+1)*D[n+1] + D[n] ) / (n+2);
		fac[n+2] = (n+2) * fac[n+1];
	}
	
	for (int n = 2; n <= MAX; n++)
	{
		res[n] = 1;
		for (int k = 1; k <= n; k++)
			res[n] += res[n-k] * D[n-k] / fac[k];
		res[n] /= 1 - D[n];
	}

	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++)
	{
		int n;
		cin >> n;
		VI input(n);
		for (int i = 0; i < n; i++)
			cin >> input[i];
		VI s = input;
		sort(input.begin(), input.end());
		int d = 0;
		for (int i = 0; i < n; i++)
			if (input[i] != s[i])
				d++;
		printf("Case #%d: %.8lf\n", kase, res[d]);
	}

	return 0;
}
