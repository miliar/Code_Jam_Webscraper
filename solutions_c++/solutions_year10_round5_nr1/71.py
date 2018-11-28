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

ll x[20];
int D, K;

ll mod(ll a, ll MOD)
{
	return (a % MOD + MOD) % MOD;
}

bool check(ll A, ll P)
{
	int B = mod(x[1] - A * x[0], P);

	for (int j = 0; j < K - 1; j++)
	{
		int n = mod(A * x[j] + B, P);
		if (n != x[j + 1])
			return false;

	}
	return true;
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

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);

	vector<int> IsPrime(1000000, true);
	IsPrime[0] = IsPrime[1] = false;
	for (int i = 2; i * i < IsPrime.size(); i++)
	{
		if (IsPrime[i]) for (int j = i * i; j < IsPrime.size(); j += i) IsPrime[j] = false;
	}

	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		
		scanf("%d %d", &D, &K);

		for (int i = 0; i< K; i++)
		{
			scanf("%lld", &x[i]);
		}

		if (K < 2)
		{
			printf("Case #%d: I don't know.\n", nTest);
			continue;
		}

		if (K == 2)
		{
			if (x[0] != x[1])
				printf("Case #%d: I don't know.\n", nTest);
			else
				printf("Case #%d: %lld\n", nTest, x[0]);

			continue;
		}
		 

		int maxA = 1;
		rep(i, D) maxA *= 10;

		vector<pair<int, int> > sol;

		int ans = -1;

		int minP = *max_element(x, x + K)+ 1;

		if (x[1] == x[0])
		{
			bool same = true;
			for (int i = 1; i < K; i++)
			{
				if (x[i] != x[0])
				{
					same = false;
				}
			}

			if (!same)
				printf("Case #%d: I don't know.\n", nTest);
			else
				printf("Case #%d: %lld\n", nTest, x[0]);
			continue;
		}

		
		for (int P = minP; P < maxA; P++)
		{				
			if (!IsPrime[P])
				continue;		
			
			ll xx = mod(x[2 - 1] - x[2 - 2], P);
			ll yy = mod(x[2] - x[2 - 1], P);

			 

			ll A = mod(yy * powmod(xx, P - 2, P), P);

			{			

				bool ok = true;

				for (int j = 2; j < K; j++)
				{
					ll xx = mod(x[j - 1] - x[j - 2], P);
					ll yy = mod(x[j] - x[j - 1], P);

					if (mod(A * xx, P) != yy)
					{
						ok = false;
						break;
					}
				}
				if (ok) 
				{
					if (check(A, P))
					{
						int B = mod(x[1] - A * x[0], P);

						int next = mod(A * x[K - 1] + B, P);
						if (ans == -1 )
						{
							ans = next;
						}
						else if (ans != next)
						{
							ans = -1;
							goto printIt;
						}
					}
				}
			}
		}

printIt:
		

		if (ans == -1)
		{
			printf("Case #%d: I don't know.\n", nTest);
		}
		else
		{
			printf("Case #%d: %d\n", nTest, ans);


		}
		fflush(stdout);
	} 


	return 0;
}


