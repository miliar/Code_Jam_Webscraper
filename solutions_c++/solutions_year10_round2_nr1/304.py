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
		int n, m, wynik=0;
		set<string> istenieja;
		scanf("%d%d",&n, &m);
		char t[300];
		REP(i, n) {
			scanf("%s",t);
			string a = t;
			istenieja.insert(a);
		}
		REP(i, m) {
			scanf("%s",t);
			string a = t;
		
			string dot="";
			vector<string> v;
			REP(j, a.size()) {
				if (a[j]=='/' && j>0) v.push_back(dot);
				dot+=a[j];
			}
			v.push_back(dot);
			REP(i, v.size()) {
				if (istenieja.find(v[i])==istenieja.end()) {
					wynik+=(v.size()-i);
					REP(j, v.size()) istenieja.insert(v[j]);
					break;
				}
			}
		}
		printf("Case #%d: %d\n",iile, wynik);
	}
	return 0;
}

