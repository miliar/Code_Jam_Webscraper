#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

void main() {
	int order[1001];
	int nextone[1001];
	long long made[1001];
	long long nowmade[1001];
	long long g[1001];

	int T;
	int R;
	int k;
	int N;
	int i, j;

	scanf("%d", &T);

	REP(i, T) {
		scanf("%d %d %d", &R, &k, &N);
		REP(j, N)
			cin >> g[j];

		memset(order, 0, sizeof(order));
		memset(nextone, 0, sizeof(nextone));
		memset(made, 0, sizeof(made));
		memset(nowmade, 0, sizeof(nowmade));

		int ti = 1;
		int ind = 0;
		long long tom = 0;

		while (order[ind] == 0 && ti <= R) {
			order[ind] = ti++;
			made[ind] = tom;
			long long rid = 0;
			int next = ind;
			while (rid + g[next] <= (long long)k) {
				rid += g[next];
				next = (next + 1) % N;
				if (ind == next)
					break;
			}
			tom += rid;
			nowmade[ind] = rid;

			nextone[ind] = next;
			ind = next;
		}

		if (ti > R) {
			cout << "Case #" << (i+1) << ": " << tom << endl;
		} else {
			int remained = R - order[ind];
			int tim = remained / (ti - order[ind]);
			int tim2 = remained % (ti - order[ind]);

			long long res = made[ind] + tim * (tom - made[ind]);

			while (tim2 >= 0) {
				res += nowmade[ind];
				ind = nextone[ind];
				--tim2;
			}
			cout << "Case #" << (i+1) << ": " << res << endl;
		}
	}
}