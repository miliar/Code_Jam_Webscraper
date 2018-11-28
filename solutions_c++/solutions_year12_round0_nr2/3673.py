#include <cassert>
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
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp make_pair
#define pb push_back

int m[31][2];

int main() {

	int T;
	cin >> T;
	FOR(i, 0, 31) m[i][0] = m[i][1] = -1;
	FOR(t, 1, T+1) {
		int N, S, P, res = 0, x;
		cin >> N >> S >> P;
		FOR(i, 0, N) {
			cin >> x;
			if (m[x][0] < 0) {
				FOR(j, 0, 11) {
					FOR(k, 0, 11) {	
						FOR(l, 0, 11) {
							if (l+k+j == x) {
								int n = max(l,max(k,j));
								if (n-k <= 1 && n-j <= 1 && n-l <= 1)
									m[x][0] = max(m[x][0], n);
								if (n-k <= 2 && n-j <= 2 && n-l <= 2)
									m[x][1] = max(m[x][1], n);
							}
						}
					}
				}
			}
			if (m[x][0] >= P)
				res++;
			else if (m[x][1] >= P && S-- > 0)
				res++;
		}
		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
