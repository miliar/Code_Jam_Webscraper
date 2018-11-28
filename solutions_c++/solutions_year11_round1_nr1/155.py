#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// FreeCell Statistics

long long gcd(long long a, long long b)
{
	if (b == 0) {
		return a;
	}
	return gcd(b, a % b);
}

int main()
{
	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		long long N;
		int Pd, Pg;
		cin >> N >> Pd >> Pg;
		cout << "Case #" << caseno << ": ";
		long long ud = (Pd == 0) ? 1 : 100 / gcd(Pd, 100);
		if (ud > N || (Pd > 0 && Pg == 0 || Pd < 100 && Pg == 100)) {
			cout << "Broken" << endl;
		} else {
			cout << "Possible" << endl;
		}
	}

	return 0;
}
