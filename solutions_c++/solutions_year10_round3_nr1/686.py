#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <cstring>
#include <map>
using namespace std;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;
	for(int nt = 1; nt <= T; nt++)
	{
		vector< pair<int, int> > v;
		int n;
		cin >> n;
		int a, b;
		for(int i = 0; i < n; i++)
		{
			cin >> a >> b;
			v.push_back(make_pair(a, b));
		}
		int y = 0;
		for(int i = 0; i < v.size(); i++)
		{
			for(int j = 0; j < v.size(); j++)
			{
				if(v[i].first < v[j].first && v[i].second > v[j].second)
					y++;
				if(v[i].first > v[j].first && v[i].second < v[j].second)
					y++;
			}
		}
		cout << "Case #" << nt << ": " << y / 2 << endl;
	}

	return 0;
}