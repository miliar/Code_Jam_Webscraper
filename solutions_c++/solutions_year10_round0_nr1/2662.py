#include <iostream>
using namespace std;

int main()
{
	bool b;
	unsigned long t, n, k, i;

	cin >> t;

	for (i = 0; i < t; i++)
	{
		cin >> n >> k;
		b = false;

		b = ((((1 << n) - 1) & k) == ((1 << n) - 1));

		cout << "Case #" << i+1 << ": " << (b ? "ON" : "OFF") << endl;
	}

	return 0;
}
