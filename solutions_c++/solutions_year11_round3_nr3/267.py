#include<iostream>
#include<stdio.h>

using namespace std;

int cas()
{
	int n, l, h, i, j;
	cin >> n >> l >> h;
	int ar[n];
	for (i = 0; i < n; i++)
	{
		cin >> ar[i];
	}
	bool flag;
	int ans = 0;
	for (i = l; i <= h; i++)
	{
		flag = true;
		for (j = 0; j < n; j++)
		{
			if (i % ar[j] == 0 || ar[j] % i == 0) continue;
			flag = false;
		}
		if (flag)
		{
			ans = i;
			break;
		}
	}
	return ans;
}

int main()
{
	int t;
	cin >> t;
	int i, ans;
	for (i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		if (ans = cas())
		{
			cout << ans << endl;
		}
		else cout << "NO\n";
	}
	return 0;
}
