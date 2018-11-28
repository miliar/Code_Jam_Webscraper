#include <iostream>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long t, n, k;
	cin >> t;
	for (long long i = 0; i < t; ++i)
	{
		cin >> n >> k;
		if (k % (1 << n) == (1 << n) - 1)
			cout << "Case #" << (i + 1) << ": ON" << endl;
		else
			cout << "Case #" << (i + 1) << ": OFF" << endl;
	}
	return 0;
}