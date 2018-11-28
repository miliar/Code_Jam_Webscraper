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

int T, N, D, dst[20000], len[20000], maxd[20000];

int main() {
	scanf("%d", &T);
	FOR(cs, 1, T+1) {
		scanf("%d", &N);
		FOR(i, 0, N) scanf("%d%d", &dst[i], &len[i]);
		scanf("%d", &D);
		memset(maxd, -1, sizeof(maxd));
		maxd[0] = dst[0];
		bool poss = false;
		FOR(i, 0, N) {
			if (dst[i] + maxd[i] >= D) {
				poss = true;
				break;
			}
			FOR(j, i+1, N) {
				if (dst[i] + maxd[i] < dst[j]) break;
				maxd[j] = max(maxd[j], min(dst[j] - dst[i], len[j]));
			}
		}
		if (poss) {
			cout << "Case #" << cs << ": YES" << endl;
		} else {
			cout << "Case #" << cs << ": NO" << endl;
		}
	}
	return 0;
}
