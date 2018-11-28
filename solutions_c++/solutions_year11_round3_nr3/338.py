#include<cstdio>
#include<iostream>

using namespace std;

int solve()
{
	int n, l, h;
	int i, j;
	bool FLAG;
	int answ = 0;

	cin >> n >> l >> h;

	int ar[n];

	for (i = 0; i < n; i++)
	{
		cin >> ar[i];
	}

	for (i = l; i <= h; i++)
	{
		FLAG = 1;

		for (j = 0; j < n; j++)
		{
			if (i % ar[j] == 0 || ar[j] % i == 0) continue;
			FLAG = false;
		}

		if (FLAG) {
			answ = i;
			break;
		}
	}

	return answ;
}

int main()
{
	int t;
	int i;
        int ans;

	cin >> t;
	
	for (i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";

		if (ans = solve()) {
			cout << ans << '\n';
		} else 
			cout << "NO\n";
	}

	return 0;
}
