// C++11

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
#include <unordered_map>
#include <unordered_set>
#include <tuple>
using namespace std;


typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define FORD(i,a,b) for(int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for(__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define pb push_back
#define mp make_pair

int main () {
	int T;
	cin >> T;

	FOR(t,1,T+1) {
		int N, S, P, tmp, result = 0;
		cin >> N >> S >> P;

		FOR(i,0,N) {
			cin >> tmp;
			int best = (tmp + 2) / 3;
			if (best + 1 == P && S > 0) {
				if ((tmp % 3 == 0 && tmp >= 3) || (tmp % 3 == 2)) {
					best++;
					S--;
				}
			}
			if (best >= P) result++;
		}

		cout << "Case #" << t << ": " << result << endl;
	}

	return 0;
}
