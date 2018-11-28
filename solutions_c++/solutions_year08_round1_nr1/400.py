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

typedef vector<string> VS;
typedef vector<int> VI;

// BEGIN CUT HERE
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<VI> VVI;
#define UNIQUE(v) (v).erase(unique(ALL(v)),(v).end())
// std::__gcd(a,b)
// __gnu_cxx::power(a,b)
#define DEBUG(x) cerr<<#x<<'='<<x<<endl
ostream& operator<<(ostream& o,const VS& c){ FORIT(p,c) o<<*p<<endl; return o; }
template<class T> ostream& operator<<(ostream& o,const vector<T>& c){ FORIT(p,c) o<<*p<<" "; return o; }
template<class T> ostream& operator<<(ostream& o,const vector<vector<T> >& c){ FORIT(p,c) o<<*p<<endl; return o; }
template<class U,class V> ostream& operator<<(ostream& o,const pair<U,V>& p){ return o<<'('<<p.first<<','<<p.second<<')'; }
template<class T> ostream& operator<<(ostream& o,const set<T>& c){ FORIT(p,c) o<<*p<<" "; return o; }
template<class U,class V> ostream& operator<<(ostream& o,const map<U,V>& c){ FORIT(p,c) o<<*p<<" "; return o; }
template<class T> ostream& operator<<(ostream& o,queue<T> c){ while(!c.empty()) o<<c.front()<<" ",c.pop(); return o; }
VS split(string s,string d){
    s+=d[0];
    VS r;
    string w;
    FORIT(i,s) if(d.find(*i)==string::npos) w+=*i; else if(w!="") r.push_back(w),w="";
    return r;
}
// END CUT HERE

LL solve(vector<LL>& A,vector<LL>& B){
	sort(ALL(A));
	sort(ALL(B));
	int N = SIZE(A);
	long long ret = 0;
	REP(i,N) ret += A[i] * B[N-1-i];
	return ret;
}
int main(){
	int TC;
	cin >> TC;
	FORE(tc,1,TC){
		int N;
		cin >> N;
		vector<LL> A(N),B(N);
		REP(i,N) cin >> A[i];
		REP(i,N) cin >> B[i];
		cout << "Case #" << tc << ": " << solve(A,B) << endl;
	}
	return 0;
}
