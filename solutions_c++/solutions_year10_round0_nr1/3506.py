#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <ctime>
#include <sstream>
#include <iomanip>
#include <map>
#include <set>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef set<int> SI;
typedef set<string> SS;
typedef long long ll;
typedef unsigned long long ull;

#define REP(i,n) for(int i=0;i<(n);++i)
#define DREP(i,n) for(int i=(n)-1;i>=0;--i)
#define FOR(i,n,m) for(int i=(n);i<(m);++i)
#define DFOR(i,n,m) for(int i=(n);i>=(m);--i)
#define LOOP for(;;)
#define zero(n) memset((n),0,sizeof(n))
#define RMB(x) (x).erase((x).begin())
#define RME(x) (x).erase((x).end()-1)
#define SORT(x) sort((x).begin(),(x).end())
#define PB push_back
#define ISS istringstream
#define OSS ostringstream




int main ( void )
{
	int t;
	long long k, n;
	long long m;

	cin >> t;

	long long b[35] = {0};
	b[0] = 1;
	b[1] = 2;
	REP ( i, 30 ) {
		b[i+2] = b[i+1] * 2;

	}

	REP ( i, t ) {
		cin >> n >> k;
		m = k % b[n];
		if ( m == b[n] - 1 ) {
			cout << "Case #" << i+1 << ": ON" << endl;
		} else {
			cout << "Case #" << i+1 << ": OFF" << endl;
		}

	}
	return 0;

}

