#include <iostream>
#include <strstream>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <string>
#include <stack>
#include <cctype>
#include <cassert>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstring>
#include <functional>
#include <cstdlib>
#include <queue>
using namespace std;
#ifdef LOCAL
#define ll __int64
#define OUTLL "%I64d" 
#else
#define ll long long
#define OUTLL "%lld"
#endif
#define trav(it,cont) for(it=(cont).begin(); it!=(cont).end(); ++it)
#define forn(i,n) for(i=0;(i)<(n);++i)
#define MAX(a,b) ((a)<(b)?(b):(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define SWAP(a,b) a^=b;b^=a;a^=b
using namespace std;

const int N = 510;
int dp[N][256];
char strtmp[N];
int n;
char input()
{
	return 1;
}
char* pattern = "welcome to code jam";
int LEN = strlen(pattern);

int main()
{
#ifdef LOCAL
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int i, k, lv, ti, t;
	scanf("%d", &t);
	gets(strtmp);
	forn(ti,t){
		gets(strtmp);
		memset(dp,0,(sizeof dp));
		n = strlen(strtmp);

		int cur = 0;
		forn(i,n){
			if(strtmp[i] == pattern[0])cur++;
			dp[i][0] = cur;
		}

		for(k=1; k<LEN; k++){
			for(i=1; i< n; i++){
				dp[i][k] = dp[i-1][k];
				if(strtmp[i] == pattern[k] ){
					dp[i][k] += dp[i-1][k-1];
					dp[i][k] %= 10000;
				}
			}
		}

		printf("Case #%d: %04d\n", ti+1, dp[n-1][LEN-1]);
	}
	return 0;
}
