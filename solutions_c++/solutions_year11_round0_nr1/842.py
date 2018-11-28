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

int pos[2];
queue< pair<int,int> > Q[2];

void make_move(int who, bool can_push) {
	if (pos[who] == Q[who].front().nd) {
		if (can_push) {
			Q[who].pop();
		} 
	} else if (pos[who] < Q[who].front().nd) {
		++pos[who];
	} else {
		--pos[who];
	}
}

int go() {
	if (Q[0].empty() && Q[1].empty()) 
		return false;

	if (Q[0].empty()) 
		make_move(1, 1);
	else if (Q[1].empty()) 
		make_move(0, 1);		
	else {
		int priority_0 = Q[0].front().st;
		int priority_1 = Q[1].front().st;
		
		if (priority_0 < priority_1) {
			make_move(1, 0);
			make_move(0, 1);
		} else {
			make_move(0, 0);
			make_move(1, 1);	
		}
	}
	return true;
}

void solve(int test) {
	int n;
	scanf("%d ", &n);
	
	FOR(i,1,n) {
		int where;
		char id;
		scanf("%c %d ", &id, &where);
		if (id == 'O') Q[0].push(mp(i, where));
		if (id == 'B') Q[1].push(mp(i, where));
	}
	
	pos[0] = pos[1] = 1;
	int result = 0;
	while (go()) {
		//printf("-------------------\n");
		++result;
	}
	
	printf("Case #%d: %d\n", test, result);
}

int main() {
	int tests = next_int();
	FOR(test, 1, tests) {
		solve(test);
	}
	return 0;
}

















