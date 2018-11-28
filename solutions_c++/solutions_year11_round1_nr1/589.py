#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

bool Solve()
{
	int pd, pg, tot = 100;
	long long n;
	cin >> n >> pd >> pg;
	if (pd < pg && pg == 100)
		return false;
	else if (pd > pg && pg == 0)
		return false;
	while (pd > 0)
	{
		if (pd % 2 == 0 && tot % 2 == 0)
		{
			pd /= 2;
			tot /= 2;
		}
		else if (pd % 5 == 0 && tot % 5 == 0)
		{
			pd /= 5;
			tot /= 5;
		}
		else
			break;
	}
	//cout << tot << "" << pd << endl;
	if (tot <= n || pd == 0)
		return true;
	return false;
	
}

int main()
{
	int t, f;
	bool res;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> t;
	for (f = 1; f <= t; f++)
	{
		res = Solve();
		printf("Case #%d: %s\n", f, res ? "Possible" : "Broken");
	}
	return 0;
}

