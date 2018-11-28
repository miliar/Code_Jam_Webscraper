#include <cstdio>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

long long NumberGame(int A1, int A2, int B1, int B2)
{
	double rat = (1 + sqrt(5)) / 2;
	long long ret = (long long)(A2 - A1 + 1) * (B2 - B1 + 1);
	for (int i = A1; i <= A2; i++) {
		int lb = max(B1, (int)ceil(i / rat));
		int ub = min(B2, (int)floor(i * rat));
		if (lb <= ub) {
			ret -= ub - lb + 1;
		}
	}
	return ret;
}

int main()
{
	string line;

	int cases;
	cin >> cases;
	getline(cin, line);

	for (int caseno = 1; caseno <= cases; caseno++) {
		int A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;

		long long ret = NumberGame(A1, A2, B1, B2);

		cout << "Case #" << caseno << ": " << ret << endl;
	}

	return 0;
}
