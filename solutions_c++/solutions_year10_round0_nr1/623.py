#include <iostream>

using namespace std;

int main()
{
	long long n, t, k;

	cin >> t;

	for (long long i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";

		cin >> n >> k;

		n = 1LL << n;

		if (k < n - 1 || (k - n + 1) % n != 0)
			cout << "OFF\n";
		else
			cout << "ON\n";
	}

	return 0;
}
