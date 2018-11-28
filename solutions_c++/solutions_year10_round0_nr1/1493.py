#include <iostream>

using namespace std;

typedef long long lint;

int main()
{
	int tc;
	cin >> tc;

	for (int cn = 1; cn <= tc; ++cn)
	{
		lint n, k;
		cin >> n >> k;

		lint mask = (1 << n) - 1;

		cout << "Case #" << cn << ": " << ((k & mask) == mask ? "ON" : "OFF") << endl;
	}

	return 0;
}
