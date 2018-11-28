#include <iostream>
#include <bitset>
using namespace std;

int main()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		int n,k;
		cin >> n >> k;

		int d = k % (1 << n);
		bitset <30> b(d);
		if (b.count() == n) cout << "Case #" << T << ": ON\n";
		else cout << "Case #" << T << ": OFF\n";
	}
	return 0;
}
