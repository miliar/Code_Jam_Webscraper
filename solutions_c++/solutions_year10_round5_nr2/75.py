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
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;


inline void checkMin(int& a, int b)
{
	if (a > b) a = b;
}
inline void checkMin(ll& a, ll b)
{
	if (a > b) a = b;
}

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);

	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		 
		ll L;
		int N;
		cin >> L >> N;

		vector<int> x(N);

		rep(i, N) cin >> x[i];

		sort(all(x));

		int MAX_BUILD = 100000;
		vector<ll> dp(MAX_BUILD, LLONG_MAX);
		dp[0] = 0;

		rep(i, N)
		{
			for (int j = 0; j < MAX_BUILD - x[i]; j++)
			{
				if (dp[j] == LLONG_MAX)
					continue;

				checkMin(dp[x[i] + j], dp[j] + 1);
			}
		}


		ll ans = LLONG_MAX;

		for (int i = 0; i < N; i++)
		{
			ll largest = x[i];
			ll cnt = L / largest;

			while (true)
			{
				if (L - cnt * largest >= MAX_BUILD)
					break;
				if (dp[L - cnt * largest] != LLONG_MAX)
				{
					ll res = cnt + dp[L - cnt * largest];
					checkMin(ans, res);
				}
				cnt--;
			}
		}
		
		

		if (ans != LLONG_MAX)
			printf("Case #%d: %lld\n", nTest, ans);
		else
		{

			printf("Case #%d: IMPOSSIBLE\n", nTest);
		}
		fflush(stdout);
	} 


	return 0;
}


