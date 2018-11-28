#include <string>
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
#define PB push_back
#define S second

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define RESET(a,c) memset(a,(c),sizeof(a))


typedef vector<int> VI;
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/


int match[1010];

int solve()
{
    int S, Q;
    scanf("%d\n", &S);
    char buff[2000];
    vector<string> vs, vq;
    
    REP(i, S) {
        gets(buff);
        vs.PB( string(buff));
    }
    scanf("%d\n", &Q);
    REP(i, Q) {
        gets(buff);
        vq.PB(string(buff));
    }
    
    if(Q == 0) return 0;
    
    RESET(match, -1);

    REP(i, Q) REP(j, S)  if(vq[i] == vs[j]) match[i] = j;
    

    
    int ret = INF;

    REP(xx, S) {
		int cur = xx, cnt = 0;
		
		REP(i, Q) if(match[i] == cur) {
				VI nx(S, INF);
				FORD(j, Q-1, i+1) if(match[j] != -1) nx[match[j]] = j;
				nx[match[i]] = -123;
				int mx = -1;
				REP(j, S) if(nx[j] > mx) mx = nx[j], cur = j;
				++cnt;
			}
        	
    	
		ret = min(ret, cnt);
	}
    return ret;
}

int main(void)
{
    int D,T = 1;
    scanf("%d\n", &D);
    while(D--) printf("Case #%d: %d\n", T++, solve());
	return (0);
}

