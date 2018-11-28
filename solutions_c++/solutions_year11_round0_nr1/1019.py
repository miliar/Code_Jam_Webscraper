#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

struct press {
	string type;
	int which;
};

press s[111];

int main() {

	freopen("input.txt.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;

	for (int e=1; e<=t; e++) {
		int n; cin >> n;
		for (int u=0; u<n; u++) {
			cin >> s[u].type >> s[u].which;
		}

		map<string, int> pos;
		pos["O"] = 1;
		pos["B"] = 1;

		int sum = 0;
		for (int i=0; i<n; i++) {

			while (true) {
				++sum;
				int nxtb = -1;
				string tt;
				for (int u=i+1; u<n; u++) {
					if (s[u].type != s[i].type) {
						nxtb = u;
						tt = s[u].type;
						break;
					}
				}

				if (nxtb != -1) {
					if (pos[tt] < s[nxtb].which)
						++pos[tt];
					else if (pos[tt] > s[nxtb].which)
						--pos[tt];
				}


				if (pos[s[i].type] == s[i].which) {
					break;
				}

				if (pos[s[i].type] < s[i].which)
					pos[s[i].type]++;
				else
					--pos[s[i].type];

			}
		}

		printf("Case #%d: %d\n", e, sum);
	}

	return 0;
}