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

int seq[5005];
VI wolne;

void gen(int k) {
	wolne.clear();
	REP(i,k) wolne.push_back(i);
	int poz=0;
	FOR(i,1,k) {
		int pozy=(poz+(i-1))%size(wolne);
		seq[wolne[pozy]]=i;
		wolne.erase(wolne.begin()+pozy);
		if(i<k) poz=pozy%size(wolne);
	}
}

int main() {
	int ntc;
	scanf("%d",&ntc);
	REP(tc,ntc) {
		int k;
		scanf("%d",&k);
		memset(seq,0,sizeof(seq));
		gen(k);
		int n;
		scanf("%d",&n);
		printf("Case #%d: ",tc+1);
		REP(i,n) {
			int x;
			scanf("%d",&x);
			printf("%d ",seq[x-1]);
		}
		printf("\n");
	}
	return 0;
}
