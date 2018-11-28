#include <iostream>
#include <string>
#include <vector>

using namespace std;

string SQ[1000], SE[100];
int dp[1001][101];

int main()
{
	int n, m, kk, min;
	
	freopen("out.txt","w",stdout);
	freopen("4.txt","r",stdin);
	
	cin >> n;
	
	for (int ii = 1; ii <= n; ++ii)
	{
		cin >> m;
		getchar();
		
		memset(dp, 0, sizeof(dp));
		
		for (int i = 0; i < m; ++i)
		{
			string str;
			getline(cin, str);
			SE[i] = str;
		}
		
		cin >> kk;
		getchar();		
		
		for (int i = 0; i < kk; ++i)
		{
			string str;
			getline(cin, str);
			SQ[i] = str;
		}
		
		if (!kk) 
		{
			printf("Case #%d: 0\n", ii);
			continue;
		}
		
		int flag = 0;
		
		for (int i = 0; i < m; ++i)
		{	
			int j = 0;
			
			while (SQ[j] != SE[i] && j < kk - 1) ++j;
			
			if (SQ[j] != SE[i] && j == kk - 1) ++j;
			
			dp[0][i] = j - 1;
			
			if (j == kk)	flag = 1;	
		}
		
		if (flag) 
		{
			printf("Case #%d: 0\n", ii);
			continue;
		}
		
		flag = 0;
		
		for (int i = 1;;++i)
		{
			for (int j = 0; j < m; ++j)
			{
				for (int k = 0; k < m; ++k)
				if (dp[i - 1][k] >= 0)
				{
					if (k == j) continue;
					
					int l = dp[i - 1][k] + 1;
						
					while (SQ[l] != SE[j] && l < kk - 1) ++l;
					
					if (SQ[l] != SE[j] && l == kk - 1) ++l;
					
					if (dp[i][j] < l - 1)
					{
						dp[i][j] = l - 1;
						if (l == kk)
						{	
							min = i;
							flag = 1;
							break;
						}
					}
				}
				if (flag) break;
			}
			if (flag) break;
		}
		
		printf("Case #%d: %d\n", ii, min);
	}
}
