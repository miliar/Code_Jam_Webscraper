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
#define SIZE(c) ((int)(c).size())
#define FORIT(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()

typedef vector<string> VS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<VI> VVI;

// BEGIN CUT HERE
#define DEBUG(x) cerr<<#x<<'='<<x<<endl
ostream& operator<<(ostream& o,const VS& c){ FORIT(p,c) o<<*p<<endl; return o; }
template<class T> ostream& operator<<(ostream& o,const vector<T>& c){ FORIT(p,c) o<<*p<<" "; return o; }
template<class T> ostream& operator<<(ostream& o,const vector<vector<T> >& c){ FORIT(p,c) o<<*p<<endl; return o; }
template<class U,class V> ostream& operator<<(ostream& o,const pair<U,V>& p){ return o<<'('<<p.first<<','<<p.second<<')'; }
template<class T> ostream& operator<<(ostream& o,const set<T>& c){ FORIT(p,c) o<<*p<<" "; return o; }
template<class U,class V> ostream& operator<<(ostream& o,const map<U,V>& c){ FORIT(p,c) o<<*p<<" "; return o; }
template<class T> ostream& operator<<(ostream& o,queue<T> c){ while(!c.empty()) o<<c.front()<<" ",c.pop(); return o; }
// END CUT HERE

const int TOTAL = 24 * 60;
const int EXTRA = 64;

// global
int NA,NB;
VVI TA,TB;
VI CA,CB;

int parseTime(const string& s){
	assert( SIZE(s) == 5 );
	assert( s[2] == ':' );
	assert( isdigit(s[0]) );
	assert( isdigit(s[1]) );
	assert( isdigit(s[3]) );
	assert( isdigit(s[4]) );
	int h = atoi(s.substr(0,2).c_str());
	int m = atoi(s.substr(3,2).c_str());
	assert( 0 <= h && h <= 23 );
	assert( 0 <= m && m <= 59 );
	return h * 60 + m;
}
void parseTimes(int N,VVI& T,int turn){
	T = VVI(TOTAL + EXTRA);
	REP(t,N){
		string departure, arrival;
		cin >> departure >> arrival;
		int time1 = parseTime(departure);
		int time2 = parseTime(arrival);
		assert( time1 < time2 );
		T[time1].push_back(time2 + turn);
	}
}
int doit(int time, const VVI& T, VI& C1, VI& C2){
	int ret = 0;
	for( int d = 0; d < SIZE(T[time]); d++ ){
		if( C1[time] == 0 ){
			ret++;
		} else {
			C1[time]--;
		}
		C2[T[time][d]]++;
	}
	return ret;
}
int main(){
	int TC;
	cin >> TC;
	for( int tc = 1; tc <= TC; tc++ ){
		int turn;
		cin >> turn >> NA >> NB;
		parseTimes(NA,TA,turn);
		parseTimes(NB,TB,turn);

		CA = VI(TOTAL + EXTRA,0);
		CB = VI(TOTAL + EXTRA,0);

		int retA = 0, retB = 0;
		for( int t = 0; t < TOTAL; t++ ){
			retA += doit(t,TA,CA,CB);
			retB += doit(t,TB,CB,CA);
			CA[t+1] += CA[t];
			CB[t+1] += CB[t];
		}
		cout << "Case #" << tc << ": " << retA << " " << retB << endl;
	}
	return 0;
}
