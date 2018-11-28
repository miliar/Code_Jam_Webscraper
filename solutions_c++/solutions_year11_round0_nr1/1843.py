#include <string>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define SIZE(x) (int)((x).size())

#define ALL(v) (v).begin(), (v).end()
#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define PV(v) ({ cout << #v << " = "; for(int __i = 0; __i < (int)(v).size();++__i ) cout << (v)[__i] << " "; putchar('\n'); putchar('\n'); })


typedef pair<int,int> PII;
typedef vector<int> VI;
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

#define IN(x, r1, r2) ( (x) >= (r1) && (x) <= (r2))


int sgn(int x) {
	if(x > 0) return 1;
	if(x < 0) return -1;
	return 0;
}
void solve()
{
	int N;
	VI cel[2];
	vector<PII> cur;
	scanf ("%d ", &N);
	REP(i, N) {
		char s[100], c;  int x;
		assert(scanf("%s %d", s, &x) == 2);
		c = s[0];
		assert(c == 'O' || c == 'B');
		cel[(c == 'O')].PB(x);
		cur.PB( MP( (c == 'O'), x));
	}
	REP(x, 2) reverse(ALL(cel[x]));
	reverse(ALL(cur));
	int poz[2]; 
	poz[0] = poz[1] = 1;
	int ret = 0;
	
	while(SIZE(cur)) {
		bool fst_rem = true;
		REP(x, 2) if(SIZE(cel[x])) {
			if(poz[x] == cel[x].back() && cur.back().F == x && fst_rem) {
				assert(cur.back().S == cel[x].back());
				cel[x].pop_back();
				cur.pop_back();
				fst_rem = false;
			}
			else poz[x] += sgn(cel[x].back() - poz[x]);
		}
		++ret;
	}
	printf("%d\n", ret);
}

int main(void)
{
	int T = RI();
	FOR(i,1,T) {
		printf("Case #%d: ", i);
        solve();
	}
	return (0);
}
