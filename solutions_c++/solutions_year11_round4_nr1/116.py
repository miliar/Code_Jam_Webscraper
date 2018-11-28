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
const int maxn = (int)1e4+123;
i64 S,R;
i64 w[maxn],l[maxn];
int p[maxn];

int cmpw(int a,int b){
	return w[a]*R+w[b]*S<w[b]*R+w[a]*S;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int tid = 1 ; tid <= T ; tid++ ){
		i64 X; scanf("%lld ",&X);
		scanf("%lld %lld ",&S,&R);
		double t; scanf("%lf ",&t);
		int n; scanf("%d ",&n);
		//eprintf("n = %d\n",n);
		i64 totallen = 0;
		forn(i,n){
			i64 B,E; scanf("%lld %lld %lld",&B,&E,&w[i]);
			l[i] = E - B;
			totallen+=l[i];
			p[i] = i;
		}
		l[n] = X - totallen;
		w[n] = 0;
		p[n]=n;
		n++;
		sort(p,p+n,cmpw);
	//	forn(i,n)eprintf("%lld%c",w[p[i]]," \n"[i+1==n]);
	//	forn(i,n)eprintf("%lld%c",l[p[i]]," \n"[i+1==n]);
		double res = 0.;
		forn(i,n){
			if(fabs(t)>1e-9){
				if((w[p[i]]+R)*t<l[p[i]]){
					res+=t;
					res += 1.*(l[p[i]]-(w[p[i]]+R)*t)/(w[p[i]]+S);
					t=0.;
				}else{
					res += 1.*l[p[i]]/(w[p[i]]+R);
					t-=1.*l[p[i]]/(w[p[i]]+R);
				}
			}else{
				res+=(l[p[i]]+0.)/(S+w[p[i]]+0.);
			}
		}
		printf("Case #%d: %.20lf\n",tid,res);
	}
	return 0;
}
