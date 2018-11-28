#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int d[2000001];
int mid = 1;

long long solve(int a, int b)
{
	int R = 0;
	for (int i=a; i<=b; ++i, ++mid)
	{
//		cout << mid << endl;
		d[i] = mid;
		vector<int> t;

		int j = i;
		while (j)
		{
			t.push_back(j % 10);
			j /= 10;
		}
		reverse(t.begin(), t.end());

		while (j < t.size())
		{
			int r = 0;
			for (int k = j; k < t.size(); ++k)
				r = r * 10 + t[k];
			for (int k = 0; k < j; ++k)
				r = r * 10 + t[k];
			if (a <= r && r <= b && d[r] != mid)
			{
				d[r] = mid;
				++R;
			}
			++j;
		}
	}
	return R / 2;
}

int main()
{
	memset(d, 0, sizeof(d));
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i)
	{
		int a, b;
		cin >> a >> b;
		cout << "Case #" << i << ": " << solve(a, b) << endl;
	}
	return 0;
}
