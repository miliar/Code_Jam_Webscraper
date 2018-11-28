#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>

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
		int N;
		cin >> N;
		vi a(N), b(N);
		REP(i,N) cin >> a[i] >> b[i];
		int x = 0;
		REP(i,N)REP(j,i) if((a[i] - a[j]) * (b[i] - b[j]) < 0) x++;
		
		printf("Case #%d: %d\n", t + 1, x);
	}
	
	return 0;
}
