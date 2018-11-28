#include <algorithm>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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
inline int next_int() { int x; scanf("%d",&x); return x; }
#define all(A) (A).begin(),(A).end()
#define st first
#define nd second
#define mp make_pair
#define pb push_back

int vend[1009];
LD pos[1009];
LD D;
vector< pair<int,int> > vec;

bool check(LD value){
	LD left_limit = -1e25;
	
	FOREACH(it,vec){
		left_limit = max(it->st - value, left_limit + D);
		left_limit += (it->nd - 1) * D;
		
		if (left_limit + 1e-10 < it->st) continue;
		if (left_limit - it->st > value + 1e-10) return false;
	}
	return true;
}


void solve() {	
	int n=next_int();
	int d=next_int();
	D=d;
	vec.clear();
	FOR(i,1,n){
		int pos=next_int();
		int vend=next_int();	
		vec.pb(mp(pos,vend));
	}
	sort(vec.begin(),vec.end());
	LD lo = 0;
	LD hi = 1e25;
	FOR(steps,1,500){
		LD mid=(lo+hi)/2.;
		if(check(mid)){
			hi=mid;
		}else lo=mid;
	}
	printf("%.9llf\n",(lo+hi)/2.);
}

int main() {
	int tests=next_int();
	FOR(test,1,tests){
		printf("Case #%d: ",test);
		solve();
	}
	return 0;
}



















