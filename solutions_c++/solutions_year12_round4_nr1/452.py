#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;


int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int n;
		cin >> n;
		int pos[10000];
		int len[10000];
		for (int i = 0; i < n; ++i)
			cin >> pos[i] >> len[i];
		int dist;
		cin >> dist;
		int dp[10000];
		dp[0] = pos[0];
		for (int i = 1; i < n; ++i)
		{
			dp[i] = 0;
			for (int j = 0; j < i; ++j)
			{
				if (pos[j] + dp[j] < pos[i])
					continue; // Cannot reach when swinging
				int newDp = pos[i] - pos[j];
				if (newDp > len[i])
				{
					dp[i] = len[i];
					break;
				}
				if (newDp > dp[i])
					dp[i] = newDp;
			}
		}
		bool possible = false;
		for (int i = 0; i < n; ++i)
		{
			if (pos[i] + dp[i] >= dist)
			{
				possible = true;
				break;
			}
		}
		cout << "Case #" << (t+1) << ": " << (possible ? "YES" : "NO") << endl;
	}
	return 0;
}
