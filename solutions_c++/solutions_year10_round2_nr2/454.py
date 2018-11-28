#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int testCnt;
	cin >> testCnt;
	for (int T = 1; T <= testCnt; ++T)
	{
		int n, k, b, time;
		cin >> n >> k >> b >> time;
		vector<int> x, v;
		for (int i = 0; i < n; ++i)
		{
			int t; 
			cin >> t;
			x.push_back(t);
		}
		for (int i = 0; i < n; ++i)
		{
			int t; 
			cin >> t;
			v.push_back(t);
		}
		int res = 0, cnt = 0;
		for (int i = (int)x.size()-1; i >= 0 && cnt < k; --i)
		{
			if ((double)(b-x[i])/(float)v[i] > time)
				continue;
			++cnt;
			for (int j = i; j < (int)x.size(); ++j)
				if ((double)(b-x[j])/(float)v[j] > time)
					++res;
		}
		if (cnt < k)
			cout << "Case #" << T << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << T << ": " << res << endl;
	}
	return 0;
}