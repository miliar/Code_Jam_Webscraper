#include <iostream>
#include <vector>

using namespace std;

vector <pair <char, int> > arr;

int sgn(int x)
{
	if(x == 0)
		return 0;
	if(x < 0)
		return -1;
	return 1;
}

int main()
{
	freopen("input.txt.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		int n;
		cin >> n;
		arr.resize(n);
		for(int i = 0; i < n; i++)
			cin >> arr[i].first >> arr[i].second;
		int pa = 1, pb = 1, ans = 0;
		for(int i = 0; i < n; i++)
		{
			if(arr[i].first == 'B')
			{
				int t = abs(pa - arr[i].second) + 1;
				ans += t;
				int next = -1;
				for(int j = i; j < n; j++)
					if(arr[j].first == 'O')
					{
						next = j;
						break;
					}
				pa = arr[i].second;
				if(next == -1)
					continue;
				if(abs(pb - arr[next].second) <= t)
					pb = arr[next].second;
				else
					pb += sgn(arr[next].second - pb) * t;
			}
			else
			{
				int t = abs(pb - arr[i].second) + 1;
				ans += t;
				int next = -1;
				for(int j = i; j < n; j++)
					if(arr[j].first == 'B')
					{
						next = j;
						break;
					}
				pb = arr[i].second;
				if(next == -1)
					continue;
				if(abs(pa - arr[next].second) <= t)
					pa = arr[next].second;
				else
					pa += sgn(arr[next].second - pa) * t;
			}
		}
		printf("Case #%d: %d\n", tc + 1, ans);
	}
	return 0;
}