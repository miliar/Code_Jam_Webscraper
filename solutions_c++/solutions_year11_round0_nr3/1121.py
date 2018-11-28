#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef long long Int;
typedef pair<long long, long long> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int main(){
	int test, tcase = 1;
	cin >> test;
	while( test-- ){
		int n;
		cin >> n;
		Int mini = -1;
		Int sum = 0 , xo = 0;
		REP( i , n ){
			Int data;
			cin >> data;
			sum += data;
			xo ^= data;
			if( mini == -1 || mini > data ) mini = data;
		}
		cout << "Case #" << tcase++  << ": ";
		if( xo != 0 ) cout << "NO" << endl;
		else cout << sum - mini << endl;
	}
	return 0;
}

