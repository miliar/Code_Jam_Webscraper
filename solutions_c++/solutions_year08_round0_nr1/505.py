#include <iostream>
#include <string>
#include <map>
using namespace std;
const int MAX = 105;
const int INF = 100000000;

char str[MAX];
int cnt = 0;
map<string, int> ID;
int s, q;
int dp[1005][MAX];

int main (void)
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int T, Case = 1;
	scanf("%d", &T);
	while (T --)
	{
		string temp;
		ID.clear();
		cnt = 0;

		int i, j, k;
		scanf("%d", &s);
		gets(str);		//
		for (i = 0; i < s; ++ i)
		{
			gets(str);
			temp = str;
			ID[temp] = cnt++;
		}

		for (i = 0; i < q; ++ i)
			for (j = 0; j < s; ++ j)
				dp[i][j] = INF;

		scanf("%d", &q);
		gets(str);		//
		for (i = 0; i < q; ++ i)
		{
			gets(str);
			temp = str;
			k = ID[temp];
			if (i == 0)
			{
				for (j = 0; j < s; ++ j)
					if (j != k)
						dp[i][j] = 0;
			}
			else
			{
				int jj;
				for (jj = 0; jj < s; ++ jj)
				{
					if (jj == k)
					{
						dp[i][jj] = INF;
						continue;
					}
					else dp[i][jj] = dp[i-1][jj];
					for (j = 0; j < s; ++ j)
						if (j != jj && dp[i-1][j]+1 < dp[i][jj])
							dp[i][jj] = dp[i-1][j]+1;
				}
			}
		}

		int ans = INF;
		if (q == 0)
			ans = 0;
		else
		for (j = 0; j < s; ++ j)
			if (dp[q-1][j] != -1 && dp[q-1][j] < ans)
				ans = dp[q-1][j];
		
		printf("Case #%d: %d\n", Case++, ans);
	}
	return 0;
}