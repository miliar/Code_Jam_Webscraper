#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int 
main()
{
	freopen("C-large.in", "r", stdin);
	freopen("2.txt", "w", stdout);
	int t;
	cin >> t;
	for(int q = 0; q < t; ++q)
	{
		int n;
		cin >> n;
		vector <int> a(n);
		unsigned long long ans = 0;
		for(int i = 0; i < n; ++i)
		{
			cin >> a[i];
			ans += a[i];
		}
		sort(a.begin(), a.end());
		ans -= a[0];

		vector <int> a1(0);
		vector <int> a2(0);
		for(int  i = 0; i < n; ++i)
		{
			a1.resize(0);
			while(a[i] != 1)
			{
				int q;
				q = a[i] % 2;
				a[i] /= 2;
				a1.push_back(q);
			}
			a1.push_back(a[i]);
			if(a1.size() > a2.size())
			{
				for(int  j = a2.size(); j < a1.size(); ++j)
				{
					a2.push_back(0);
				}
			}
			for(int j = 0; j < a1.size(); ++j)
			{
				a2[j] = a2[j] ^ a1[j];
			}
		}
		vector <int> a0(a2.size(), 0);
		cout << "Case #" << q + 1 << ": ";
		if(a0 == a2)
		{
			cout << ans << endl;
		}
		else
		{
			cout << "NO" << endl;
		}
	}
	return 0;
}
