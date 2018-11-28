#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

const int MOD = 100003;

int BitCount(int a) 
{ 
	int res = 0; 
	while (a > 0) 
	{ 
		++res; 
		a = a & (a - 1); 
	} 
	return res; 
} 

int powmod(int a, int b, int MOD)
{
	if (b == 0) return 1;
	ll res = powmod(a, b / 2, MOD);
	res = (res * res) % MOD;
	if (b % 2)
		res = (res * a) % MOD;
	return res;
}

const int MAX_N = 502;

ll Choose[MAX_N][MAX_N];
ll dp[MAX_N + 1][MAX_N + 1];


int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);

	for( int i = 0; i < MAX_N; ++i ) 
	{ 
		Choose[i][0] = 1; 
		for( int j = 1; j <= i; ++j ) 
			Choose[i][j] = ( Choose[i-1][j-1] + Choose[i-1][j] ) % MOD; 
	}

	dp[2][2] = 0;
	dp[2][1] = 1;
	dp[2][0] = 0;	

	for (int n = 3; n <= MAX_N; n++)
	{
		for (int cnt = 1; cnt < n; cnt++)
		{
			if (cnt == 1)
			{
				dp[n][cnt] = 1;
				continue;
			}
			
			ll total = 0;
			for (int j = 1; j < cnt; j++)
			{
				total = (total + dp[cnt][j] * (Choose[n - cnt - 1][cnt - j - 1]) % MOD) % MOD;
			}
			dp[n][cnt] = total;

		}

	}


	int nTestCount;
	scanf("%d", &nTestCount);

	for (int nTest = 1; nTest <= nTestCount; nTest++)
	{
		int N;
		scanf("%d", &N);

		int res = 0;

		for (int j = 1; j < N; j++)
			res = (res + dp[N][j]) % MOD;		

		printf("Case #%d: %d\n", nTest, res);

		fflush(stdout);
	}
 

	return 0;
}


