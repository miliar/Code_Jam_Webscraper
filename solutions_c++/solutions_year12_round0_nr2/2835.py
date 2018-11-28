#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stdio.h>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <time.h>

using namespace std;

#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()
#define sz(v) (int) v.size()
#define mp make_pair
#define pb push_back

int main() {
	freopen("B-large.in", "rt", stdin);
	freopen("out.out", "wt", stdout);
	int T, N, S, P, t, count = 1, res;
	cin >> T;
	while (T--) {
		res = 0;
		cin >> N >> S >> P;
		FOR(i, 0, N) {
			cin >> t;
			if (t %3 == 0) {
				if (t / 3 >= P)
					res++;
				else if (S && t && (t / 3) + 1 >= P){
					res++;
					S--;
				}
			} else if (t %3 == 1 && (t / 3) + 1 >= P) {
				res++;
			} else if (t %3 == 2){
				if ((t / 3) + 1 >= P)
					res++;
				else if (S && (t / 3) + 2 >= P) {
					res++;
					S--;
				}
			}
		}
		cout << "Case #" << count++ << ": " << res << endl;
	}
	return 0;
}
