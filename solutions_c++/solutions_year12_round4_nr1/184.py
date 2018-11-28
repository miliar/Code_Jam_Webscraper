#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define UN(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset ((a), (b), sizeof (a))
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

string testname = "A-large";

const int N = 10124;

int a[N], b[N], c[N];

int main () {
    freopen((testname+".in").c_str(), "r", stdin);
    freopen((testname+".out").c_str(), "w", stdout);
    int t;
    cin >> t;
    FOR (test, 1, t+1) {
	int n;
	cin >> n;
	REP (i, n) {
	    cin >> a[i] >> b[i];
	}
	cin >> a[n];
	++n;
	memset (c, -1, sizeof (c));
	c[0] = a[0];
	REP (i, n) if (c[i] != -1) {
	    FOR (j, i+1, n) if (c[i] >= a[j] - a[i]) {
		c[j] = max (c[j], min (a[j] - a[i], b[j]));
	    }
	}
	printf("Case #%d: ", test);
	if (c[n-1] == -1) puts("NO"); else puts("YES");
    }
    return 0;
}
