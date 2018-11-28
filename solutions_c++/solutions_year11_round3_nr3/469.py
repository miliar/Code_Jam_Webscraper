#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cmath>

using namespace std;

int freq[1000], n;

bool check (int x)
{
	for (int i = 0; i < n; i++)
	{
		if (freq[i] < x && x % freq[i] != 0)
			return false;
		else if (freq[i] > x && freq[i] % x != 0)
			return false;
	}

	return true;
}

int main()
{
	int ncases, l, h;

	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++)
	{
		cin >> n >> l >> h;
		for (int i = 0; i < n; i++)
		{
			cin >> freq[i];
		}

		int found = -1;
		for (int i = l; i <= h; i++)
		{
			if (check(i))
			{
				found = i;
				break;
			}
		}

		if (found == -1)
			printf("Case #%i: NO\n", caseno);
		else
			printf("Case #%i: %i\n", caseno, found);
	}
}
