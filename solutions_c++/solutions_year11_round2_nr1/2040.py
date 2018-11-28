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

const int MAXN=105;

int n;
char brd[MAXN][MAXN];

double WP[MAXN],OWP[MAXN],OOWP[MAXN];

int main() {
	int ntc;
	scanf("%d",&ntc);
	FOR(tc,1,ntc) {
		printf("Case #%d:\n",tc);
		scanf("%d",&n);
		REP(i,n) {
			scanf("%s",brd[i]);
			WP[i]=OWP[i]=OOWP[i]=0.0;
		}
		REP(i,n) {
			int games=0,won=0;
			REP(j,n) {
				won+=(brd[i][j]=='1');
				games+=(brd[i][j]!='.');
			}
			WP[i]=(double)won/games;
		}
//		REP(i,n) printf("%.8lf\n",WP[i]);
		REP(cur,n) {
			int cnt=0;
			REP(i,n) if(brd[cur][i]!='.') {
				++cnt;
				int games=0,won=0;
				REP(j,n) if(j!=cur) {
					won+=(brd[i][j]=='1');
					games+=(brd[i][j]!='.');
				}
				OWP[cur]+=(double)won/games;
			}
			OWP[cur]/=cnt;
		}
//		REP(i,n) printf("%.8lf\n",OWP[i]);
		REP(cur,n) {
			int cnt=0;
			REP(i,n) if(brd[cur][i]!='.') {
				++cnt;
				OOWP[cur]+=OWP[i];
			}
			OOWP[cur]/=cnt;
		}
//		REP(i,n) printf("%.8lf\n",OOWP[i]);
		REP(i,n) printf("%.8lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
	}
	return 0;
}
