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

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int L, D, N;
string dict[10000];
bool poss[20][30];

int main() {
	cin >> L >> D >> N;
	FOR(i, 0, D) cin >> dict[i];
	string pattern;
	FOR(cs, 1, N+1) {
		cin >> pattern;
		memset(poss, 0, sizeof(poss));
		int p = 0;
		FOR(i, 0, sz(pattern)) {
			if (islower(pattern[i])) {
				poss[p][pattern[i]-'a'] = true;
			} else {
				i++;
				while (islower(pattern[i])) {
					poss[p][pattern[i]-'a'] = true;
					i++;
				}
			}
			p++;
		}
		int res = 0;
		FOR(i, 0, D) {
			bool b = true;
			FOR(j, 0, sz(dict[i])) {
				if (!poss[j][dict[i][j]-'a']) {
					b = false;
					break;
				}
			}
			if (b) res++;
		}
		cout << "Case #" << cs << ": " << res << endl;
	}
	return 0;
}
