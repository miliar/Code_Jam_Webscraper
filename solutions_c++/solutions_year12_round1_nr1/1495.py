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
double prob[110000];
double corprob[110000];

void main() {
	int T;

	cin >> T;

	int i, j;

	REP(i,T) {
		int A, B;
		cin >> A >> B;

		REP(j,A)
			cin >> prob[j];

		corprob[0] = prob[0];
		FOR(j,1,A - 1) {
			corprob[j] = corprob[j-1] * prob[j];
		}

		FOR(j,A,B - 1) {
			corprob[j] = 0;
		}

		double res = 110000;
		double ex;
		for(j = A - 1; j >= 0; --j) {
			ex = corprob[j] * (A - j - 1 + B - j - 1 + 1) + (1 - corprob[j]) * (A - j - 1 + B - j - 1 + 1 + B + 1);
			res = min(res, ex);
		}

		ex = corprob[B - 1] * 1 + (1 - corprob[B - 1]) * (1 + B + 1);
		res = min(res, ex);

		cout << "Case #" << (i+1) << ": ";
		printf("%.7lf\n", res);
	}
}