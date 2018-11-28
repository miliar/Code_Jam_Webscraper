#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>

using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define ZERO(m)     memset(m,0,sizeof(m))
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define LL          long long
#define LD          long double
#define MP          make_pair
#define X           first
#define Y           second
#define VC          vector
#define PII			pair <int, int>
#define VI          VC<int>
#define VPII		VC < PII >
#define VS          VC<string>
#define DB(a)		cout << #a << ": " << a << endl;

void print(VI v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
void print(VS v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS rv; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) rv.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) rv.PB(s.substr(p)); return rv;}

int main() {
	int tc;
	cin >> tc;
	FOR(atc, 1, tc + 1) {
		int c; cin >> c;
		VS vc;
		REP(i, c) {string s; cin >> s; vc.PB(s);}
		int d; cin >> d;
		VS vd;
		REP(i, d) {string s; cin >> s; vd.PB(s);}
		
		int n; cin >> n;
		string s; cin >> s;
		string r = "";
		
		
		REP(i, s.S) {
			r += s[i];
			if (r.S >= 2) {
				REP(j, vc.S) if (r[r.S - 2] == vc[j][0] && r[r.S - 1] == vc[j][1] || r[r.S - 1] == vc[j][0] && r[r.S - 2] == vc[j][1]) {
					r = r.substr(0, r.S - 2) + vc[j][2];
					break;
				}
			}
			REP(j, vd.S) if (r[r.S - 1] == vd[j][0] || r[r.S - 1] == vd[j][1]) {
				char c = (r[r.S - 1] == vd[j][0]) ? vd[j][1] : vd[j][0];
				REP(k, r.S) if (r[k] == c) {
					r = "";
					goto out;
				}
			}
			out: ;
		}
		
		printf("Case #%d: [", atc);
		REP(i, r.S) {
			if (i) cout << ", ";
			cout << r[i];
		}
		cout << "]" << endl;
	}
}