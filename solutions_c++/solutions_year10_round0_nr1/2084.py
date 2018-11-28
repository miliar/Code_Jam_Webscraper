#include <iostream>

using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;

	cin >> T;

	for (int t = 1; t <= T; ++ t)
	{
		long long n,k;

		cin >> n >> k;

		k %= (1 << n);

		cout << "Case #" << t << ": ";

		if (k == (1 << n) - 1)
			cout << "ON\n";
		else
			cout << "OFF\n";
	}

	return 0;
}