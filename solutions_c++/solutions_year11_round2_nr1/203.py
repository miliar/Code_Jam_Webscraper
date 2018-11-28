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
#define VD          VC< LD >

void print(VI v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
void print(VS v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
void print(VD v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS rv; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) rv.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) rv.PB(s.substr(p)); return rv;}

char d[100][100];
int w[100];
int g[100];
LD wp[100];
LD owp[100];
LD oowp[100];
int main() {
	int tc;
	cin >> tc;
	FOR(atc, 1, tc + 1) {
		int n;
		cin>>n;
		ZERO(g);
		ZERO(w);
		REP(i, n) {
			string s;
			cin >> s;
			REP(j, n) {
				d[i][j] = s[j];
				if (d[i][j] != '.') g[i]++;
				if (d[i][j] == '1') w[i]++;
			}
		}
		REP(i, n) {
			wp[i] = g[i] == 0 ? 0 : (double)w[i] / g[i];
		}
		
		REP(i, n) {
			owp[i] = 0;
			REP(j, n) if (i != j && d[i][j] != '.') {
				owp[i] += g[j] == 1 ? 0 : (double)(w[j] - (d[j][i] - '0')) / (g[j] - 1); 
			}
			if (g[i]) owp[i] /= g[i];
		}
		
		REP(i, n) {
			oowp[i] = 0;
			REP(j, n) if (i != j && d[i][j] != '.') {
				oowp[i] += owp[j];
			}
			if (g[i]) oowp[i] /= g[i];
		}
		
		printf("Case #%d:\n", atc);
		REP(i,n) printf("%.11Lf\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
	}
}