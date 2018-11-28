#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <cmath>

using namespace std;

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int t;
	cin >> t;
	for (int p = 1; p <= t; p++)
	{
		int s;
		int cnt = 0;
		cin >> s;
		vector<string> v(s);
		if (s != 0)
			getline(cin, v[0]);
		for (int i = 0; i < s; i++)
			getline(cin, v[i]);
		int q;
		cin >> q;
		vector<string> a(q);
		if (q != 0)
		getline(cin, a[0]);
		for (int i = 0; i < q; i++)
			getline(cin, a[i]);
		bool fl = true;
		int pos = 0;
		while (fl)
		{
			vector<int> d(s, q+10);
			for (int i = pos; i < q; i++)
				for (int j = 0; j < s; j++)
				{
					if (v[j] == a[i])
						d[j] = min(d[j], i);
				}
			int maxt = 0;
			for (int i = 0; i < s; i++)
			{
				if (maxt < d[i])
				{
					maxt = d[i];
					pos = i;
				}
			}
			if (maxt == q+10)
			{
				fl = false;
			}
			else
			{
				pos = maxt;
				cnt++;
			}
		}
		cout << "Case #" << p << ": " << cnt << endl;
	}
	return 0;
}