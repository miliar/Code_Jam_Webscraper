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
#define sz size()

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

map<string, int> names;
int best[2000][200];

int main() {
	string name;
	int casos, S, Q;
	cin >> casos;
	REP(caso, casos) {
		names.clear();
		cin >> S;
		cin.ignore(100, '\n');
		REP(i, S) {
			getline(cin, name);
			names[name] = i;
		}
		CLEAR(best[0], 0);
		cin >> Q;
		cin.ignore(100, '\n');
		FOR(i, 1, Q+1) {
			getline(cin, name);
			if (names.find(name) == names.end()) cout << "ERROR!!" << endl;
			int val = names[name];
			REP(j, S) {
				best[i][j] = 0x3fffffff;
				if (j != val) {
					best[i][j] = best[i-1][j];
					REP(k, S) best[i][j] <?= best[i-1][k] + 1;
				}
			}
		}
		/*REP(i, Q+1) {
			REP(j, S) cout << setw(20) << best[i][j] << " ";
			cout << endl;
		}*/
		cout << "Case #" << caso + 1 << ": ";
		cout << *min_element(best[Q], best[Q] + S) << endl;
	}
	return 0;
}
