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

const int MAXM = 10010;

bool isLeaf[MAXM];
bool isAnd[MAXM];
bool changes[MAXM];
bool value[MAXM];

int left(int p){ return 2*p + 1; }
int right(int p){ return 2*p + 2; }

int calc(int,int);

void relax(int node,int L,int R,int cost,int& ret){
	int curL = calc(left(node),L);
	int curR = calc(right(node),R);
	if( curL == -1 || curR == -1 ) return;
	if( ret == -1 || (ret > cost + curL + curR) ){
		ret = cost + curL + curR;
	}
}

int mem[MAXM][4];

int calc(int node,int V){
	int& ret = mem[node][V];
	if( ret != -2 ) return ret;
	if( isLeaf[node] ){
		return ret = (value[node] == V ? 0 : -1);
	}
	ret = -1;
	REP(L,2) REP(R,2){
		if( (L && R) == V ){
			int cost = 0;
			if( isAnd[node] || changes[node] ){
				if( !isAnd[node] ) cost++;
				relax(node,L,R,cost,ret);
			}
		}
		if( (L || R) == V ){
			int cost = 0;
			if( !isAnd[node] || changes[node] ){
				if( isAnd[node] ) cost++;
				relax(node,L,R,cost,ret);
			}
		}
	}
	return ret;
}
void run(int tc){
	int V,M;
	cin >> M >> V;
	REP(i,M){
		if( i < (M-1)/2 ){
			int G,C;
			cin >> G >> C;
			isLeaf[i] = false;
			isAnd[i] = G;
			changes[i] = C;
		}else{
			int val;
			cin >> val;
			isLeaf[i] = true;
			value[i] = val;
		}
	}
	REP(i,M) REP(v,4) mem[i][v] = -2;
	int ret = calc(0,V);
	cout << "Case #" << tc << ": ";
	if( ret == -1 ){
		cout << "IMPOSSIBLE" << endl;
	}else{
		cout << ret << endl;
	}
}
int main(){
	int TC;
	cin >> TC;
	FORE(tc,1,TC) run(tc);
	return 0;
}
