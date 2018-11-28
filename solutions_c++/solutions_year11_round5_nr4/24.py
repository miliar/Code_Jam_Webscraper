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

string s;
string f;

bool issquare(ll x) {
	for (ll y = max(ll(sqrtl(x))-10,0LL); y < ll(sqrtl(x))+10; y++) if (y*y == x) return true;
	return false;
}

void go(int i) {
	if (i == SZ(s)) {
		ll x = 0;
		REP(i, SZ(f)) x = 2*x + (f[i]-'0');
		if (issquare(x)) cout << f << endl;
	} else {
		if (s[i] == '?') {
			f[i] = '0'; go(i+1);
			f[i] = '1'; go(i+1);
		} else {
			go(i+1);
		}
	}
}

int main() {
	int casos;
	cin >> casos;
	REP(caso, casos) {
		cin >> s;
		f = s;
		cout << "Case #" << caso+1 << ": ";
		go(0);
	}
	return 0;
}
