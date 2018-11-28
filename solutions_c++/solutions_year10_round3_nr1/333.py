#include <iostream>
#include <map>
#include <vector>
#include <utility>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, t;
	vector<pair<int, int>> v;
	cin >> t;
	for (int tc = 0; tc < t; ++tc)
	{
		cin >> n;	
		v.resize(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i].first >> v[i].second;
		}
		int count = 0;
		for (int i = 0; i < n; ++i)
		{
			for (int j = i + 1; j < n; ++j)
			{
				if ((v[i].first - v[j].first) * (v[i].second - v[j].second) < 0)
					++count;
			}
		}

		cout << "Case #" << (tc + 1) << ": " << count << endl;
		
		/*if (pass < k)
			cout << "Case #" << (j + 1) << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << (j + 1) << ": " << s << endl;*/
	}
	return 0;
}