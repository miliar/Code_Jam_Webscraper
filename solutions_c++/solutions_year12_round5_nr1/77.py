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
pair<pi, int> p[10000];
int n;
bool cmp(pair<pi, int> a, pair<pi, int> b) {
	return (a.x.x * 100 + a.x.y * b.x.x < b.x.x * 100 + b.x.y * a.x.x) || 
		   ((a.x.x * 100 + a.x.y * b.x.x == b.x.x * 100 + b.x.y * a.x.x) && (a.y < b.y));
}
int main(){	
	freopen(problem_name".in","rt",stdin);
	freopen(problem_name".out","wt",stdout);
	int T;
    scanf("%d", &T);
    for (int ti = 1; ti <= T; ti++) {
    	printf("Case #%d:", ti);
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &p[i].x.x);
			p[i].y = i;
		}
		for (int i = 0; i < n; i++) {
			scanf("%d", &p[i].x.y);
			p[i].x.y = 100 - p[i].x.y;
			p[i].y = i;
		}
		sort(p, p + n, cmp);
		for (int i = 0; i < n; i++) {
			printf(" %d", p[i].y);
		}
		printf("\n");
    }
	return 0;
}
