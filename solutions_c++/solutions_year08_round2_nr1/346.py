#include <iostream>
using namespace std;

typedef long long LL;

int TESTS, N;
LL A, B, C, D, X, Y, MOD, dp[3][3], ans;

void Read()
{
	cin >> N >> A >> B >> C >> D >> X >> Y >> MOD;
}

LL comb3(LL a)
{
	return (((LL(a - 2) * LL(a - 1) / 2LL) * LL(a)) / 3LL);
}

void Solve()
{
	ans = 0;
	memset(dp, 0, sizeof(dp));
	
	dp[X % 3][Y % 3] ++;
	
	for(int i = 1; i < N; i ++)
	{
		X = (A * X + B) % MOD;
		Y = (C * Y + D) % MOD;
		
		dp[X % 3][Y % 3] ++;
	}
	
	for(int i = 0; i < 3; i ++)
	{
		ans += comb3(dp[i][0]) + comb3(dp[i][1]) + comb3(dp[i][2]);
		ans += dp[i][0] * dp[i][1] * dp[i][2];
	}
	
	for(int i = 0; i < 3; i ++)
	{
		ans += dp[0][i] * dp[1][i] * dp[2][i];
	}
	
	ans += dp[0][0] * dp[1][1] * dp[2][2];
	ans += dp[0][0] * dp[1][2] * dp[2][1];
	ans += dp[0][1] * dp[1][0] * dp[2][2];
	ans += dp[0][1] * dp[1][2] * dp[2][0];
	ans += dp[0][2] * dp[1][0] * dp[2][1];
	ans += dp[0][2] * dp[1][1] * dp[2][0];
}


void Write(const int test)
{
	cout << "Case #" << test << ": " << ans << "\n";
}

int main()
{
	cin >> TESTS;
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve();
		
		Write(i);
	}
//	system("pause");
	
	return 0;
}
/*
1
6 2 0 2 1 1 2 11
*/
