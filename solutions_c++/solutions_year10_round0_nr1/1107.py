#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		unsigned long n, k;
		cin >> n >> k;

		unsigned long m = 1;
		for (unsigned long i = 1; i < n; ++i)
			m |= 1 << i;

		cout << "Case #" << t << ": " << ((k & m) == m ? "ON" : "OFF") << endl;
	}
}
