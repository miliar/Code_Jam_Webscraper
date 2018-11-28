#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <climits>
#include <cstring>
#include <complex>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
typedef vector<int> vi;


#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define x first
#define y second
#define y1 y1_gdssdfjsdgf
#define y0 y0_fsdjfsdogfs
#define ws ws_fdfsdfsdgfs
#define image(a) {sort(all(a)),a.resize(unique(all(a))-a.begin());}
#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )
#define problem_name "a"
int T;
int n;
int nx[10000];
int was[10000];
int h[10000];
int main(){
	#ifdef home
	assert(freopen(problem_name".out","wt",stdout));
	assert(freopen(problem_name".in","rt",stdin));
	#endif
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		scanf("%d", &n);
		for (int i = 0; i < n - 1; i++) {
			scanf("%d", &nx[i]);
			nx[i]--;			
		}
		for (int i = 0; i < n; i++) {
			was[i] = 0;
		}
		nx[n - 1] = n;
		for (int i = 0; i < n - 1; i++) {	
			for (int j = i + 1; j < n - 1; j++) {
				if (nx[i] > j && nx[j] > nx[i]) {
					printf("Case #%d: Impossible\n", ti);
					goto aa;
				}
			}
		}
		was[n - 1] = 1;
		h[n - 1] = (int)1e9;		
	//	cerr<<"!"<<endl;
		for (int i = 0; i < n; i++) if (was[i] == 0){
			int tk = i;
			int en = -1;
			while (1) {
				if (was[tk] == 1) {
					en = tk;
					break;
				}
				tk = nx[tk];
			}
//			cerr<<i<<" "<<en<<endl;
			tk = i;
			while (1) {
				if (tk == en) break;
				h[tk] = h[en] - i * (en - tk);
				was[tk] = 1;
				tk = nx[tk];
			}	
		}
		printf("Case #%d:", ti);
		for (int i = 0; i < n; i++) {
			printf(" %d", h[i]);
		}
		printf("\n");
		aa:;	
	}
	return 0;
}
