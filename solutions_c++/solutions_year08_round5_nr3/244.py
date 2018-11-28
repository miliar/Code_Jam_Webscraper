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
#define CONTAINS(S,X) (((S)&(1LL<<(X)))>0)

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

// UP, RIGHT, DOWN, LEFT
int DR[] = {-1,0,+1,0};
int DC[] = {0,+1,0,-1};

const int INF = 1000000000;
const double EPS = 1e-10;

VS room;
int R,C;
int mem[12][1<<12];

bool good(int S,int r,int bad){
	if( (S & bad) > 0 ) return false;
	REP(c,C) if( CONTAINS(S,c) && room[r][c] == 'x' ) return false;
	FOR(c,1,C) if( CONTAINS(S,c) && CONTAINS(S,c-1) ) return false;
	return true;
}
int getBad(int S){
	int ret = 0;
	REP(c,C) if( CONTAINS(S,c) ){
		if( c > 0 ) ret |= 1 << (c-1);
		if( c < C-1 ) ret |= 1 << (c+1);
	}
	return ret;
}
int calc(int r,int bad){
	if( r == -1 ) return 0;
	int& ret = mem[r][bad];
	if( ret != -1 ) return ret;
	ret = 0;
	REP(s,1<<C) if( good(s,r,bad) ){
		ret = max(ret, oneCount(s) + calc(r-1,getBad(s)));
	}
	return ret;
}
void run(int tc){
	cin >> R >> C;
	room = VS(R);
	REP(r,R) cin >> room[r];
	REP(r,12) REP(bad,1<<12) mem[r][bad] = -1;
	cout << "Case #" << tc << ": " << calc(R-1,0) << endl;
}
int main(){
	int TC;
	cin >> TC;
	FORE(tc,1,TC) run(tc);
	return 0;
}
