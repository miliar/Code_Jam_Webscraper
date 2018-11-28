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

int a[1<<10];

int main(){
	int T;
	scanf("%d",&T);
	for(int test = 1 ; test <= T ; test++ ){
		int n;
		scanf("%d",&n);
		forn(i,n) scanf("%d",&a[i]);
		int q = 0;
		forn(i,n) q^=a[i];
		if(!q){
			sort(a,a+n);
			reverse(a,a+n);
			int res = 0;
			forn(i,n-1) res+=a[i];
			printf("Case #%d: %d\n",test,res);
		}else{
			printf("Case #%d: NO\n",test);
		}
	}
	return 0;
}
