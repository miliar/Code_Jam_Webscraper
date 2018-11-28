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
	int n,a,b,c;
	int i,j,k,l;
	char comb[120][3];
	char opp[120][2];
	char wor[150];

	cin >> n;

	REP(i,n) {
		cin >> a;
		REP(j,a) {
			cin >> comb[j][0];
			while (comb[j][0] == ' ')
				cin >> comb[j][0];
			cin >> comb[j][1];
			cin >> comb[j][2];
		}

		cin >> b;
		REP(j,b) {
			cin >> opp[j][0];
			while (opp[j][0] == ' ')
				cin >> opp[j][0];
			cin >> opp[j][1];
		}

		cin >> c;
		vector<char> res;
		REP(j,c) {
			cin >> wor[j];
			while (wor[j] == ' ')
				cin >> wor[j];

			if (res.empty())
				res.push_back(wor[j]);
			else {
				char cand = res.back();
				REP(k,a) {
					if ((cand == comb[k][0] && wor[j] == comb[k][1]) ||
						(cand == comb[k][1] && wor[j] == comb[k][0])) {
						res.pop_back();
						res.push_back(comb[k][2]);
						break;
					}
				}

				if (k == a) {
					int p = res.size();
					REP(k,p) {
						REP(l,b) {
							if ((res[k] == opp[l][0] && wor[j] == opp[l][1]) ||
								(res[k] == opp[l][1] && wor[j] == opp[l][0])) {
								res.clear();
								p = res.size();
								break;
							}
						}
					}

					if (p != 0)
						res.push_back(wor[j]);
				}
			}
		}

		cout << "Case #" << i + 1 << ": [";
		REP(j, res.size()) {
			if (j != 0)
				cout << ", ";
			cout << res[j];
		}
		cout << "]" << endl;
	}
}