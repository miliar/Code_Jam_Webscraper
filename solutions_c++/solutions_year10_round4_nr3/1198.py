#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <ext/hash_map>

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define INF 1000000000
#define EPS 0.0000000001
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef pair<int, int> PII;
typedef long long i64; 
typedef map<PII,bool>::iterator it1;
typedef map<PII,PII>::iterator it2;

int main() {
	freopen("C-small.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);
	int T;
	cin >> T;
	REP(t,T){
		int r; cin >> r;
		map<PII,bool> m,m2;
		int res = 0;
		REP(i,r){
			int x1,x2,y1,y2; cin >> x1 >> y1 >> x2 >> y2;
			FOR(x,x1,x2+1) FOR(y,y1,y2+1) {
				PII p = make_pair(x,y);
				m[p]=true;
			}
		}
		do {
			++res;
			map<PII,PII> d;
			for (it1 i=m.begin();i!=m.end();++i) {
				PII p = i->X;
				d[make_pair(p.X+1,p.Y)].X=1;
				d[make_pair(p.X,p.Y+1)].Y=1;
			}
			for (it1 i=m.begin();i!=m.end();++i) {
				PII p = i->X;
				PII n = d[p];
				if (n.X==1 || n.Y==1) m2[p]=true;
			}
			for (it2 i=d.begin();i!=d.end();++i) {
				PII p = i->Y;
				if (p.X!=1 || p.Y!=1) continue;
				p = i->X;
				m2[p]=true;
			}
			m = m2;
			m2.clear();
		} while (m.sz!=0);
		cout << "Case #" << (t+1) << ": " << res << endl;
	}
}
