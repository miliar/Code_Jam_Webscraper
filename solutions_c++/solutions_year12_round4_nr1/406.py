#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tc = 0;
	cin >> tc;
	for (int t = 1 ; t <= tc; ++t) {
		vector <pair<int,int> > arr;
		int n;
		cin >> n;
		int d;
		arr.resize(n);
		for (int i=  0; i < n; ++i)
			cin >> arr[i].first >> arr[i].second;
		cin >> d;
		arr.push_back(make_pair(d,0));
		vector <int> can(n+1, -1);
		can[0] = arr[0].first;
		for (int i = 0; i < n; ++i)
		{
			if (can[i] < 0)
				continue;
			for (int j = i + 1; j <= n; ++j)
			{
				if (arr[j].first-arr[i].first > arr[i].second ||
					arr[j].first-arr[i].first > can[i])
					break;
				can[j] = max(can[j], min(arr[j].first-arr[i].first, arr[j].second));

			}
		}
		if (can[n] == 0)
			cout << "Case #" << t << ": YES\n";
		else
			cout << "Case #" << t << ": NO\n";
			
	}

	return 0;
}