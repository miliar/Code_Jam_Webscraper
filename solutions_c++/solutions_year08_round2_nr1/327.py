#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <list>
#include <numeric>
#include <bitset>
#include <ext/algorithm>
#include <ext/numeric>
#define fr(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define fo(_a,_n) fr(_a,0,_n)
#define all(_v) (_v).begin(),(_v).end()
#define sz size()
typedef long long LL; using namespace std; using namespace __gnu_cxx; 

int X[100010], Y[100010];
LL dp[100010][4][3][3];

int main()
{
	int N;
	scanf("%d", &N);
	for (int test = 1; test <= N; ++test)
	{
		// input and generate
		int n, A, B, C, D, x0, y0, M;
		scanf("%d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		
		int x = x0, y = y0;
		X[0] = x;
		Y[0] = y;
		for (int i = 1; i < n; ++i)
		{
			x = (LL)((LL)A * x + B) % M;
		  	y = (LL)((LL)C * y + D) % M;
			X[i] = x;
			Y[i] = y;
		}
		
		// solve
		memset(dp, 0, sizeof dp);
		dp[0][0][0][0] = 1;
		
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < 3; ++j)
			{
				for (int k = 0; k < 3; ++k)
				{
					for (int l = 0; l < 3; ++l)
					{
						if (dp[i][j][k][l] == 0) continue;
						dp[i + 1][j][k][l] += dp[i][j][k][l];
						dp[i + 1][j + 1][(k + X[i]) % 3][(l + Y[i]) % 3] += dp[i][j][k][l];
					}
				}
			}
		}
		LL res = 0;
		for (int i = 0; i <= n; ++i)
			res += dp[i][3][0][0];
		
		cout << "Case #" << test << ": " << res << endl;
	}
	
	return 0;
}
