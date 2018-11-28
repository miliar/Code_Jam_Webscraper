/*    muriloadriano @ topcoder
 *    muriloufg @ codeforces
 */
#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <deque>
#include <ctime>
#include <cfloat>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <list>
#include <iomanip>
#include <climits>
#include <sstream>
#include <queue>
#include <utility>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back
#define ff first
#define ss second
#define ti(x) typeof(x.begin())
#define all(x) x.begin(), x.end()
#define fill(x, y) memset(x, y, sizeof(x)) 

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int INF = 0x3f3f3f3f;
const double EPS = 1e-5;

template <typename T> T abs(const T& a) { if (a >= 0) return a; return -a; }


int main()
{
	ios::sync_with_stdio(false);
	
	long long n, pd, pg;
 	int tc;
	cin >> tc;
	
	for (int t = 1; t <= tc; ++t) {
		cin >> n >> pd >> pg;
		cout << "Case #" << t << ": ";
	
		if ((pg == 100 && pd < 100) || (pg == 0 && pd != 0)) { cout << "Broken\n"; continue; }
		
		long long x = __gcd(pd, 100LL);
		
		x = 100 / x;
		
		//cout << pd << ": " << __gcd(pd, 100LL) << ": " << x << endl;
		
		if (x <= n) cout << "Possible\n";
		else cout << "Broken\n";
	}
	return 0;
}




























