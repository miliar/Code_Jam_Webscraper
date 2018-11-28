#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cassert>
#include <ctime>

#define next next_asdf
#define prev prev_asdf
#define y1 y1_asdf
#define ws ws_asdf

#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),(a).end()
#define forn(i, n) for(int (i)=0;(i)<(n);++(i))
#define ford(i, n) for(int (i)=1;(i)<=(n);++(i))
#define forit(it, v) for(typeof((v).begin()) (it)=(v).begin();(it)!=(v).end();++(it))

#ifdef home
	#define eprintf(...) {fprintf(stderr, __VA_ARGS__);fflush(stderr);}
#else
	#define eprintf(...) {}
#endif

#ifdef WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

using namespace std;

typedef long long ll;
typedef double ld;
typedef pair<int, int> pi;
typedef vector<int> vi;

const ld eps=1e-10;
const int inf=(int)1e9;

/* --- main part --- */

#define TASK_NAME "a"
const int maxn = 2010;
int x[maxn];
int res[maxn];
vi v[maxn];

void go(int x, int H, int a, int b)
{
	//eprintf("%d %d %d %d\n", x, H-(int)1e9, a, b);
	res[x] = H;
	for(int i=0;i<sz(v[x]);i++)
	{
		go(v[x][i], (int)1e9+a*v[x][i]-b, a+1, b+v[x][i]+1);
	}
}
int main()
{
	#ifdef home
		assert(freopen(TASK_NAME".in", "r", stdin));
		assert(freopen(TASK_NAME".out", "w", stdout));
	#endif
	int tn;
	scanf("%d", &tn);
	ford(_, tn)
	{
		int n;
		scanf("%d", &n);
		for(int i=0;i<n-1;i++) scanf("%d", &x[i]);
		for(int i=0;i<n-1;i++) x[i]--;
		bool imp = false;
		for(int i=0;i<n-1;i++) for(int j=i+1;j<n-1;j++) if(x[i]>j && x[j]>x[i]) imp = true;
		printf("Case #%d: ", _);
		if(imp){ printf("Impossible\n"); continue; }
		for(int i=0;i<n;i++) v[i].clear();
		for(int i=0;i<n-1;i++) v[x[i]].pb(i);
		for(int i=0;i<n;i++) res[i]=inf;
		go(n-1, (int)1e9, 0, 1);
		for(int i=0;i<n;i++) printf("%d%c", res[i], " \n"[i+1==n]);
		/*eprintf("%d\n", _);
		for(int i=0;i<n;i++) eprintf("%d%c", res[i]-(int)1e9+20, " \n"[i+1==n]);
		for(int i=0;i<n-1;i++) eprintf("%d%c", x[i]+1, " \n"[i+2==n]);*/
		for(int i=0;i<n-1;i++)
		{
			int best=i+1;
			for(int j=i+2;j<n;j++) if((res[j]-res[i])*(ll)(best-i) > (res[best]-res[i])*(ll)(j-i)) best=j;
			assert(best == x[i]);
		}		
	}
	#ifdef home
		eprintf("%d ms\n", (int)(clock()*1000.0/CLOCKS_PER_SEC));
	#endif
	return 0;
}	



