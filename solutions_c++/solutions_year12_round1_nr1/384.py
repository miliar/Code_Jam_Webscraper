#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long LL;
typedef long double LD;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define y1 y1_gedjcdgfce
#define y0 y0_sadasdasdsa
#define ws ws_sadsadsada
#define left left_asdsadsadsadsa
#define right right_asdasdsadasda
#define hash hash_asdasdasdsad

#ifdef DEBUG
#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}
#else
#define eprintf(...) {}
#endif

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif

#define TASK "task"

const int maxn = 1<<20;

double p[maxn];
double sp[maxn];


int main(){
	#ifdef DEBUG
	//assert(freopen(TASK".in","rt",stdin));
	//assert(freopen(TASK".out","wt",stdout));
	#endif
	int T;
	scanf("%d",&T);
	for( int test = 1 ; test <= T ; test++ ) {
		int A,B;
		scanf("%d%d",&A,&B);
		forn(i,A) scanf("%lf",&p[i]);
		sp[0] = 1.;
		forn(i,A) sp[i+1] = sp[i]*p[i]; 
		double res = 1 + B + 1;
		for( int corect = 0 ; corect <= A ; corect++ ) {
			res = min(A-corect + (1.-sp[corect])*(B+1) + B-corect+1,
					res);
		}
		printf("Case #%d: %.20e\n",test,res);
	}
	return 0;
}
