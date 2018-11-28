#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cmath>

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define ALL(cont) cont.begin(), cont.end()

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vl;
typedef vector<double> vd;

int main()
{
	int T;
	cin >> T;
	REP(t,T)
	{
		int L, P, C;
		cin >> L >> P >> C;
		int ans = ceil(log2(ceil((log((double)P / L)) / log(C))));
		
		printf("Case #%d: %d\n", t + 1, ans);
	}
	
	return 0;
}
