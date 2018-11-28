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
#define all(x) x.begin, x.end()
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
	int tc;
	cin >> tc;

	for (int t = 1; t <= tc; ++t) {
		vector<int> vet;
		int n;
		cin >> n;
		
		int x;
		unsigned has = 0;
		for (int i = 0; i < n; ++i) {
			cin >> x;
			has ^= x;
			vet.pb(x);
		}
			
		if (!has) {
			sort(vet.begin(), vet.end());
			
			int ans = 0;
			for (int i = 1; i < n; ++i) ans += vet[i];
			cout << "Case #" << t << ": " << ans << "\n";
		}
		else {
			cout << "Case #" << t << ": NO\n";
		}
	}
	
	
	return 0;
}




























