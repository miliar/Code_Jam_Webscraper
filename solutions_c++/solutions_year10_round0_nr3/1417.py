#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <limits.h>

using namespace std;


long long find(int r, int k, vector<int>& v)
{
	long long sum = 0;
	for (auto i = 0; i < v.size(); i++)
	{
		sum += v[i];
	}
	if (sum <= k)
		return sum * r;

	int R = r;
	int idx = 0;
	sum = 0;
	long long ans = 0;
	bool g = true;
	while (R > 0)
	{
		int K = k;
		while (true)
		{
			if (K < v[idx])
			{
				break;
			}
			sum += v[idx];
			K -= v[idx];
			idx = (idx + 1) % v.size();
		}
		--R;
		if (idx == 0 && g)
		{
			ans += sum * (r / (r - R));
			g = false;
			sum = 0;
			R = r % (r - R);

		}
	}
	ans += sum;
	return ans;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int r, k, n;
		cin >> r >> k >> n;
		vector<int> v(n);
		for (int j = 0; j < n; j++)
			cin >> v[j];
		printf("Case #%d: ", i + 1);
		cout << find(r, k, v) << endl;
	}
	return 0;
}