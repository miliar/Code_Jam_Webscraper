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

int DR[] = {1,2};
int DC[] = {2,1};

const int INF = 1000000000;
const double EPS = 1e-10;
const int MOD = 10007;
int R,C;
bool rock[128][128];
int mem[128][128];

int calc(int r,int c){
	int& ret = mem[r][c];
	if( ret != -1 ) return ret;
	if( r == R-1 && c == C-1 ) return ret = 1;
	ret = 0;
	REP(a,2){
		int r2 = r + DR[a], c2 = c + DC[a];
		if( r2 < R && c2 < C && !rock[r2][c2] ){
			ret += calc(r2,c2);
			ret %= MOD;
		}
	}
	return ret;
}
void run(int tc){
	int B;
	cin >> R >> C >> B;
	REP(r,R) REP(c,C){
		rock[r][c] = false;
		mem[r][c] = -1;
	}
	REP(_,B){
		int r,c;
		cin >> r >> c;
		rock[r-1][c-1] = true;
	}
	cout << "Case #" << tc << ": " << calc(0,0) << endl;
}
int main(){
	int TC;
	cin >> TC;
	FORE(tc,1,TC) run(tc);
	return 0;
}
