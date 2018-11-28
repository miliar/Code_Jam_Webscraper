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

int l,d,n;

char words[5000][16];

char patt[1000];
bool possible[15][50];

int main() {
	scanf("%d%d%d\n",&l,&d,&n);
	REP(i,d) gets(words[i]);
	REP(tc,n) {
		printf("Case #%d: ",tc+1);
		gets(patt);
		memset(possible,0,sizeof(possible));
		int nxt=0;
		for(int i=0;patt[i];++i) {
			if(isalpha(patt[i])) {
				possible[nxt++][patt[i]-'a']=1;
			} else {
				++i;
				while(isalpha(patt[i])) {
					possible[nxt][patt[i]-'a']=1;
					++i;
				}
				++nxt;
			}
		}
		int res=0;
		REP(i,d) {
			bool ok=true;
			REP(j,l) if(!possible[j][words[i][j]-'a']) { ok=false; break; }
			res += ok;
		}
		printf("%d\n",res);
	}
	return 0;
}
