#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main()
{
	//freopen("b2.in", "r", stdin);
	//freopen("b2.out", "w", stdout);

	int t, n, s, p, ti;

	cin >> t;
	for (int k = 1; k <= t; k++)
	{
		cin >> n >> s >> p;
		int cnt = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> ti;
			int max = ti > 0 ? (ti + 4) / 3 : 0;
			int min = (ti + 2) / 3;

			if ( min >= p )
			{
				cnt++;
			}
			else if ( max >= p && s > 0 )
			{
				s--;
				cnt++;
			}
		}
		cout << "Case #" << k << ": " << cnt << endl;
	}

	return 0;
}
