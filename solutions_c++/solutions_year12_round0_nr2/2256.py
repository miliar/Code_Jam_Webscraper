#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <map>

using namespace std;

void init()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
}

int main()
{
	init();
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int N, S, p;
		cin >> N >> S >> p;
		vector <int> dancers(N);
		for (int i = 0; i < N; ++i)
		{
			cin >>  dancers[i];
		}
		sort(dancers.rbegin(), dancers.rend());
		int ans = 0;
		int possible = 0;
		for (int i = 0; i < N; ++i)
		{
			if (dancers[i] >= 3 * p - 2)
			{
				++ans;
			}
			else
			{
				if ((p > 1) && (dancers[i] >= 3 * (p - 2) + 2))
				{
					++possible;
				}
			}
		}
		ans += min(possible, S);
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}
