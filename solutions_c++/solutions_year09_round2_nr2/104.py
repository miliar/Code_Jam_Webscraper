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

int T;
string N;

int main() {
	cin >> T;
	FOR(cs, 1, T+1) {
		cin >> N;
		cout << "Case #" << cs << ": ";
		if (next_permutation(all(N))) {
			cout << N << endl;
		} else {
			char first;
			FOR(i, 0, sz(N)) {
				if (N[i] != '0') {
					first = N[i];
					N[i] = '0';
					break;
				}
			}
			cout << first << N << endl;
		}
	}
	return 0;
}
