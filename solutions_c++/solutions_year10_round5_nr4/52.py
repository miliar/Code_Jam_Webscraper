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

int N, B;

const int MOD = 1000000007;

int has[10][10];

int solve(int cur, int last)
{
	if (cur == N)
		return 1;

	int ans = 0;

	for (int res = last + 1; res + cur <= N; res++)
	{
		int x = 0;
		int k = res;
		bool ok = true;
		while (k)
		{
			if (has[x][k % B])
			{
				ok = false;
				break;;
			}
			k /= B;
			x++;
		}

		if (!ok)
			continue;

		x = 0;
		k = res;
		while (k)
		{
			has[x][k % B] = true;
			k /= B;
			x++;
		}
		ans += solve(cur + res, res);
		if (ans >= MOD)
			ans-= MOD;

		x = 0;
		k = res;
		while (k)
		{
			has[x][k % B] = false;
			k /= B;
			x++;
		}

	}

	return ans;
}

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);

	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		
		scanf("%d %d", &N, &B);

		int res = solve(0, 0);

		printf("Case #%d: %d\n", nTest, res);
		
		fflush(stdout);
	} 


	return 0;
}


