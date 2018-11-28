#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <ext/hash_set>
#include <ext/hash_map>
#include <ext/numeric>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define REPE(i,n) FORE(i,0,n)
#define SIZE(c) ((int)(c).size())
#define FORIT(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()
#define UNIQUE(v) (v).erase(unique(ALL(v)),(v).end())
#define SORT(v) sort(ALL(v))

typedef long long LL;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef pair<int,int> PII;

#define DEBUG(x) cerr<<#x<<'='<<x<<endl
ostream& operator<<(ostream& o,const VS& c){ FORIT(p,c) o<<*p<<endl; return o; }
template<class T> ostream& operator<<(ostream& o,const vector<T>& c){ FORIT(p,c) o<<*p<<" "; return o; }
template<class T> ostream& operator<<(ostream& o,const vector<vector<T> >& c){ FORIT(p,c) o<<*p<<endl; return o; }
template<class U,class V> ostream& operator<<(ostream& o,const pair<U,V>& p){ return o<<'('<<p.first<<','<<p.second<<')'; }
template<class T> ostream& operator<<(ostream& o,const set<T>& c){ FORIT(p,c) o<<*p<<" "; return o; }
template<class U,class V> ostream& operator<<(ostream& o,const map<U,V>& c){ FORIT(p,c) o<<*p<<" "; return o; }
template<class T> ostream& operator<<(ostream& o,queue<T> c){ while(!c.empty()) o<<c.front()<<" ",c.pop(); return o; }

int oneCount(int n){ return n > 0 ? 1 + oneCount(n & (n-1)) : 0; }
int bitCount(int n){ return n > 0 ? 1 + bitCount(n / 2) : 0; }
VS split(string s,string d){
    s+=d[0];
    VS r;
    string w;
    FORIT(i,s) if(d.find(*i)==string::npos) w+=*i; else if(w!="") r.push_back(w),w="";
    return r;
}
// std::__gcd(a,b)
// __gnu_cxx::power(a,b)

LL myabs(LL n){ return n < 0 ? -n : n; }

LL N,M;

LL det(LL x1,LL y1,LL x2,LL y2){
	return x1*y2 - y1*x2;
}
LL area2(LL x1,LL y1,LL x2,LL y2,LL x3,LL y3){
	return myabs(det(x2-x1,y2-y1,x3-x1,y3-y1));
}
bool good(LL x2,LL y2,LL x3,LL y3,LL& x0,LL& y0){
	LL minx = 0 <? x2 <? x3;
	LL maxx = 0 >? x2 >? x3;
	LL miny = 0 <? y2 <? y3;
	LL maxy = 0 >? y2 >? y3;
	if( maxx - minx >  N || maxy - miny > M ) return false;
	x0 = -minx;
	y0 = -miny;
	return true;
}
#define CHECK(a,A) assert( 0 <= (a) && (a) <= A )

void run(int tc){
	LL A;
	cin >> N >> M >> A;
	cout << "Case #" << tc << ": ";
	FORE(x2,-N,N)FORE(y2,-M,M) FORE(x3,-N,N)FORE(y3,-M,M){
		LL x0,y0;
		if( myabs(det(x2,y2,x3,y3)) == A && good(x2,y2,x3,y3,x0,y0) ){
			CHECK(x0,N);
			CHECK(y0,M);
			CHECK(x2+x0,N);
			CHECK(y2+y0,M);
			CHECK(x3+x0,N);
			CHECK(y3+y0,M);
			cout << x0 << " " << y0 << " " << x2+x0 << " " << y2+y0 << " " << x3+x0 << " " << y3+y0 << endl;
			return;
		}
	}
	cout << "IMPOSSIBLE" << endl;
}
int main(){
	int TC;
	cin >> TC;
	FORE(tc,1,TC) run(tc);
	return 0;
}
