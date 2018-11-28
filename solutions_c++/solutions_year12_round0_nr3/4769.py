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
		int a, b;
		scanf("%d%d", &a, &b);
		int a0=a, d=1, dc=1;
		while(a0>9) a0/=10, d*=10, dc++;
		int res=0;
		for(int i=a;i<=b;i++)
		{
			int x=i;
			forn(j, dc)
			{
				x=x/10 + (x%10)*d;
				if(i<x && x>=a && x<=b) res++;
			}
		}
		printf("Case #%d: %d\n", _, res);
	}
	#ifdef home
		eprintf("%d ms\n", (int)(clock()*1000.0/CLOCKS_PER_SEC));
	#endif
	return 0;
}	



