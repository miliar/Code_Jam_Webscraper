#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x,b,e) for (int x = (b); x < (e); ++x)
#define FORD(x,b,e) for (int x = (b) x >= (e); --x)
#define REP(x,n) for (int x = 0; x < (n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) c.begin(), c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for (VAR(i,c.begin()); i != c.end(); ++i)
#define PB push_back
#define ST first
#define ND second
const int MAXK = 5000;
const int MAXN = 100;
typedef list<int> li;
typedef li::iterator lit;
int res[MAXK];
int qr[MAXN];
int main()
{
	int T; scanf("%d",&T);
	REP(z,T) {
		int K; scanf("%d",&K);
		int n; scanf("%d",&n);
		REP(i,n) scanf("%d",&qr[i]);
		li l;
		REP(i,K) l.PB(i);
		lit it = l.begin();
		REP(i,K) {
		    int ed = i%SIZE(l);	
			//cout << "L "; FOREACH(dit,l) cout << *dit << ' '; cout << endl;
			REP(j,ed) { ++it; if (it == l.end()) it = l.begin(); }
			//cout << *it  << endl;
			res[*it] = i+1;
			lit nit = it;
			++it; if (it == l.end()) it = l.begin();
			l.erase(nit);
		}
		printf("Case #%d: ",z+1);
		REP(i,n) printf("%d ",res[qr[i]-1]);
		printf("\n");
	}
	return 0;
}
