#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int n;

bool Cmp(const pair <int, string> &p1, const pair <int, string> &p2)
{
	int l1 = -1, l2 = -1;
	for(int i = 0; i < n; i++)
		if(p1.second[i] == '1')
			l1 = i;
	for(int i = 0; i < n; i++)
		if(p2.second[i] == '1')
			l2 = i;
	if(l1 < l2)
		return true;
	if(l1 > l2)
		return false;
	return p1.first < p2.first;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cin >> n;
		vector <pair <int, string> > m;
		vector <int> arr;
		arr.resize(n);
		m.resize(n);
		for(int j = 0; j < n; j++)
		{
			cin >> m[j].second;
			m[j].first = j;
		}
//		sort(m.begin(), m.end(), Cmp);
		for(int j = 0; j < n; j++)
		{
			arr[j] = 0;
			for(int k = 0; k < n; k++)
				if(m[j].second[k] == '1')
					arr[j] = k;
		}
		int ans = 0;
		bool ok = true;
		int cnt = 0;
		for(int j = 0; j < n; j++)
		{
			ok = true;
			for(int k = j; k < n && ok; k++)
				if(arr[k] <= j)
				{
					ok = false;
					if(k <= j)
						break;
					for(int l = k - 1; l >= 0; l--)
					{
						swap(arr[l], arr[l + 1]);
						ans++;
						if(l <= j)
							break;
					}
				}
		}
/*		while(ok)
		{
			ok = false;
			for(int j = 0; j < n; j++)
				if(arr[j] > j && arr[j] > arr[j + 1])
				{
					swap(arr[j], arr[j + 1]);
					ok = true;
					ans++;
				}
		}*/
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}