#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define	fn(i, n)	for (int i = 0; i < (n); ++i)

int TESTS;

int main()
{
	freopen ("A-small.in", "rt", stdin);
	freopen ("A-small.out", "wt", stdout);

	cin >> TESTS;
	for (int test = 1; test <= TESTS; ++test)
	{
		int n;
		int m[100];
		int ans;
		cin >> n;
		string s;
		fn (i, n) {
			cin >> s;
			for (m[i] = n-1; m[i] > 0 && s[m[i]] == '0'; --m[i]);
		}
		ans = 0;
		for (int i = n-1; i >= 0; --i) {
			for (int ii = i; m[ii] > ii; ++ii) {
				int j;
				for (j = ii + 1; m[j] > ii; ++j);
				for (int jj = j; jj > ii; --jj) {
					++ans;
					swap (m[jj], m[jj-1]);
				}
			}
		}
		cout << "Case #" << test << ": " << ans << endl;
	}

	return 0;
}