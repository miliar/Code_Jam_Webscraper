#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;

	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		int n, i, j, k, D;
		cin >> n;
		vector<int> d(n), l(n);
		for(i = 0; i < n; i++)
			cin >> d[i] >> l[i];
		cin >> D;
		vector<int> best(n, 0);
		best[0] = d[0];
		for(i = 0; i < n; i++)
			for(j = i + 1; j < n; j++)
				if (d[j] - d[i] <= best[i])
					best[j] = max(best[j], min(l[j], d[j] - d[i]));
		cout << "Case #" << t << ": ";
		bool good = false;
		for(i = 0; i < n; i++)
			if (best[i] + d[i] >= D)
				good = true;
		cout << (good ? "YES" : "NO") << endl;
	}

	return 0;
}