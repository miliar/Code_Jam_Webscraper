#include <iostream>
#include <map>
using namespace std;
int dp[1024][1024];
const int oo = 1000000000;
int main()
{
	int n;
	cin >> n;
	for (int t=0; t<n; t++)
	{
		map<string, int> mp;
		int s;
		cin >> s;
		string line;
		getline(cin, line);
		for (int i=0; i<s; i++)
		{
			getline(cin, line);
			mp[line] = i;
		}
		int q;
		cin >> q;
		for (int i=1; i<=q; i++)
			for (int j=0; j<s; j++)
				dp[i][j] = oo;
		getline(cin, line);
		for (int i=0; i<q; i++)
		{
			getline(cin, line);
			int act = -1;
			if (mp.count(line))
				act = mp[line];
			for (int j=0; j<s; j++)
				if (j != act)
					dp[i+1][j] = min(dp[i+1][j], dp[i][j]);
				else
				{
					for (int k=0; k<s; k++)
						if (k != act)
							dp[i+1][k] = min(dp[i+1][k], dp[i][j] + 1);
				}
		}
		printf("Case #%d: %d\n", t+1, *min_element(dp[q], dp[q]+s));
	}
	return 0;
}
