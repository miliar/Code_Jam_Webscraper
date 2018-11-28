#define MAX_TIME 20.0

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
#include <sys/time.h>
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
#define PL            pair < PII, PII >
#define X           first
#define Y           second
#define VC          vector
#define VI          VC<int>
#define VD            VC<double>
#define VVI         VC< VI >
#define VS          VC<string>
#define VPII        VC< PII >
#define DB(a)       cerr << #a << ": " << a << endl;

void print(VI v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
void print(VD v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
void print(VS v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
void print(VVI v) {cerr << "[ ---";if (v.S) cerr << " ", print(v[0]);FOR(i, 1, v.S) cerr << " ", print(v[i]);    cerr << "--- ]\n";}
void print(PII p) {cerr << "{" << p.X << ", " << p.Y << "}";}
void print(VPII v) {cerr << "[";if (v.S) print(v[0]);FOR(i, 1, v.S)  cerr << ", ", print(v[i]);cerr << "]\n";}

template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS rv; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) rv.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) rv.PB(s.substr(p)); return rv;}

double getTime() {
    unsigned LL time;
    __asm__ volatile ("rdtsc" : "=A" (time));
#ifdef LOCAL
    return time / 2.8e9; 
#else
    return time / 3.6e9;
#endif
}

int main() {
	int n;
	cin >> n;
	REP(i, n) {
		LL a, b;
		cin >> a >> b;
		LL x = 1ll << a;
		b %= x;
		cout << "Case #" << (i + 1) << ": " << (b == x - 1 ? "ON" : "OFF") << endl;
	}
}
