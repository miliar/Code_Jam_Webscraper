#include <iostream>
#include <cstdio>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;

int
main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, z;
	cin >> T;
	double p = (sqrt(5) - 1) / 2;
	for (z = 1; z <= T; z++)
	{
		long long A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;
		long long ans = 0;
		for (long long i = A1; i <= A2; i++)
		{
			long long q = i * p;
			if (q >= B2)
				ans += B2 - B1 + 1;
			else if (q >= B1)
				ans += q - B1 + 1;
		}
		for (long long i = B1; i <= B2; i++)
		{
			long long q = i * p;
			if (q >= A2)
				ans += A2 - A1 + 1;
			else if (q >= A1)
				ans += q - A1 + 1;
		}
		cout << "Case #" << z << ": " << ans << endl;
	}
	return(0);
}

