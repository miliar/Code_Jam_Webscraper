#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

int main()
{
	int CN;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> CN;
	for (int tc = 0; tc < CN; ++tc)
	{
		cout << "Case #" << tc+1 << ": ";
		int n;
		cin >> n;
		vector<int> a(n), b(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> a[i];
			b[i] = a[i];
		}
		sort(b.begin(), b.end());
		int k = 0;
		for (int i = 0; i < n; ++i)
		{
			if (a[i] != b[i])
				++k;
		}
		cout << k << ".000000" << endl;
	}
}