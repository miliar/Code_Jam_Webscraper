#include <cstdio>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <numeric>

using namespace std;

string SnapperChain(int n, int k)
{
	return (k % (1 << n) == (1 << n) - 1) ? "ON" : "OFF";
}

int main()
{
	string line;

	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int n, k;
		cin >> n >> k;

		string ret = SnapperChain(n, k);

		cout << "Case #" << caseno << ": " << ret << endl;
	}

	return 0;
}
