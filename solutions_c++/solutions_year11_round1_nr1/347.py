#include <iostream>
#include <vector>
#include <stdint.h>

using namespace std;

void show(bool flag)
{
	if (flag)
		cout << "Possible" << endl;
	else
		cout << "Broken" << endl;
}

void solve()
{
	int64_t n;
	int pd, pg;
	cin >> n >> pd >> pg;
	if (pd == 100)
	{
		if (pg > 0)
			show(true); // 1/1, pg/100
		else
			show(false);
		return;
	}
	if (pd == 0)
	{
		if (pg == 100)
			show(false);
		else
			show(true); // 0/1, pg/100
		return;
	}
	// 0 < pd < 100
	if (pg == 0 || pg == 100)
	{
		show(false);
		return;
	}

	int x = 100;
	while (pd % 2 == 0 && x % 2 == 0)
	{
		pd /= 2;
		x /= 2;
	}
	while (pd % 5 == 0 && x % 5 == 0)
	{
		pd /= 5;
		x /= 5;
	}
	show(x <= n);
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

