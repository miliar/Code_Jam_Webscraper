#include <iostream>
#include <vector>
using namespace std;
const int maxx = 100;

char s[100]; 
int a[100];

int dp[100][1<<11];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for(int z = 1; z <= t; ++z)
	{
		int n, m;
		scanf("%d%d", &n, &m);
		memset(a, 0, sizeof a);
		for(int i = 1; i <= n; ++i)
		{
			scanf("%s", s);
			for(int j = 0; j < m; ++j)
				if(s[j] == 'x')
					a[i] |= (1 << j);
		}
		memset(dp, 0, sizeof dp);
		dp[0][0] = 0;
		for(int i = 1; i <= n; ++i)
		{
			for(int j = 0; j < (1<<m); ++j) if((j & a[i]) == 0)
			{
				bool fl = true;
				for(int k = 1; k < m; ++k)
					if(((j>>(k-1))&1) == 1 && ((j>>(k))&1) == 1)
					{
						fl = false;
						break;
					}
				if(!fl) continue;
				int bit = 0;
				for(int k = 0; k < m; ++k)
					if((j>>k)&1)
						bit++;
				for(int k = 0; k < (1<<m); ++k) if(((j<<2)&(k<<1))==0 && ((j<<1)&(k<<2))==0)
					dp[i][j] = max(dp[i][j], dp[i-1][k]);
				dp[i][j] += bit;
			}
		}
		int maxx = 0;
		for(int i = 0; i < (1<<m); ++i)
			maxx = max(maxx, dp[n][i]);
		cout << "Case #" << z << ": " << maxx << endl;
	}

	return 0;
}