#include <iostream>
#include <sstream>
#include <string>
#include <set>

using namespace std;

set<int> hash;
set<int> yes[11];
int tot;
int bs[20];

int calc(int x, int base)
{
	int y = 0;
	while (x > 0)
	{
		y += (x%base)*(x%base);
		x /= base;
	}
	if (y == 1) return y;
	if (hash.count(y)) return y;
	hash.insert(y);
	return calc(y, base);
}

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	for (int i = 1; i <= 50000; i++)
	{
		for (int j = 2; j <= 10; j++)
		{
			hash.clear();
			hash.insert(i);
			if (calc(i, j) == 1) yes[j].insert(i);
		}
	}
	int T;
	string s;
	cin >> T;
	getline(cin, s);
	for (int i = 1; i <= T; i++)
	{
		getline(cin, s);
		istringstream sin(s);
		int x;
		tot = 0;
		while (sin >> x) bs[tot++] = x;
		for (int j = 2; j <= 50000; j++)
		{
			bool flag = true;
			for (int k = 0; k < tot; k++)
				if (!yes[bs[k]].count(j))
				{
					flag = false;
					break;
				}
			if (flag)
			{
				cout << "Case #" << i << ": " << j << endl;
				break;
			}
		}
	}
}