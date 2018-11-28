#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

long long n, p, l, c;
int t;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		cin >> l >> p >> c;
		long long cur = (p + l - 1) / l;
		long long st = 1;
		long long temp = 0;
		while (st < cur)
		{
			st *= c;
			temp++;
		}
		st = 1;
		long long ans = 0;
		while (st < temp)
		{
			st *= 2;
			ans++;
		}
		cout << ans << endl;
	}
	return 0;
}
