#include <iostream>
#include <algorithm>

using namespace std;

int keys[1000];

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt)
	{
		int p, k, l;
		cin >> p >> k >> l;
		for(int i = 0; i < l; ++i) cin >> keys[i];
		sort(keys, keys + l, greater<int>());
		int res = 0;
		for(int i = 0; i < l; ++i)
		{
			res += (i / k + 1) * keys[i];
		}
		printf("Case #%d: %d\n", tt, res);
	}
	return 0;
}