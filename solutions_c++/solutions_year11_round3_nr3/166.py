#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("answer.txt", "w", stdout);
	int tc;
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		long long n, l, h;
		cin >> n >> l >> h;
		vector<int> f(n);
		for(int i = 0; i < n; ++i)
		{
			cin >> f[i];
		}
		int ans = -1;
		for(int i = l; i <= h; ++i)
		{
			bool ok = true;
			for(int j = 0; j < n; ++j)
			{
				if(f[j] % i != 0 && i % f[j] != 0)
				{
					ok = false;
					break;
				}
			}
			if(ok)
			{
				ans = i;
				break;
			}
		}

		
		if(ans < 0)
			cout << "Case #" << Case + 1 <<": " << "NO" << endl;
		else
			cout << "Case #" << Case + 1 <<": " << ans << endl;
	}

	return 0;
}
