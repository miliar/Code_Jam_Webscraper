#include <iostream>
#include <math.h>
#include <map>
#include <vector>
#include <utility>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long l, p, c, t;
//	vector<pair<int, int>> v;
	cin >> t;
	for (long long tc = 0; tc < t; ++tc)
	{
		cin >> l >> p >> c;
		//v.resize(n);
		int count = 0;
		for (long long i = l; i < p; i *= c)
			++count;
		
		long long ans = ceil(log((double)count) / log(2.0));
		cout << "Case #" << (tc + 1) << ": " << ans << endl;
	}
	return 0;
}