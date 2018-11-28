// Headers {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,j,k) for(int i=(j); i<=(k); ++i)
#define FORD(i,j,k) for(int i=(j); i>=(k); --i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ST first
#define ND second
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SQR(a) ((a)*(a))
#define debug(x) cerr << #x << " = " << x << '\n'
template<typename Q> inline int size(Q a) { return a.size(); }
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<pair<int,int> > VPII;
typedef unsigned long long ULL;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
const int INF=1000000000;
// }}}

int n;
char board[40][41];
int nr[40];

int main() {
        int ntc;
        scanf("%d",&ntc);
        FOR(tc,1,ntc) {
                scanf("%d",&n);
                REP(i,n) scanf("%s",board[i]);
                REP(i,n) {
                        nr[i]=-1;
                        REP(j,n) if(board[i][j]=='1') nr[i]=j;
                }
                int res=0;
                REP(i,n) if(nr[i]>i) {
                        FOR(j,i+1,n-1) if(nr[j]<=i) {
                                while(j!=i) {
                                        swap(nr[j],nr[j-1]);
                                        --j;
                                        ++res;
                                }
                                break;
                        }
                }
                printf("Case #%d: %d\n",tc,res);
        }
	return 0;
}
