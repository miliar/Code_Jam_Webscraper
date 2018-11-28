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

const int maxn = 1<<10;

long long r[maxn];
long long xx[maxn],yy[maxn];

int check(int ind, long long x,long long y) {
    forn(j,ind) {
        if ( (x - xx[j])*(x-xx[j]) + (y-yy[j])*(y-yy[j]) < 
        (r[ind]+r[j])*(r[ind]+r[j])) return 0;
    }
    return 1;
}

int main(){
    int T;
    assert(scanf("%d",&T)==1);
    srand(time(NULL));
    for( int test = 1 ; test <= T ; test++ ) {
        int n; 
        assert(scanf("%d",&n)==1);
        long long W,L;
        assert(scanf("%lld%lld",&W,&L)==2);
        forn(i,n) assert(scanf("%lld",&r[i])==1);
        st:
        for( int i = 0 ; i < n ; i++ ) {
            int cnt = 0;
            while(1) {
                cnt++;
                long long x = rand()%(W+1);
                long long y = rand()%(L+1);
                if(check(i,x,y)){
                    xx[i] = x;
                    yy[i] = y;
                    break;
                }
                if( cnt >= 100 ) goto st;
            }
        }
        printf("Case #%d: ",test);
        forn(i,n) {
            assert(xx[i]>=0&&yy[i]>=0);
            assert(xx[i]<=W&&yy[i]<=L);
            printf("%lld %lld%c",xx[i],yy[i]," \n"[i+1==n]);
        }
    }
	return 0;
}
