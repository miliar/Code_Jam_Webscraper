#include <iostream>
#include <queue>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("res.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc ++)
	{
		int n;
		cin >> n;
		int ans = 0;
		int x;
		for (int i = 0; i < n; i ++)
		{
			cin >> x;
			if (x != i+1)
				ans ++;
		}

		cout << "Case #" << tc <<": " <<ans << endl;
	}

	return 0;
}
