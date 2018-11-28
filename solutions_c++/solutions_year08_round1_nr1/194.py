#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	for (int test = 1; test <= t; ++test)
	{
		int n;
		scanf("%d", &n);
		int tmp;
		vector<int> v0, v1;
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &tmp);
			v0.push_back(tmp);
		}
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &tmp);
			v1.push_back(tmp);
		}
		sort(v0.begin(), v0.end());
		sort(v1.rbegin(), v1.rend());
		long long ans = 0;
		for (int i = 0; i < n; ++i)
			ans += 1LL * v0[i] * v1[i];
		printf("Case #%d: %lld\n", test, ans);
	}
}
