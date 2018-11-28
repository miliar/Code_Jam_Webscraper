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
const int maxn=1010;
pi a[maxn];
set<pi> s1;
set<pi> s2;
int use[maxn];
int res=0;
int cur=0;
int last=0;
int can=1;
int n;
bool imp=false;
inline void upd_s1()
{
	if(imp) return;
	while(last<n && a[last].fs<=cur)
	{
		if(use[last]==0) s1.insert(mp(-a[last].sc, last));
		last++;
	}
}
inline void use_1()
{
	int done=0;
	while(!done && !s1.empty())
	{
		int t=(*s1.begin()).sc;
		s1.erase(s1.begin());
		if(a[t].fs > cur) break;
		if(use[t]==0) done=1, use[t]=1, cur++, res++;
	}
	if(!done) imp=true;											
}
inline void use_all2()
{
	if(imp) return;
	while(!s2.empty() && (*s2.begin()).fs<=cur)
	{
		int t=(*s2.begin()).sc;
		s2.erase(s2.begin());
		if(use[t]<2) cur+=2-use[t], res++, use[t]=2;
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
		scanf("%d", &n);
		for(int i=0;i<n;i++) scanf("%d%d", &a[i].fs, &a[i].sc);
		sort(a, a+n);
		s2.clear();
		for(int i=0;i<n;i++) s2.insert(mp(a[i].sc, i));
		s1.clear();
		res=0, cur=0, last=0, imp=false;
		memset(use, 0, sizeof use);
		use_all2();
		while(!imp && cur!=2*n)
		{
			upd_s1();
			use_1();
			use_all2();
		}
		printf("Case #%d: ", _);
		if(cur!=2*n) printf("Too Bad\n");
		else printf("%d\n", res);
	}					  
	#ifdef home
		eprintf("%d ms\n", (int)(clock()*1000.0/CLOCKS_PER_SEC));
	#endif
	return 0;
}	



