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

const int INF = 2000000000;
const int MINQ = 0, MAXQ = 1000;
const int MINS = 2, MAXS = 100;

int mem[128][1024];

int calc(int S,VI& queries,int s,int q){
	if( q >= SIZE(queries) ) return 0;
	int& ret = mem[s][q];
	if( ret != -1 ) return ret;
	if( queries[q] == s ){
		ret = INF;
		REP(s2,S) if( s2 != s ){
			ret = min(ret, 1 + calc(S,queries,s2,q+1));
		}
		return ret;
	}
	return ret = calc(S,queries,s,q+1);
}
void addId(map<string,int>& idMap,const string& key){
	if( idMap.count(key) == 0 ){
		int id = idMap.size();
		idMap[key] = id;
	}
}
int solve(int S,VI& queries){
	int Q = SIZE(queries);
	if( Q <= 1 ) return 0;
	REP(s,S+1) REP(q,Q+1) mem[s][q] = -1;
	int ret = INF;
	REP(s,S) ret = min(ret, calc(S,queries,s,0));
	assert( ret <= Q - 1 );
	return ret;
}

int main(){
	int TC;
	cin >> TC;
	for( int tc = 1; tc <= TC; tc++ ){
		map<string,int> idMap;

		int S,Q;
		cin >> S;
		assert( S >= MINS );
		assert( S <= MAXS );

		string name;
		getline(cin,name);
		REP(i,S){
			getline(cin,name);
			addId(idMap,name);
		}

		cin >> Q;
		assert( Q >= MINQ );
		assert( Q <= MAXQ );

		getline(cin,name);
		VI queries;
		REP(i,Q){
			getline(cin,name);
			assert( idMap.count(name) != 0 );
			queries.push_back(idMap[name]);
		}

		cout << "Case #" << tc << ": " << solve(S,queries) << endl;
	}
	return 0;
}
