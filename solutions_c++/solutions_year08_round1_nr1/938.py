#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int
prod(const int *v1, const int *v2, const int& n)
{
	int result = 0;
	for (int i = 0; i != n; ++i)
		result += v1[i] * v2[i];
	return result;
}

int
main()
{
	int cases;
	cin >> cases;

	for (int c = 1; c != cases + 1; ++c) {
		int n;	// number of integers in a vector
		cin >> n;

		int *v1 = new int[n],	// vectors
			*v2 = new int[n];

		for (int i = 0; i != n; ++i)
			cin >> v1[i];
		for (int i = 0; i != n; ++i)
			cin >> v2[i];
		
		sort(v1, v1 + n);
		sort(v2, v2 + n, greater<int>());

		cout << "Case #" << c << ": " << prod(v1, v2, n) << endl;



		delete v1, v2;
	}

	return 0;
}
