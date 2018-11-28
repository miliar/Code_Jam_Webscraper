#include <iostream>

using namespace std;

static const int maxn = 1000;

int a[maxn + 1];
bool flag[maxn + 1];

double solve()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i)
	{
		cin >> a[i];
		flag[i] = false;
	}
	double ans = 0;
	for (int i = 1; i <= n; ++i)
	{
		if (flag[i])	continue;
		int j = i, l = 0;
		do
		{
			flag[j] = true;
			j = a[j];
			++l;
		} while (j != i);
		cerr << "l = " << l << endl;
		ans += l == 1 ? 0 : l;
	}
	return ans;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		cout << "Case #" << i << ": " << solve() << endl;
	return 0;
}

