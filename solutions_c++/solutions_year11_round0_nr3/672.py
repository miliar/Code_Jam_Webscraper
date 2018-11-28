#include <iostream>
#include <algorithm>
using namespace std;

main ()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		int n;
		cin >> n;

		int arr[n];

		long long x = 0;
		long long sum = 0;
		for (int i = 0; i < n; i++) 
		{
			cin >> arr[i];
			x ^= arr[i];
			sum += arr[i];
		}
		sort(arr,arr+n);
		cout << "Case #" << T << ": ";
		if (x != 0) cout << "NO\n";
		else
		{
			cout << sum-arr[0] << "\n";
		}
	}
}
