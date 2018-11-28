#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>

using namespace std;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define REPD(i,n) for (int i((n)-1); i >= 0; --i)
#define TRACE(x...) 
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << endl) 
#define ALL(v) (v).begin(), (v).end()

int main()
{
	int T,n,Y;
	vi v1,v2;
	scanf("%d ",&T);
	FOR(X,1,T) 
	{
		v1.clear(); v2.clear();
	scanf("%d ",&n);
		REP(i,n) {
			scanf("%d ",&Y);
			v1.push_back(Y);
		}
		REP(i,n) {
			scanf("%d ",&Y);
			v2.push_back(Y);
		}
		sort(ALL(v1));
		sort(ALL(v2));
		int total = 0;
		REP(i,n) {
			total += v1[i]*v2[n-i-1];
		}
		printf("Case #%d: %d\n",X,total);
	}
	return 0;
}
