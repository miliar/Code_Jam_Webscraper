#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
typedef long long LL;
typedef long double LD;
#define REP(I,N) for(int I=0;I<(N);++I)
#define FOR(I,A,B) for(int I=(A);I<=(B);++I)
#define FORD(I,A,B) for(int I=(A);I>=(B);--I)
#define FOREACH(I,C) for(__typeof((C.begin())) I=(C).begin();I!=(C).end();++I)
template<class T> inline void debug(const T&c) { cout << "{"; FOREACH(it,c) cout << *it << ","; cout << "}" << endl; }
template<class T> inline void setmin(T &a,const T& b){if(b<a) a=b;}
template<class T> inline void setmax(T &a,const T& b){if(b>a) a=b;}
template<class T> inline int size(const T&c) { return (int)c.size(); }
template<class T> inline string to_str(const T& a) { ostringstream os(""); os << a; return os.str(); }
template<class T> inline T sqr(const T&a) { return a*a; }
template<class T> T next() { T x; cin >> x; return x; }
int next_int() { int x; scanf("%d",&x); return x; }
#define all(A) (A).begin(),(A).end()
#define st first
#define nd second
#define mp make_pair
#define pb push_back

char graph[250][250];
bool bad[250][250];

void solve() {
	int comb;
	int opos;
	
	REP(i,250) {
		REP(j,250) {
			graph[i][j] = 0;
			bad[i][j] = 0;
		}
	}
	
	cin >> comb;
	REP(i, comb) {
		string s;
		cin >> s;
		graph[s[0]][s[1]] = s[2];		
		graph[s[1]][s[0]] = s[2];
	}
	
	cin >> opos;
	REP(i, opos) {
		string s;
		cin >> s;
		bad[s[0]][s[1]] = true;
		bad[s[1]][s[0]] = true;
	}
	
	int n;
	cin >> n;
	string seq;
	cin >> seq;
	
	vector<char> res;
	REP(i, n) {
		char c = seq[i];
		
		if (res.empty()) {
			res.pb(c);
			continue;
		}	
		
		char d = res.back();
			
		if (graph[c][d]) {
			res.pop_back();
			res.pb(graph[c][d]);
			continue;
		} 
		
		int ok = true;
		FOREACH(it, res) 
			if (bad[*it][c]) ok = false;
		
		if (!ok) {
			res.clear();
		} else {
			res.pb(c);
		}
	}
	
	printf("[");
	REP(i, res.size()) {
		printf("%c", res[i]);
		if (i + 1 != res.size()) printf(", ");
	} 
	printf("]\n");
}

int main() {
	int tests;
	scanf("%d\n",&tests);
	FOR(test,1,tests) {
		printf("Case #%d: ", test);
		solve();
	}
	return 0;
}

















