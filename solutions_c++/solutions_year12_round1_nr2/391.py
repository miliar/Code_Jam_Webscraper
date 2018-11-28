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

const int maxn = 2000;

int star[maxn];
int a[maxn],b[maxn];

int main(){
	#ifdef DEBUG
	assert(freopen(TASK".in","rt",stdin));
	assert(freopen(TASK".a","wt",stdout));
	#endif
	int T; scanf("%d",&T);
	for( int test = 1; test <= T ; test++ ) {
		int n; scanf("%d",&n);
		eprintf("n = %d\n",n);
		forn(i,n) scanf("%d%d",&a[i],&b[i]);
		memset(star,0,sizeof star);
		int ss = 0;
		int act = 0;
		while(1) {
			int found2 = 0;
			do{
				found2 = 0;
				for( int i = 0 ; i < n ; i++ ) {
					if( star[i] < 2 && b[i] <= ss ) {
						found2 = 1;
						ss += 2-star[i];
						star[i] = 2;
						act++;
					}
				}
			}while(found2);
			int maxi = -1;
			for( int i = 0 ; i < n ; i++ ) {
				if( star[i] < 1 && a[i] <= ss ) {
					if( maxi == -1 || b[maxi] < b[i] ) maxi = i; 
				}
			}
			if( maxi == -1 ) break;
			star[maxi] = 1;
			ss++;
			act++;
		}
		printf("Case #%d: ",test);
		if( ss != 2*n ) {
			printf("Too Bad\n");
		}else{
			printf("%d\n",act);
		}
	}
	return 0;
}
