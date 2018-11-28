#include <algorithm>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <cstring>
#include <complex>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long i64;
typedef long double d64;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair

#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif
const int maxn = 1<<10;

d64 F[maxn];
d64 fact[maxn];
d64 dp[maxn];

d64 coef(int n,int k){
	if(k>=20)
		return 1./(exp(1.)*fact[n-k]);
	return F[k]/fact[n-k]/fact[k];
}

int main(){
	F[0] = 1.;
	F[1] = 0.;
	fact[0] = 1.;
	for(int i = 2 ; i < maxn ; i++ ) F[i] = (i-1)*(F[i-1]+F[i-2]);
	for(int i = 1 ; i < maxn ; i++ ) fact[i] = i*fact[i-1];
	dp[0] = 0.;
	dp[1] = 0.;
	for(int n = 2 ; n < maxn ; n++ ){
		d64 tmp = 1.;
		for(int k = 0 ; k < n ; k++ ) tmp+=coef(n,k)*dp[k];
		dp[n] = tmp/(1.-coef(n,n));
	}
	int T;
	scanf("%d",&T);
	for(int testID = 1 ; testID <= T ; testID++ ){
		int n;
		scanf("%d",&n);
		int q=0;
		for(int i = 1 ; i <= n ; i++ ){
			int a;
			scanf("%d",&a);
			if(a!=i) q++;
		}
		printf("Case #%d: %.20lf\n",testID,(double)dp[q]);
	}
	return 0;
}
