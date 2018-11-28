#include <iostream>

using namespace std;

int main()
{
	unsigned t, n, k;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n >> k;
		cout << "Case #" << i+1 << ": ";
		int p = (1 << n) - 1;
		if ((k & p) == p)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	return 0;
}
