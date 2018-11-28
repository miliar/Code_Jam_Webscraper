#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int solve(int k, const string& s)
{
	vector<int> p(k); for (int i = 0; i < k; ++i) p[i] = i;
	int n = (int)s.length();
	int minlen = n;
	do {
		int rle = 1;
		string ress(n, ' ');
		for (int i = 0; i < n; ++i) ress[i] = s[(i / k) * k + p[i % k]];
		for (int i = 1; i < n; ++i) if (ress[i] != ress[i-1]) ++rle;
		if (rle < minlen) minlen = rle;
	} while (next_permutation(p.begin(), p.end()));

	return minlen;
}


int main()
{
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int k;
		string s;
		cin >> k >> s;
		cout << "Case #" << (test + 1) << ": " << solve(k, s) << endl;
	}
	return 0;
}
