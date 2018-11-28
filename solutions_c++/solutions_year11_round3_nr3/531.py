// Test.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 0; i < numCases; ++i) 
	{
		int n;
		long long l, h;
		cin >> n >> l >> h;

		vector<long long> a;
		a.resize(n);
		for (int j = 0; j < n; ++j)
			cin >> a[j];

		long long ln = 0;
		for (long long f = l; f <= h; ++f) {
			bool br = true;
			for (int j = 0; j < n; ++j)
				if (a[j] % f != 0 && f % a[j] != 0) {
					br = false;
					break;
				}
			if (br) {
				ln = f;
				break;
			}
		}

		cout << "Case #" << i+1 << ": ";
		if (ln > 0)
			cout << ln;
		else
			cout << "NO";
		cout << endl;
	}

	return 0;
}

