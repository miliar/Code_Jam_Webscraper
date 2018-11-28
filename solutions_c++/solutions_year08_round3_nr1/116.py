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


int main()
{
	int k, T, i;
	freopen("A-large.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
	scanf("%d", &T);
	for(k = 1 ; k <= T ; ++k)
	{
		ll res = 0, t;
		ll P, K, L;
		scanf("%lld %lld %lld", &P, &K, &L);
		vector< ll > freq;
		for(i = 0 ; i < L ; ++i)
		{
			scanf("%lld", &t);
			freq.pb(t);
		}
        sort( rall(freq) );
		int c = 0, times = 1;
		bool flag = true;
		while(flag){
		for(i = 0 ; i < K && flag ; ++i)
		{
            res += (times * freq[c]);
			c++;
			if(c >= sz(freq))flag = false;
		}
		times++;
		}
		printf("Case #%d: %lld\n", k, res);
	}
	return 0;
}
