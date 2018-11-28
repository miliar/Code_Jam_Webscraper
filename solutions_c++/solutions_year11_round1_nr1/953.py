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
#include <cstring>

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

typedef pair<long long, long long> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int main(){
	int test;int tcase = 1; 
	long long n , pd , pg;
	scanf("%d",&test);
	while( test-- ){
		printf("Case #%d: ",tcase++ );
		scanf("%lld%lld%lld",&n,&pd,&pg);
		if( pg == 0 and pd != 0 ) printf("Broken\n");
		else if( pg == 100 and pd != 100 ){
			printf("Broken\n");
		}
		else if( pd == 100 ) printf("Possible\n");
		else if( pd < 100 and pg < 100) {
			long long g = __gcd( 100LL , pd );
			pd/=g;
			long long c2 = 100LL/g; 
			if( c2 <= n and c2 > pd )	printf("Possible\n");
			else		printf("Broken\n");
		}
	}
	return 0;
}

