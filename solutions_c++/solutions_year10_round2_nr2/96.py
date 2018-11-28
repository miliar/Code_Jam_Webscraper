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

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);

	int nTestCount;
	scanf("%d", &nTestCount);

	for (int nTest = 1; nTest <= nTestCount; nTest++)
	{
		int N, K, B, T;
		scanf("%d %d %d %d", &N, &K, &B, &T);

		vector<int> x(N);
		rep(i, N)
		{
			scanf("%d", &x[i]);
		}
		vector<int> v(N);
		rep(i, N)
		{
			scanf("%d", &v[i]);
		}


		vector<int> maxSwap(N);

		for (int i = N - 1; i >= 0; i--)
		{
			if (B - x[i] > T * v[i])
			{
				maxSwap[i] = 100000;
				continue;
			}

			if (i == N - 1)
			{
				maxSwap[i] = 0;
				continue;
			}

			int res = 100000;
			int cur = 0;

			for (int j = i + 1; j < N; j++)
			{
				if (v[j] >= v[i])
					continue;

				double sx = double(x[i] * v[j] - x[j] * v[i]) / (v[j] - v[i]);

				res = min(res, cur + maxSwap[j]);

				if (sx < B - 1e-7)
				{
					cur++;
				}
			}
			maxSwap[i] = min(res, cur);
		}
		
		sort(all(maxSwap));

		int res = 0;
		if (K > N)
		{
			res = 100000;
		}
		else
		{
			for (int i = 0; i < K; i++)
				res += maxSwap[i];
		}
		

		if (res >= 100000)
			printf("Case #%d: IMPOSSIBLE\n", nTest);
		else
			printf("Case #%d: %d\n", nTest, res);
		fflush(stdout);
	}


	return 0;
}


