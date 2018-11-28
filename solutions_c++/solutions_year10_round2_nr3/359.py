#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;
typedef long long ll;
typedef long double ld;

int N;

ll dp[510][510];
ll MOD = 100003;

unsigned long long nCr(unsigned long long n, unsigned long long r) {
	if (n == r)
		return 1;
	if( n == 0 )
		return 0;
	return nCr(n - 1, r) * n / (n - r);
}
ll getWays(int n, int ind) {
	if (ind == 1){
//		cerr << n << " " << ind <<" : " << 1 << endl;
		return 1;
	}
	if (dp[n][ind] != -1)
		return dp[n][ind];
	ll res = 0;
	for (int i = 1; i < ind; ++i) {
		res += ( getWays(ind,i)*(nCr(n-ind-1,ind-i-1)%MOD) )%MOD;
		res %= MOD;
	}
//	cerr << n << " " << ind <<" : " << res << endl;
	return dp[n][ind] = res;
}

#define SMALL
//#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif

	cin >> N;
	for (int ii = 1; ii <= N; ii++) {
		//cin>>c>>n;
		//for(int i = 0 ; i < n; i++)
		//	cin>>arr[i];
		memset(dp,-1,sizeof dp);
		ll res = 0;
		int n;
		cin >> n;
		for (int i = 1; i < n; ++i) {
			res += getWays(n,i);
			res %= MOD;
		}
		printf("Case #%d: ", ii);
		printf("%d",(int)res);
		printf("\n");
	}
	return 0;
}
