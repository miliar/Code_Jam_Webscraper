#include <algorithm>  
#include <iostream>  
#include <cstdio>  
#include <sstream>  
#include <ctype.h>  
#include <cstring>  
#include <string>  
#include <cmath>  
#include <queue>  
#include <vector>  
#include <map>  
#include <set>  

using namespace std;  

typedef long long i64;
typedef unsigned long long u64;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> ii;

#define pb push_back
#define sz(a) (int)(a).size()
#define all(a) (a).begin(),(a).end()
#define mset(a,byteval) memset(a, byteval, sizeof(a))
#define ff(i,b) for(i=0;i<(b);++i)
#define fr(i,a,b) for(i=(a);i<(b);++i)

const int inf = 1<<30;
const i64 inf64 = 1LL<<60;

int main() {

	freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);

	int Tests;
	scanf("%d", &Tests);

	for (int Test = 1; Test <= Tests; ++Test) {
		i64 L;
		int N;
		scanf("%I64d%d", &L, &N);

		vi v(N);
		for (int i = 0; i < N; ++i)
			scanf("%d", &v[i]);

		sort(all(v));

		vi dp(10000, inf64);

		dp[0] = 0;
		for (int i = 0; i < v.size(); ++i) {
			for (int j = v[i]; j < dp.size(); ++j) {
				dp[j] = min(dp[j], dp[j-v[i]] + 1);
			}
		}

		i64 res = inf64;
		for (int i = 0; i < v.size(); ++i) {
			i64 a = L / v[i];
			for (int j = 0; j < 10000; ++j) {
				i64 t = L % a;
				if (t + v[i] * j < dp.size()) 
					res = min(res, a - j + dp[t + v[i] * j]);
			}
		}

		if (res >= inf64) 
			printf ("Case #%d: IMPOSSIBLE\n", Test);
		else printf ("Case #%d: %I64d\n", Test, res);
	}

	return 0;
} 

