// Headers {{{
#include <algorithm>
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
typedef pair<int,int> PII;
const int INF=1000000000;
// }}}

int n;
PII pkt[100000];
int ile[3][3];

int main() {
	int ntc;
	scanf("%d",&ntc);
	REP(tc,ntc) {		
		int A,B,C,D,x0,y0,M;
		scanf("%d%d%d%d%d%d%d%d",&n,&A,&B,&C,&D,&x0,&y0,&M);
		pkt[0].ST=x0,pkt[0].ND=y0;
		int X=x0,Y=y0;
		FOR(i,1,n-1) {
			X=int((LL(A)*LL(X)+LL(B))%LL(M));
			Y=int((LL(C)*LL(Y)+LL(D))%LL(M));
			pkt[i].ST=X,pkt[i].ND=Y;
		}
		REP(i,3) REP(j,3) ile[i][j]=0;
		REP(i,n) ++ile[pkt[i].ST%3][pkt[i].ND%3];
		LL res=0;
		REP(x1,3) REP(x2,3) REP(x3,3) REP(y1,3) REP(y2,3) REP(y3,3) {
			if((x1+x2+x3)%3==0 && (y1+y2+y3)%3==0) {
				res+=LL(ile[x1][y1])*LL(ile[x2][y2]-(x1==x2 && y1==y2))*LL(ile[x3][y3]-(x3==x2 && y3==y2)-(x3==x1 && y3==y1));
			}
		}
		printf("Case #%d: %lld\n",tc+1,res/6);
	}
	return 0;
}
