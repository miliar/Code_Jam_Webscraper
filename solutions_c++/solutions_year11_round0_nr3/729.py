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
		vector<int> c(n);

		int x = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> c[i];
			x ^= c[i];
		}
		if (x != 0)
			cout << "NO";
		else
		{
			sort(c.begin(), c.end());
			long long int sum = 0;
			for (int i = 1; i < c.size(); ++i)
				sum  += c[i];
			cout << sum;
		}
		cout << endl;
	}
}