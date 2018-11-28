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

#define TASK "task"
int main(){
	i64 pd,pg,n;
	int T;
	scanf("%d",&T);
	for(int test = 1 ; test <= T ; test++ ){
		scanf("%lld%lld%lld",&n,&pd,&pg);
		int ok = 0;
		for(i64 D = 1 ; D <= n && !ok ; D++ ){
			if((D*pd)%100LL) continue;
			i64 winD = (D*pd)/100LL;
			eprintf("D = %lld\n",D);
			for(i64 b = 0 ; !ok ; b++ ){
				i64 q = b*pg + pg*D - winD*100;
				if(q>=0&&(q%100LL==0LL)){
					i64 a = q/100LL;
					if(a<=b) ok = 1;
					if(pg==100) break; else ok = 1;
				}
				if(pg==0) break;
			}
		}
		printf("Case #%d: ",test);
		if(ok) printf("Possible\n"); else printf("Broken\n");
		eprintf("test %d ok.\n",test);
	}
	return 0;
}
