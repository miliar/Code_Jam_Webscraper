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
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())
#define MP(x,y) make_pair(x,y)

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

int T;
int n;
ll a[2000], b[2000];

int main() {
	cin >> T;
	REP(t, T) {
		cin >> n;
		REP(i, n) cin >> a[i];
		REP(i, n) cin >> b[i];
		sort(a, a+n);
		sort(b, b+n);
		reverse(b, b+n);
		ll tot = 0;
		REP(i, n) tot += a[i]*b[i];
		cout << "Case #" << t+1 << ": " << tot << endl;
	}
	return 0;
}
