#include <iostream>

using namespace std;

int main()
{
	int nTests;
	cin >> nTests;
	
	for (int run = 1; run <= nTests; ++run)
	{
		int n, k;
		cin >> n >> k;
		k %= (1 << n);
		if (k == ((1 << n) - 1)) cout << "Case #" << run << ": ON" << endl;
		else cout << "Case #" << run << ": OFF" << endl;
	}
	return 0;
}
