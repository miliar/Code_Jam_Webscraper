#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <iterator>
#include <iostream>
#include <sstream>
#include <cmath>
#include <cstdio>
using namespace std;
 
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;
 
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,a) for(int i=0;i<(a);i++)
#define FOREACH(i,x) for(__typeof((x).begin()) i=(x.begin()); i!=(x).end(); ++i)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define INF 1000000000

int dep[10000][2], ready[10000][2];

int main () {
	int n;
	scanf("%d",&n);
	REP(c,n) {
		memset(dep,0,sizeof(dep));
		memset(ready,0,sizeof(ready));
		int t, na, nb, ra = 0, rb = 0, ta = 0, tb = 0;
		scanf("%d %d %d",&t,&na,&nb);
		REP(i,na) {
			int dh, dm, ah, am;
			scanf("%d:%d",&dh,&dm);
			scanf("%d:%d",&ah,&am);
			dep[dh * 60 + dm][0]++;
			ready[ah * 60 + am + t][1]++;
		}
		REP(i,nb) {
			int dh, dm, ah, am;
			scanf("%d:%d",&dh,&dm);
			scanf("%d:%d",&ah,&am);
			dep[dh * 60 + dm][1]++;
			ready[ah * 60 + am + t][0]++;
		}
		REP(cur,2000) {
			ta += ready[cur][0];
			tb += ready[cur][1];
			if (ta < dep[cur][0]) {
				ra += dep[cur][0] - ta;
				ta = dep[cur][0];
			}
			if (tb < dep[cur][1]) {
				rb += dep[cur][1] - tb;
				tb = dep[cur][1];
			}
			ta -= dep[cur][0];
			tb -= dep[cur][1];
		}
		printf("Case #%d: %d %d\n", c + 1, ra, rb);
	}

	return 0;
}

