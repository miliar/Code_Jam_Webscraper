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
	freopen("B-large.in", "r", stdin);
	freopen("answer.txt", "w", stdout);
	int tc;
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		long long l, t, n, c;
		cin >> l >> t >> n >> c;
		vector<long long> d(n);
		for(int i = 0; i < c; ++i)
		{
			int a;
			cin >> a;
			for(int k = 0; c*k+i < n; ++k)
			{
				d[c*k+i] = a;
			}
		}

		long long time = 0;
		int k = 0;
		while(k < n && time + 2*d[k] < t)
		{
			time += (d[k] << 1);
			++k;
		}
		long long res = 0;
		if(k < n)
		{
			if(time + 2*d[k] - t > 0)
			{
				d.push_back(time/2 + d[k] - t/2);
				++n;
			}
			sort(d.begin() + k + 1, d.end(), greater<int>());
			res += t;
			int i = k + 1;
			for(; i < n && l > 0; ++i, --l)
			{
				res += d[i];
			}
			for(; i < n; ++i)
			{
				res += (d[i] << 1);
			}
		}
		else
		{
			for(int i = 0; i < n; ++i)
			{
				res += (d[i] << 1);
			}
		}

		cout << "Case #" << Case + 1 <<": " << res << endl;
	}

	return 0;
}
