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

pair<pii, int> a[1024];

bool cmp(const pair<pii, int> & q, const pair<pii, int> & w) {
    if (q.X.X * w.X.Y == q.X.Y * w.X.X) {
	return q.Y < w.Y;
    }
    return q.X.X * w.X.Y < q.X.Y * w.X.X;
}

int main () {
    freopen((testname+".in").c_str(), "r", stdin);
    if (testname != "input") {
	freopen((testname+".out").c_str(), "w", stdout);
    }
    int tests;
    cin >> tests;
    FOR (test, 1, tests+1) {
	int n;
	cin >> n;	
	REP (i, n) {
	    cin >> a[i].X.X;
	}
	REP (i, n) {
	    cin >> a[i].X.Y;
	}
	REP (i, n) {
	    a[i].Y = i;
	}
	sort(a, a + n, cmp);
	cout << "Case #" << test << ":";
	REP (i, n) {
	    cout << ' ' << a[i].Y;
	}
	cout << endl;
    }
    return 0;
}
