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

void solve() {
	int n = next_int();
	int mini = 1<<30;
	int x = 0;
	int sum = 0;
	FOR(i,1,n) {
		int a = next_int();
		x ^= a;
		sum += a;
		setmin(mini, a);
	}
	if (x != 0) {
		printf("NO\n");
	} else {
		printf("%d\n",sum - mini);
	}
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

















