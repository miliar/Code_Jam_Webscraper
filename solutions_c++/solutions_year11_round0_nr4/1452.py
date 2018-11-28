#include <iostream>

using namespace std;

int main()
{
	int a, i, n, tot, j, b;
	cin >> a;
	for (i = 1; i <= a; ++i) {
		cin >> n;
		tot = 0;
		for (j = 1; j <= n; ++j) {
			cin >> b;
			if (j != b) tot += 1;
		}
		cout << "Case #" << i << ": " << tot << endl;
	}
	return 0;
}