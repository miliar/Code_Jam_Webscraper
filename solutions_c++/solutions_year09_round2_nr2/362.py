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
		LL w;
		vector<pair<LL,LL> >  v;
		string st;
		cin >> st;
		int i=0;
		REP(i,st.size()) {
			v.push_back(make_pair(int(st[i]-'0'),-i));
		}
		/*
		while (w>0) {
			i++;
			v.push_back(make_pair(w%10,i));
			w/=10;
		}
		*/
//		reverse(v.begin(),v.end());
		if (!next_permutation(v.begin(),v.end())) {
			sort(v.begin(),v.end());
			bool done=false;
			REP(i,v.size()) if (v[i].first!=0 && !done) {
				done=true;
				swap(v[0],v[i]);
			}
			v.insert(v.begin()+1,make_pair(0,0));
		}
		cout << "Case #"<<iile<<": ";
		REP(i,v.size()) cout << v[i].first; cout << endl;
	
	}
	return 0;
}

