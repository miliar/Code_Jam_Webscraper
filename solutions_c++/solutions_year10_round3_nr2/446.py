#include<iostream>
#include<vector>
#include<math.h>
using namespace std;

int dp[1001][1001][11];
int c;
int solve(int l, int p)
{
	if(dp[l][p][c] != -1)
	{
	//	cout << "used " << endl;
		return dp[l][p][c];
	}
	int best = 100000;
	for(int i = l+1; i < p;i ++)
	{
		int count;
		if( i*c >= p && l*c >= i)
		{
			count = 1;
			dp[l][p][c] = 1;
			return 1;
		}
		else
		{
			count = 1 + max( solve(l, i), solve(i, p));
		}
		
		best = min(best,count);
	}
	
	dp[l][p][c] = best;
	return best;
}

int main()
{
	
	int T;
	cin >> T;
	for(int z = 0; z < 11;z++)
	{
		for(int i = 0; i < 1001;i++)
		{
			for(int j = 0; j < 1001;j++)
			{
				dp[i][j][z] = -1;
			}
		}
	}
	
	for(int t = 0; t < T;t++)
	{
		int l, p;
		cin >> l >> p >> c;
		
		
		if(l*c >= p)
		{
			cout << "Case #" << t+1 << ": " << 0 << endl;
		}
		else
			cout << "Case #" << t+1 << ": " << solve(l,p) << endl;
	
	
	
	
	
	
	}


}
