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
#include <cstring>
using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

typedef long long ll;
typedef long double ld;

int main() {
#ifndef ONLINE_JUDGE
//	freopen("Qual/A-small-attempt0.in", "rt", stdin);
//	freopen("A.out","wt",stdout);
	freopen("Qual/A-large.in", "rt", stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int n;
	cin >> n;
	for (int tt = 0; tt < n; ++tt) {
		cout << "Case #" << tt + 1 << ": ";
		vector<string> all(4);
		for (int i = 0; i < 4; ++i) {
			cin >> all[i];
		}
		bool hasD = 0;
		string s = ".XOT";
		int row = 3, col = 3;
		for (int i = 0; i < 4; ++i) {
			row = 3;
			col = 3;
			for (int j = 0; j < 4; ++j) {
				hasD |= (all[i][j] == '.');
				row &= s.find(all[i][j]);
				col &= s.find(all[j][i]);
			}
			row = max(row, col);
			if (row & 1)
				goto winX;
			if (row & 2)
				goto winO;
		}
		row = 3;
		col = 3;
		for (int j = 0; j < 4; ++j) {
			row &= s.find(all[j][j]);
			col &= s.find(all[j][3 - j]);
		}
		row = max(row, col);
		if (row & 1)
			goto winX;
		if (row & 2)
			goto winO;

		if (hasD)
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;
		continue;

		winO: cout << "O won" << endl;
		continue;

		winX: cout << "X won" << endl;
		continue;
	}
	return 0;
}
