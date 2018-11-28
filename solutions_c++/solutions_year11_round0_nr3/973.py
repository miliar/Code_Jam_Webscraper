#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);	
	freopen("output.txt", "w", stdout);

	int cntTest;
	cin >> cntTest;

	for (int test = 0; test < cntTest; ++test)
	{
		int n, xor = 0, res = 0;
		cin >> n;

		vector <int> a(n);
		for (int i = 0; i < n; ++i)		
		{
			cin >> a[i];
			xor ^= a[i];
		}

		sort(a.rbegin(), a.rend());
		for (int i = 0; i < n - 1; ++i)
			res += a[i];

		cout << "Case #" << test + 1 << ": ";
		if (xor)
			cout << "NO";
		else
			cout << res;
		cout << endl;
	}

	return 0;
}