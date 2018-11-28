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
int T, n, D;
pi p[1000000];
const ld eps = 1e-9;
ld d[1000000];
int main(){
	#ifdef home
	assert(freopen(problem_name".out","wt",stdout));
	assert(freopen(problem_name".in","rt",stdin));
	#endif
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &p[i].x, &p[i].y);
		}
		pi g = p[0];
		sort(p, p + n);
		int st = -1;
		for (int i = 0; i < n; i++) {
			if (p[i] == g) {
				st = i;
			}
		}			
		scanf("%d", &D);
		for (int i = 0; i < n; i++) {
			d[i] = -1;
		}
//		cerr<<"!"<<endl;
		d[st] = p[st].x;		
		for (int i = 0; i < n; i++) if (d[i] >= -eps){			
//			cerr<<i<<" "<<d[i]<<" "<<p[i].x<<" "<<p[i].y<<endl;
			for (int j = i + 1; j < n; j++) {
				if (p[i].x + d[i] >= p[j].x - eps) {
					d[j] = max(d[j], min((ld)p[j].x - p[i].x, (ld)p[j].y));
				} 
			}
		}
		bool ans = false;
		for (int i = 0; i < n; i++) {
			if (p[i].x + d[i] >= D - eps) {
				ans = true;
			}
		}
		if (ans) {
			printf("Case #%d: YES\n", ti);
		} else {
			printf("Case #%d: NO\n", ti);
		}
	}
	return 0;
}
