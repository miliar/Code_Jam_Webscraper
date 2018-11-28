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

int N, M, A;

int main() {
	int casos;
	cin >> casos;
	REP(caso, casos) {
		cin >> N >> M >> A;
		bool found = false;
		REP(x1, N+1) REP(y1, M+1)
			REP(x2, N+1) REP(y2, M+1)
				if (x1*y2 - x2*y1 == A) {
					cout << "Case #" << caso+1 << ": 0 0 ";
					cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
					found = true;
					goto sal;
				}
		sal: if (!found) cout << "Case #" << caso+1 << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
