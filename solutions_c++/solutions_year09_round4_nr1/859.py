// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 

int main() {
	int ile;
	scanf("%d",&ile);
	FOR(iile,1,ile) {
		int n;
		VI v,q;
		char x;
		scanf("%d",&n); scanf("%c",&x);
		REP(i,n) {
			int pop=0;
			REP(j,n) {
				scanf("%c",&x);
				if (x=='1') pop=j+1;
			}
			scanf("%c",&x);
			v.push_back(pop);
		}

		REP(i,n) q.push_back(i+1);

	

		int mam;
		int swaps=0;
		REP(i,v.size()) {
			if (v[i]>q[i]) {
				mam=-1;
				FOR(j,i+1,v.size()-1) if (v[j]<=q[i] && mam==-1) mam=j;
				FORD(j,mam,i+1) {
					swap(v[j-1],v[j]);
					swaps++;
				}
			}
		}

		printf("Case #%d: %d\n",iile,swaps);
	}
	return 0;
}

