
#include <iostream>
#include <vector>

using namespace std;

void DoCase ()
{
	int num;
	cin >> num;

	vector<int> A;
	vector<int> B;

	for (int i = 0; i < num; ++i) {
		int x;
		cin >> x;
		A.push_back (x);
		cin >> x;
		B.push_back (x);
	}

	int result = 0;
	for (int i = 0; i < num; ++i)
		for (int j = 0; j < num; ++j)
			if (i != j)
				if (A[i] < A[j] && B[i] > B[j])
					++result;

	cout << result;
}

main ()
{
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; ++i) {
		cout << "Case #" << i << ": ";
		DoCase ();
		cout << endl;
	}
}
