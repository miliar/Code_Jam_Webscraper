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

string words[5000];
int main() {
	int l, d, n;
	cin >> l >> d >> n;
	REP(i, d) {
		cin >> words[i];
		REP(j, l) words[i][j] = (words[i][j] - 'a');
	}
	
	FOR(atc,1,n+1) {
		string s;
		cin >> s;
		int bs[20];
		ZERO(bs);
		int pos = 0;
		REP(i, s.S) {
			if (s[i] == '(') {
				while (s[++i] != ')') {
					bs[pos] |= 1 << (s[i] - 'a'); 
				}
			} else {
				bs[pos] = 1 << (s[i] - 'a');
			}
			pos++;
		}

		int no = 0;
		REP(i, d) {
			REP(j, l) if (!((1 << words[i][j]) & bs[j])) {
				goto next;
			}
			no++;
			next: ;
		}
		
		printf("Case #%d: ", atc);
		cout << no;
		printf("\n");
	}
}
