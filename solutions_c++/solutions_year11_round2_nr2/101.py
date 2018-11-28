#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <cstring>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

int c, d, p , v;

int main() {
	int casos;
	cin >> casos;
	REP(caso, casos) {
		cin >> c >> d;
		vector<int> l;
		REP(i, c) {
			cin >> p >> v;
			REP(j, v) l.pb(p);
		}
		double total = 0.0;
		double partial = 0.0;
		REP(i, SZ(l)-1) {
			partial += d - (l[i+1] - l[i]);
			//cout << l[i] << l[i+1] << endl;
			if (partial > total) total = partial;
			if (partial < 0) partial = 0;
			//cout << partial << endl;
		}
		cout << "Case #" << fixed << setprecision(2) << caso+1 << ": " << total/2.0 << endl;
	}
	return 0;
}
