#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <numeric>

#define all(x) x.begin() , x.end()
#define sz(x) ((int) x.size())
#define INF 0x7fffffff
#define LL long long
#define LD long double
#define VI vector<int>
#define VS vector<string>

#define MOD 100003;
using namespace std;

int dp[501][501];
int ncr[501][501];

void init()
{
	ncr[0][0] = 1;
	ncr[1][0] = ncr[1][1] = 1;
	for(int i=2 ; i<=500 ; i++)
	{
		for(int j=0 ; j<=i ; j++)
		{
			if(j==0 || j == i)
				ncr[i][j]=1;
			else
				ncr[i][j] = (ncr[i-1][j] + ncr[i-1][j-1])%MOD;
		}
	}
}

void process()
{
	for(int i=2 ; i<=500 ; i++)
		dp[2][1] = 1;

	for(int i=3 ; i<=500 ; i++)
	{
		dp[i][1]=1;
		for(int l=2 ; l<i ; l++)
		{
			if(l == i-1) dp[i][l]=1;

			else
			{
				int k=l-1;
			
				while(k>=1 &&  ((l-1-k) <= (i-l-1)))
				{
					int add = (dp[l][k] * ncr[i-l-1][l-1-k])%MOD;
					dp[i][l] = ( dp[i][l] +  add)%MOD;
					k--;
				}
			}

			/*if(i<=6)
				cout << i << " " << l << " " << dp[i][l] << endl;*/
		}	
	}
}

int main()
{
	init();
	process();
	int Te;
	cin >> Te;
	for(int te=0 ; te<Te  ; te++)
	{
		cout << "Case #"<<te+1 << ": ";
		int n;
		cin >> n;
	
		int res=0;
		for(int i=1 ; i<=n-1 ; i++)
			res  = (res+dp[n][i])%MOD;
		cout << res << endl;
	}
}
