#include <iostream>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;

int main()
{
	int t = 0;
	cin >> t;

	int num = 1;
	while (num <= t) {
		long long int n = 0, k = 0;
		cin >> n >> k;

		// Times that you will need to snap to let the light ON
		long long times = pow(2, n) - 1;

		if (k % (times+1) != times || k == 0)
			cout << "Case #" << num << ": OFF" << endl;
		else
			cout << "Case #" << num << ": ON" << endl;

		num++;
	}

	return 0;
}
