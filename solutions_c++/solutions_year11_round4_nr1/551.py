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
typedef pair<int,int> PII;
typedef vector<int> VI;
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
int nint() { int x; scanf("%d",&x); return x; }
#define all(A) (A).begin(),(A).end()
#define st first
#define nd second
#define mp make_pair
#define pb push_back

bool comp(pair<PII,int> p1, pair<PII,int> p2) {
	return p1.nd < p2.nd;
}

void solve() {
	int dist = nint();
	int ws = nint();
	int rs = nint();
	double rt = nint();
	int n = nint();
	vector<pair<PII,int> > vec;
	double pos = 0; 
	REP(i,n) {
		int a=nint();
		int b=nint();
		int s=nint();
		vec.pb(mp(mp(pos,a),0));	
		vec.pb(mp(mp(a,b),s));	
		pos = b;
	}
	vec.pb(mp(mp(pos,dist),0));
	int m = vec.size();
	
	double result = 0;
	sort(vec.begin(), vec.end(), comp);
	
	REP(i,m){
		double a = vec[i].st.st;
		double b = vec[i].st.nd;
		double t1 = double(b-a) / double(vec[i].nd + rs);		
		if (t1 > rt) {
			a += rt * double(vec[i].nd + rs); // przesuwamy sie biegnac
			result += rt; 
			rt = 0;
			result += double(b-a) / double(vec[i].nd + ws);
		} else {
			result += t1;
			rt -= t1;
		}
		//printf("	%lf %lf\n",rt,t1);
	}

	printf("%.9lf\n",result);
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

















