#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

// 4 2 6 5 1 3
// {1,5,4}
// {6,3}

// 3,2,5,6,1,4
// {3,5,1}
// {6,4}

// ans = 3.0+2.0 = 5.0

main ()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		int n;
		cin >> n;

		int arr[n];

		for (int i = 0; i < n; i++) cin >> arr[i];

		int done[n];
		memset(done,0,sizeof(done));
		
		double ans = 0.0;
		for (int i = 0; i < n; i++)
		{	
			if (done[i]) continue;			
			vector <int> v;
			v.push_back(arr[i]);
			int x = arr[i]-1;
			while (x != i)
			{
				v.push_back(arr[x]);
				done[x] = 1;
				x = arr[x]-1;
			}
			if (v.size() == 1) ans += 0.0;
			else ans += v.size();
		}
		cout << "Case #" << T << ": " << ans << ".000000\n";
	}
}
