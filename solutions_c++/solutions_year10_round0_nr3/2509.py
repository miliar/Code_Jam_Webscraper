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
		int r, k, n;
		cin >> r >> k >> n;
		vector <int> arr(n);
		for(int i = 0; i < n; i++)
			cin >> arr[i];
		vector <int> sum(n, 0), to(n);
		for(int i = 0; i < n; i++)
		{
			if(arr[i] > k)
			{
				to[i] = i;
				continue;
			}
			sum[i] = arr[i];
			to[i] = (i + 1) % n;
			for(int j = i + 1; j % n != i; j++)
				if(sum[i] + arr[j % n] > k)
				{
					to[i] = j % n;
					break;
				}
				else
					sum[i] += arr[j % n];
		}
		int now = 0;
		long long ans = 0;
		for(int i = 0; i < r; i++)
		{
			ans += sum[now];
			now = to[now];
		}
		printf("Case #%d: ", tc + 1);
		cout << ans << endl;
	}
	return 0;
}