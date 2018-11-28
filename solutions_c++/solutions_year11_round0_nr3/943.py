#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		int n;
		cin >> n;
		vector <int> arr(n);
		for(int i = 0; i < n; i++)
			cin >> arr[i];
		bool ok = true;
		for(int i = 0; i < 25; i++)
		{
			bool v = 0;
			for(int j = 0; j < n; j++)
				v ^= ((arr[j] & (1 << i)) > 0);
			if(v)
				ok = false;
		}
		printf("Case #%d: ", tc + 1);
		if(!ok)
		{
			cout << "NO" << endl;
			continue;
		}
		int mi = arr[0], sum = arr[0];
		for(int i = 1; i < n; i++)
		{
			mi = min(mi, arr[i]);
			sum += arr[i];
		}
		cout << sum - mi << endl;
	}
	return 0;
}