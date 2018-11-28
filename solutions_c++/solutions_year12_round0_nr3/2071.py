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

string testname = "C-large";

int ov[2100000];
int it;

int main () {
    freopen((testname+".in").c_str(), "r", stdin);
		freopen((testname+".out").c_str(), "w", stdout);
		int t;
		cin >> t;
		REP (i, t) {
				int a, b;
				cin >> a >> b;
				int res = 0;
				FOR (i, a, b+1) {
						int y = 0, x = i, z = 1;
						while (x) {
								x /= 10;
								++y;
								z *= 10;
						}
						z /= 10;
						int f = i;
						++it;
						REP (j, y-1) {
								f = f / 10 + (f%10) * z;
								if (f > i && (f <= b)) {
										res += (ov[f] != it);
										ov[f] = it;
								}
						}
				}
				cout << "Case #" << (i+1) << ": ";
				cout << res << endl;
		}
    return 0;
}
