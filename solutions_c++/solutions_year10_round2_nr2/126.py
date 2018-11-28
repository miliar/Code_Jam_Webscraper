#include <iostream>
#include <vector>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		printf("Case #%d: ", tc + 1);
		int n, k, b, t;
		cin >> n >> k >> b >> t;
		vector <int> x(n), v(n);
		for(int i = 0;  i< n; i++)
			cin >> x[i];
		for(int i = 0; i < n; i++)
			cin >> v[i];
		vector <bool> arr(n, false);
		for(int i = n - 1; i >= 0; i--)
		{
			if((b - x[i]) % v[i] == 0)
			{
				if((b - x[i]) / v[i] <= t)
					arr[i] = true;
				continue;
			}
			double need = double(b - x[i]) / v[i];
			if(need <= t)
				arr[i] = true;
		}
		int ans = 0;
		for(int j = n - 1; j >= 0 && k > 0; j--)
			if(arr[j])
			{
				for(int g = j + 1; g < n; g++)
					if(!arr[g])
						ans++;
				k--;
			}

		if(k > 0)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		cout << ans << endl;
	}
	return 0;
}