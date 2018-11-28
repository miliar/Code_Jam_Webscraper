#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <string>
#include <sstream>
#include <limits>
#include <cmath>
#include <cassert>
using namespace std;

int n, l, h;

int freq[100];

void solve ()
{
	cin >> n >> l >> h;

	for (int i = 0; i < n; i += 1)
	{
		cin >> freq[i];
	}

	for (int i = l; i <= h; i += 1)
	{
		bool poss = true;

		for (int j = 0; poss && j < n; j += 1)
		{
			if (i <= freq[j])
			{
				poss = freq[j] % i == 0;
			}
			else
			{
				poss = i % freq[j] == 0;
			}
		}

		if (poss)
		{
			cout << i << endl;
			return;
		}
	}

	cout << "NO" << endl;
}

int main ()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i += 1)
	{
		cout << "Case #" << i+1 << ": ";
		solve ();
	}
}

