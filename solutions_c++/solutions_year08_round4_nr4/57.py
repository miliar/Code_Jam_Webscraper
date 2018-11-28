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

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

int inf;
int K;
string s;

int first;
int c[20][20];
int d[20][20];

int mem[1<<17][17];
int best(int mask, int last) {
	int &res = mem[mask][last];
	if (res == 0x3f3f3f3f) {
		if (mask == (1<<K)-1) {
			return d[last][first] + 1;
		} else {
			REP(next, K) if (!(mask & (1<<next))) {
				res <?= best(mask | (1<<next), next) + c[next][last];
			}
		}
	}
	return res;
}

int main() {
	int casos;
	cin >> casos;
	REP(caso, casos) {
		cin >> K;
		cin >> s;
		int pieces = SZ(s)/K;
		CLEAR(c, 0); CLEAR(d, 0);
		REP(i, pieces) REP(j, K) REP(k, K) c[j][k] += s[i*K+j] != s[i*K+k];
		REP(i, pieces-1) REP(j, K) REP(k, K) d[j][k] += s[i*K+j] != s[(i+1)*K+k];
		int m = SZ(s);
		for (first = 0; first < K; first++) {
			CLEAR(mem, 0x3f);
			m <?= best(1<<first, first);
		}
		cout << "Case #" << caso+1 << ": " << m << endl;
	}
	return 0;
}
