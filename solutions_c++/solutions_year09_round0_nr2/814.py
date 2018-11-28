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
#define FORE(i,a)   for(__typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define ZERO(m)     memset(m,0,sizeof(m))
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define LL          long long
#define LD          long double
#define MP          make_pair
#define PII         pair<int, int>
#define X           first
#define Y           second
#define VC          vector
#define VI          VC<int>
#define VVI         VC< VI >
#define VS          VC<string>
#define VPII        VC< PII >
#define DB(a)       cerr << #a << ": " << a << endl;

void print(VI v) {cout << "[";if (v.S) cout << v[0];FOR(i, 1, v.S) cout << ", " << v[i];cout << "]\n";}
void print(VS v) {cout << "[";if (v.S) cout << v[0];FOR(i, 1, v.S) cout << ", " << v[i];cout << "]\n";}
void print(VVI v) {cout << "[ ---";if (v.S) cout << " ", print(v[0]);FOR(i, 1, v.S) cout << " ", print(v[i]);	cout << "--- ]\n";}
void print(PII p) {cout << "{" << p.X << ", " << p.Y << "}";}
void print(VPII v) {cout << "[";if (v.S) print(v[0]);FOR(i, 1, v.S)  cout << ", ", print(v[i]);cout << "]\n";}

template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS rv; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) rv.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) rv.PB(s.substr(p)); return rv;}

int mp[100][100];
int vs[100][100];
int bsno = 0;

int h, w;

int go(int i, int j) {
	if (vs[i][j] != -1) return vs[i][j];
	int bv = mp[i][j];
	
	if (i && mp[i-1][j] < bv) vs[i][j] = go(i-1,j), bv = mp[i-1][j];
	if (j && mp[i][j-1] < bv) vs[i][j] = go(i,j-1), bv = mp[i][j-1];
	if (j + 1 < w && mp[i][j+1] < bv) vs[i][j] = go(i,j+1), bv = mp[i][j+1];
	if (i + 1 < h && mp[i+1][j] < bv) vs[i][j] = go(i+1,j), bv = mp[i+1][j];
	
	if (bv == mp[i][j]) {
		vs[i][j] = bsno++;
	}
	
	return vs[i][j];
}

int bvs[30];
int bno = 0;

int main() {
	int tc;
	cin >> tc;
	
	
	FOR(atc,1,tc+1) {
		printf("Case #%d: ", atc);
		
		cin >> h >> w;
		REP(i, h) REP(j, w) scanf("%d", &mp[i][j]);
		ZERO(vs);
		bsno = 0;
		memset(vs, -1, sizeof vs);
		REP(i, h) REP(j, w) go(i, j);
		
		memset(bvs, -1, sizeof bvs);
		bno = 'a';
		REP(i, h) REP(j, w) {
			if (j == 0) printf("\n");
			if (j) printf(" ");
			if (bvs[vs[i][j]] == -1)
				bvs[vs[i][j]] = bno++;
			printf("%c", bvs[vs[i][j]]);
		}
		
		printf("\n");
	}
}
