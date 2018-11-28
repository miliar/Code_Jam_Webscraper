#include <iostream>
#include <vector>

using namespace std;

int
main()
{
	freopen("C-small-attempt0.IN", "r", stdin);
	freopen("1q2w3e.txt", "w", stdout);
	int t;
	cin >> t;
	for(int p = 0; p < t; ++p)
	{
		int n, l, h;
		cin >> n >> l >> h;
		vector <int> a(n);
		for(int  i = 0; i < n; ++i)
		{
			cin >> a[i];
		}
		bool f;
		int ans;
		for(int i = l; i <= h; ++i)
		{
			f = true;
			ans = i;
			for(int j = 0; j < n; ++j)
			{
				if(i % a[j] == 0)
				{
					continue;
				}
				else if(a[j] % i == 0)
				{
					continue;
				}
				else
				{
					f = false;
					break;
				}				
			}
			if(f == true)
			{
				break;
			}
		}
		if(f == true)
		{
			cout << "Case #" << p + 1 <<": " << ans << endl;
			continue;
		}
		else
		{
			cout << "Case #" << p + 1 <<": NO" << endl;
		}
	}
	return 0;
}