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
const int maxn = 10010;
int d[maxn], l[maxn];
const int N = 1<<16;
int res[2*N];
int fl[2*N];
int flX[2*N];

inline void put(int ind, int X)
{
	 res[ind] = min(res[ind], X);
	 flX[ind] = min(flX[ind], X);
	 fl[ind] = 1;
} 
inline void relax(int ind)
{
	if(fl[ind])
	{
		put(2*ind, flX[ind]);
		put(2*ind+1, flX[ind]);
		fl[ind] = 0;
		flX[ind] = inf;
	}
}
void upd(int ind, int X, int l, int r, int lq, int rq)
{
	if(l>=rq) return ;
	if(r<=lq) return ;
	if(lq<=l && r<=rq)
	{
		put(ind, X);
		return;
	}
	int m = (l+r) >> 1;
	relax(ind);
	upd(2*ind, X, l, m, lq, rq);
	upd(2*ind+1, X, m, r, lq, rq);
	res[ind] = min(res[2*ind], res[2*ind+1]);
}
int get(int ind, int l, int r, int lq, int rq)
{
	if(l>=rq) return inf;
	if(r<=lq) return inf;
	if(lq<=l && r<=rq) return res[ind];
	int m = (l+r) >> 1;
	relax(ind);
	return min(get(2*ind, l, m, lq, rq), get(2*ind+1, m, r, lq, rq));
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
		for(int i=0;i<2*N;i++) res[i] = inf, fl[i] = 0, flX[i] = inf;
		int n;
		scanf("%d", &n);
		for(int i=0;i<n;i++) scanf("%d%d", &d[i], &l[i]);
		int D;
		scanf("%d", &D);
		for(int i=0;i<n;i++) upd(1, d[i], 0, N, i, i+1);
		upd(1, 0, 0, N, 0, 1);
		int rmax = d[0];
		for(int i=0;i<n;i++)
		{
			int g = get(1, 0, N, i, i+1);
			if(g == d[i]) break;
			int L = min(d[i]-g, l[i]);
			int ind2 = upper_bound(d, d+n, d[i]+L) - d;
			upd(1, d[i], 0, N, i, ind2);
			rmax = max(rmax, d[i]+L);
		}
		printf("Case #%d: ", _);
		if(rmax >= D) printf("YES\n");
		else printf("NO\n");
//		break;
	}
	 
	#ifdef home
		eprintf("%d ms\n", (int)(clock()*1000.0/CLOCKS_PER_SEC));
	#endif
	return 0;
}	



