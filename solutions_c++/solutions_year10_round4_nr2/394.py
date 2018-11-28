#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;
int test , i , j , n , m , k;
int a[200000] , p[200000];
int dp[30000][20];
int main()
{
	freopen("c:/input.txt" , "r" , stdin);
	freopen("c:/output.txt" , "w" , stdout);
	cin>>test;
	for (int tt = 1; tt <= test; tt++)
	{
		cin>>n;
		int raod = (1<<n);
		for (i = raod + raod - 1; i >= 1; i--)
			cin>>p[i];

		for (i = 0; i <= raod + raod; i++)
			for (j = 0; j <= 10; j++)
				dp[i][j] = 1000000000;

		for (j = raod; j < raod + raod; j++)
			dp[j][p[j]] = 0;


		for (i = raod - 1; i >= 1; i--)
		{
			int l = 2*i;
			int r = 2*i + 1;
			for (j = 0; j <= 10; j++)
				for (k = 0; k <= 10; k++)
				{
					if (j > 0 && k > 0)
					{
						dp[i][min(k , j) - 1] = min (dp[i][min(k , j) - 1] ,  dp[l][j] + dp[r][k]);
					}

					dp[i][min(k , j)] = min(dp[i][min(k , j)] ,  dp[l][j] + dp[r][k] + p[i]);
				}
		}

		int ans = 2000000000;
		for (i = 0; i <= 10; i++)
			ans = min(ans , dp[1][i]);

		


		cout<<"Case #"<<tt<<": "<<ans<<endl;;
	}
	return 0;
}