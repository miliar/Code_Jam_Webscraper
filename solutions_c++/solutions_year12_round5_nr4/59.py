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
int a[100][100];
vi f[100];
char s[10000];
int cnt = 0;
int cc;
int gg[100];
int was[100];
int was1[100];
vi ls;
void add1(int x, int y) {
	was1[x] = 1;
	was1[y] = 1;
	if (a[x][y] == 1) return;
	cc++;
	gg[y]++;
	gg[x]--;
	a[x][y] = 1;
}
void add(char x, char y) {
	for (int i = 0; i < sz(f[x - 'a']); i++)
		for (int j = 0; j < sz(f[y - 'a']); j++) {
			add1(f[x - 'a'][i], f[y - 'a'][j]);
		}
}
void dfs(int v) {
	was[v] = 1;
	for (int i = 0; i < cnt; i++) if (a[v][i] == 1 && was[i] == 0) {
		dfs(i);
	}
	ls.pb(v);
}
bool bl;
void dfs1(int v) {
//	cerr<<v<<endl;
	for (int i = 0; i < cnt; i++) if (a[v][i] == 1) {
		a[v][i] = 0;
		bl = true;
		dfs1(i);
		break;
	}
}

int main(){	
	freopen(problem_name".in","rt",stdin);
	freopen(problem_name".out","wt",stdout);
	for (int i = 0; i < 26; i++) {
		f[i].pb(cnt++);
	}
	f['o' - 'a'].pb(cnt++);
	f['i' - 'a'].pb(cnt++);
	f['e' - 'a'].pb(cnt++);
	f['a' - 'a'].pb(cnt++);
	f['s' - 'a'].pb(cnt++);
	f['t' - 'a'].pb(cnt++);
	f['b' - 'a'].pb(cnt++);
	f['g' - 'a'].pb(cnt++);	
	int T;
    scanf("%d", &T);
    for (int ti = 1; ti <= T; ti++) {
    	printf("Case #%d: ", ti);
    	int k;
		scanf("%d", &k);
		scanf("%s", s);
		int n = strlen(s);
		memset(a, 0, sizeof(a));
		memset(gg, 0, sizeof(gg));
		memset(was, 0, sizeof(was));
		memset(was1, 0, sizeof(was1));
		cc = 0;
		for (int i = 0; i < n - 1; i++) {
			add(s[i], s[i + 1]);
		}
		int f1 = 0;
		int f2 = 0;
		for (int i = 0; i < cnt; i++) {
			if (gg[i] > 0) {
				f1+=gg[i];
			} else {
				f2-=gg[i];
			}
		}
		/*ls.clear();
		for (int i = 0; i < cnt; i++) {
			if (was[i] == 0 && was1[i] == 1) {				
				dfs(i);
			//	tt++;
			}
		}	*/	
		if (f1 == 0) {
			cc++;
		}
		printf("%d\n", cc + max(f1, f2));
    }
	return 0;
}
