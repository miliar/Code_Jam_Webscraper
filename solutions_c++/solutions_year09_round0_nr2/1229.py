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

int n,m;
int a[100][100];
char ret[26];

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

VPII edg[100][100];

int sink[100][100];

int bass[100][100];

inline bool ok(int x,int y) {
	return 0<=x && x<n && 0<=y && y<m;
}

int main() {
	int ntc;
	scanf("%d\n",&ntc);
	FOR(tc,1,ntc) {
		scanf("%d%d",&n,&m);
		REP(i,n) REP(j,m) scanf("%d",&a[i][j]);
		REP(i,n) REP(j,m) edg[i][j].clear();
		REP(i,n) REP(j,m) sink[i][j]=0;
		printf("Case #%d:\n",tc);
		REP(i,n) REP(j,m) {
			int best=INF,cx,cy;
			REP(k,4) {
				int x=i+dx[k],y=j+dy[k];
				if(ok(x,y) && a[x][y]<best) {
					best=a[x][y];
					cx=x;
					cy=y;
				}
			}
			if(best<a[i][j]) edg[cx][cy].push_back(MP(i,j));
			else sink[i][j]=1;
			//printf("z %d %d splywa do %d %d\n",i,j,cx,cy);
		}
		int curs=0;
		REP(i,n) REP(j,m) if(sink[i][j]) {
			queue<PII> Q;
			Q.push(MP(i,j));
			while(!Q.empty()) {
				PII cur=Q.front();
				Q.pop();
				bass[cur.ST][cur.ND]=curs;
				REP(a,edg[cur.ST][cur.ND].size()) Q.push(edg[cur.ST][cur.ND][a]);
			}
			++curs;
		}
		REP(i,26) ret[i]='#';
		char cur='a';
		REP(i,n) REP(j,m) if(ret[bass[i][j]]=='#') ret[bass[i][j]]=cur++;
		REP(i,n) {
			REP(j,m) printf("%c ",ret[bass[i][j]]);
			printf("\n");
		}
	}
	return 0;
}
