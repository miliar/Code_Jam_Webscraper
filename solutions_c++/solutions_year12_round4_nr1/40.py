#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <ctime>
using namespace std;

int n;
int d[20001], len[20001];
int dp[20001];

int MAIN()
{
	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cin >> n;
		for(int i = 1; i <= n; i++)
			cin >> d[i] >> len[i];
		n ++;
		cin >> d[n];
		len[n] = 1;
		dp[1] = d[1];
		for(int i = 2; i <= n; i++)
		{
			dp[i] = 0;
			for(int j = 1; j < i; j++)
			{
				if(d[j] + dp[j] >= d[i])
					dp[i] = max(dp[i], min(d[i] - d[j], len[i]));
			}
		}
		cout << "Case #" << caseID << ": ";
		if(dp[n] > 0)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}

int main()
{
	#ifdef LOCAL_TEST
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	//int START_TIME = clock();
	#endif
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int RUN_RESULT = MAIN();
	/*#ifdef LOCAL_TEST
	cout << endl;
	cout << "[Time Used] " << clock() - START_TIME << " ms." << endl;
	#endif*/
	return RUN_RESULT;
}
