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

string testname = "B-large";

int ask(map<int, int> & D, int x1, int x2) {
    map<int, int>::iterator it = D.lower_bound(x1+1);
    --it;
    int res = 0;
    while (it != D.end() && it->X < x2) {
	res = max(res, it->Y);
	++it;
    }
    return res;
}

void out(map<int, int> & D) {
    for(map<int, int>::iterator it = D.begin(); it != D.end(); ++it) {
	cout << it->X << ' ' << it->Y << ", ";
    }
    cout << endl;
}

int main () {
    freopen((testname+".in").c_str(), "r", stdin);
    freopen((testname+".out").c_str(), "w", stdout);
    int t;
    cin >> t;
    FOR (test, 1, t+1) {
	int n, w, l;
	cin >> n >> w >> l;
	map<int, int> D;
	D[0] = 0;
	D[w] = 0;
	//	out(D);
	int r;
	vector<pii> ans;
	printf("Case #%d:", test);
	vector<int> R(n);
	REP (i, n) {
	    cin >> r;
	    R[i] = r;
	    //	    cout << "i = " << i << " r = " << r << endl; 
	    int besty = ask(D, 0, r), bestx = -r;
	    for (map<int, int>::iterator it = D.begin(); it != D.end(); ++it) {
		int x = it->X;
		if (x + r <= w) {
		    int y = ask(D, x, x+2*r);
		    //		    cout << "Try x = " << x << " --> y = " << y << endl;
		    if (y < besty) {
			besty = y;
			bestx = x;
		    }
		}
	    }
	    if (besty == 0) besty = -r;
	    printf(" %d %d", bestx+r, besty+r);
	    ans.pb(pii(bestx+r, besty+r));
	    int x = bestx, y = besty;
   	    map<int, int>::iterator e = D.lower_bound(x + 2*r + 1);
	    map<int, int>::iterator it = e;
	    --it;
	    int after = it->Y;
	    D.erase(D.lower_bound(x), e);
	    D[max(x, 0)] = y + 2*r;
	    D[min(x+2*r, w)] = after;
	}
	puts("");
	//  REP (i, sz(ans)) {
	//      if (ans[i].X < 0 || ans[i].Y < 0 || ans[i].X > w || ans[i].Y > l) {
	//  	while (1);
	//      }
	//  }
	// REP (i, sz (ans)) {
	//     REP (j, i) {
	// 	int dist = (
	//     }
	// }
    }
    return 0;
}
