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
int T, n, w, l;
pi aa[10000];
pi p[10000];
vector<pair<pi, int> > split(vector<pair<pi, int> > a, int j, int x) {
	vector<pair<pi, int> > b;
	for (int i = 0; i < j; i++) {
		b.pb(a[i]);
	}
	b.pb(mp(mp(a[j].x.x, a[j].x.y - x),a[j].y));
	b.pb(mp(mp(a[j].x.y - x, a[j].x.y),a[j].y));
	for (int i = j + 1; i < sz(a); i++) {
		b.pb(a[i]);
	}
	return b;
}
int main(){
	#ifdef home
	assert(freopen(problem_name".out","wt",stdout));
	assert(freopen(problem_name".in","rt",stdin));
	#endif
	scanf("%d", &T);
	for (int ti = 0; ti < T; ti++) {
		scanf("%d %d %d", &n, &w, &l);
		for (int i = 0; i < n; i++) {
			scanf("%d", &p[i].x);
			p[i].y = i;
		}
	//	swap(w, l);

		sort(p, p + n);
		reverse(p, p + n);
		bool ans = true;
		vector<pair<pi, int> > ls;
		ls.pb(mp(mp(0, w), 0));
		for (int i = 0; i < n; i++) {
//			cerr<<i<<endl;			
			ans = false;			
			int tk = 0;
			int pr = 0;
			int mx = 0;
			for (int j = 0; j < sz(ls); j++) {				
				tk += ls[j].x.y - ls[j].x.x;
				mx = max(mx, ls[j].y);
				if (mx == 0 || mx + p[i].x <= l) {					
					if (tk >= 2 * p[i].x) {
						if (tk > 2 * p[i].x) {
							ls = split(ls, j, tk - 2 * p[i].x);
						}
						if (mx == 0) {
							aa[p[i].y].y = 0;
							aa[p[i].y].x = ls[pr].x.x + p[i].x;
							mx = p[i].x;
						} else {
							mx += p[i].x;
							aa[p[i].y].y = mx;
							aa[p[i].y].x = ls[pr].x.x + p[i].x;
							mx += p[i].x;
						}
						for (int k = pr; k <= j; k++) {
							ls[k].y = mx;
						}
						ans = true;
						break;
					}
					if (tk >= p[i].x && pr == 0) {
						if (tk > p[i].x) {
							ls = split(ls, j, tk - p[i].x);
						}
						if (mx == 0) {
							aa[p[i].y].y = 0;
							aa[p[i].y].x = ls[pr].x.x;
							mx = p[i].x;
						} else {
							mx += p[i].x;
							aa[p[i].y].y = mx;
							aa[p[i].y].x = ls[pr].x.x;
							mx += p[i].x;
						}
						for (int k = pr; k <= j; k++) {
							ls[k].y = mx;
						}
						ans = true;
						break;
					}
					if (tk >= p[i].x && j == sz(ls) - 1) {						
						if (mx == 0) {
							aa[p[i].y].y = 0;
							aa[p[i].y].x = ls[j].x.y;
							mx = p[i].x;
						} else {
							mx += p[i].x;
							aa[p[i].y].y = mx;
							aa[p[i].y].x = ls[j].x.y;
							mx += p[i].x;
						}
						for (int k = pr; k <= j; k++) {
							ls[k].y = mx;
						}
						ans = true;
						break;
					}
					if (pr == 0 && j == sz(ls) - 1 && 2 * p[i].x >= w) {						
						if (mx == 0) {
							aa[p[i].y].y = 0;
							aa[p[i].y].x = ls[j].x.y;
							mx = p[i].x;
						} else {
							mx += p[i].x;
							aa[p[i].y].y = mx;
							aa[p[i].y].x = ls[j].x.y;
							mx += p[i].x;
						}
						for (int k = pr; k <= j; k++) {
							ls[k].y = mx;
						}
						ans = true;
						break;
					}		
				} else {
					pr = j + 1;
					tk = 0;   
					mx = 0;
				}
			}
			assert(ans);
		}
	//	cerr<<"!"<<endl;
	//	cerr<<w<<" "<<l<<endl;
		for (int i = 0; i < n; i++) {
	//		cerr<<aa[i].x<<" "<<aa[i].y<<endl;
			assert(aa[i].x >= 0 && aa[i].x <= w);
			assert(aa[i].y >= 0 && aa[i].y <= l);
		}
		printf("Case #%d:", ti + 1);
		for (int i = 0; i < n; i++) {
			printf(" %d %d", aa[i].x, aa[i].y);
		}
		printf("\n");
	}
	return 0;
}
