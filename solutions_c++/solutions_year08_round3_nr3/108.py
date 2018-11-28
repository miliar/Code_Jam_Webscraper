#define _CRT_SECURE_NO_DEPRECATE
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <set>
#include <cmath>
#include <queue>
#include <sstream>
#include <iostream>
using namespace std;
#define inf      2147483647
#define inf64    9223372036854775807
#define eps      1e-10
#define pi      3.14159265358
#define sqr(a) (a)*(a)
#define rall(a) a.rbegin(),a.rend()
#define all(a) a.begin(),a.end()
#define sz(a) (a).size()
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back 
#define updateMIN(a, x) if(a > x)a = x 
#define updateMAX(a, x) if(a < x)a = x 
typedef long long ll;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;
#define MOD 1000000007

int main()
{
	int k, T, i;
	freopen("C-small-attempt1.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
	scanf("%d", &T);
	for(k = 1 ; k <= T ; ++k)
	{
		ll n, m, X, Y, Z, A[1001];
		ll nums[1001] = {0};
		scanf("%lld %lld %lld %lld %lld",&n, &m, &X, &Y, &Z);
		for(i = 0 ; i < m ; ++i)scanf("%lld", &A[i]);
        for(i = 0 ; i < n ; ++i)
		{
			nums[i] = A[i % m];
			A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
		}
		ll res = 0;
        int j, q;
		ll F[1001] = {0}, OldF[1001] = {0};
		for(i = 0 ; i < n ; ++i)OldF[i] = 1;
		res = n;
		for(i = 2 ; i <= n ; ++i)
		{
			ll tres = 0;
			for(j = n - 1 ; j >= 0 ; --j)
			{
				F[j] = 0;
				for(q = j + 1 ; q < n ; ++q)
				{
					if(nums[q] > nums[j])
					{
						F[j] += (OldF[q] % MOD);
					}
				}
				tres += (F[j] % MOD);
			}
			tres %= MOD;
			res += tres;
			memcpy(OldF, F, sizeof(F));
		}
		res %= MOD;
		printf("Case #%d: %lld\n", k, res);
	}
	return 0;
}
