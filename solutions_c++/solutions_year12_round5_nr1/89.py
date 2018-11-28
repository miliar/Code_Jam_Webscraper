#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int T, N;
pair<pii, int> levels[2000];

int main() {
	cin >> T;
	FOR(cs, 1, T+1) {
		cin >> N;
		FOR(i, 0, N) cin >> levels[i].first.second;
		FOR(i, 0, N) cin >> levels[i].first.first;
		FOR(i, 0, N) levels[i].first.first = -levels[i].first.first;
		FOR(i, 0, N) levels[i].first.second = -levels[i].first.second;
		FOR(i, 0, N) levels[i].second = i;
		sort(levels, levels + N);
		cout << "Case #" << cs << ":";
		FOR(i, 0, N) cout << ' ' << levels[i].second;
		cout << endl;
	}
	return 0;
}
