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
	int T;
	string D[10001];
	int panel[10001];
	string known[10001];
	bool ended[10001];

	string L;
	int N, M;
	int i,j,k,a,b;

	cin >> T;

	REP(i,T) {
		cin >> N >> M;
		REP(j,N) {
			cin >> D[j];
		}
		cout << "Case #"<<i+1<<":";
		REP(j,M) {
			cin >> L;

			map<string, int> nums;
			map<string, bitset<26> > chs;

			memset(panel, 0x00, sizeof(panel));
			memset(ended, 0x00, sizeof(ended));
			nums.clear();
			chs.clear();

			REP(k,N) {
				string x(D[k].length(), '_');
				known[k] = x;

				++nums[known[k]];
				if (nums[known[k]] == 1) {
					bitset<26> bs;
					bs.reset();
					chs[known[k]] = bs;
				}

				REP(a, D[k].length()) {
					if (known[k][a] == '_') {
						chs[known[k]].set(D[k][a] - 'a');
					}
				}
			}

			REP(k,N) {
				if (nums[known[k]] == 1) {
					ended[k] = true;
					nums.erase(known[k]);
				}
			}

			REP(k,26) {
				char cand = L[k];
				map<string, int> newnums;
				map<string, bitset<26> > newchs;

				REP(a,N) {
					if (ended[a])
						continue;

					if (chs[known[a]].test(cand-'a')) {
						bool hit = false;
						REP(b,D[a].length()) {
							if (D[a][b] == cand) {
								known[a][b] = cand;
								hit = true;
							}
						}

						if (!hit)
							++panel[a];

						++newnums[known[a]];
						if (newnums[known[a]] == 1) {
							bitset<26> bs;
							bs.reset();
							newchs[known[a]] = bs;
						}
						REP(b, D[a].length()) {
							if (known[a][b] == '_') {
								newchs[known[a]].set(D[a][b] - 'a');
							}
						}

					} else if (newnums[known[a]] == 0) {
						newnums[known[a]] = nums[known[a]];
						newchs[known[a]] = chs[known[a]];
					}
				}

				nums = newnums;
				chs = newchs;

				REP(a,N) {
					if (!ended[a] && nums[known[a]] == 1) {
						ended[a] = true;
						nums.erase(known[a]);
					}
				}
			}

			int maxpanel = -1;
			int res = 0;
			REP(k,N) {
				if (maxpanel < panel[k]) {
					maxpanel = panel[k];
					res = k;
				}
			}

			cout << ' ' << D[res];
		}
		cout << endl;
	}
}