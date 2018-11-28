#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef pair<int,int> ii;

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int tc;
	cin >> tc;

	for (int t = 1; t <= tc; t++)
	{
		int n,s,p;
		cin >> n >> s >> p;
		vector<ii> v(n);

		for (int i = 0; i < n; i++)
		{
			int x, d, r;
			cin >> x;

			d = x / 3;
			r = x % 3;

			if (r == 0) v[i] = make_pair(d,3);
			else v[i] = make_pair(d+1, r);			
		}

		//sort(v.begin(), v.end());
		//reverse(v.begin(), v.end());

		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			if (v[i].first >= p) ++ans;
			else if (s > 0 && v[i].first > 0 && v[i].second > 1 && v[i].first == p - 1)
			{
				++ans;
				--s;
			}
		}

		printf("Case #%d: %d\n", t, ans);
	}
}