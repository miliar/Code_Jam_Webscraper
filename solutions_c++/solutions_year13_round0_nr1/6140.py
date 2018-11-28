/*
 * A.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Marwan
 */

#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstring>
#include <sstream>
#include <complex>
#include <iomanip>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <climits>
#include <set>
#include <map>

using namespace std;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;
#define MP make_pair
#define SZ(x) (int)x.size()

int dcmp(double a, double b) {
	return (fabs(a - b) <= eps) ? 0 : ((a < b) ? -1 : 1);
}

typedef long long ll;
typedef pair<int, int> pii;

int di[] = { 0, 1, 1, 1 };
int dj[] = { 1, 1, 0, -1 };
vector<string> vs(4);

bool valid(int i, int j, char c) {
	return i >= 0 && i < 4 && j >= 0 && j < 4
			&& (vs[i][j] == c || vs[i][j] == 'T');
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
//	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);
#endif
	int T;
	cin >> T;
	for (int tt = 0; tt < T; tt++) {
		cout << "Case #" << tt + 1 << ": ";
		for (int i = 0; i < 4; i++)
			cin >> vs[i];

		bool dot = false;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {

				if (vs[i][j] == '.' || vs[i][j] == 'T') {
					dot |= vs[i][j] == '.';
					continue;
				}

				for (int k = 0; k < 4; k++) {
					int cnt = 0;
					for (int d = 0; d < 4; d++)
						cnt += valid(i + di[k] * d, j + dj[k] * d, vs[i][j]);

					if (cnt == 4) {
						cout << vs[i][j] << " won" << endl;
						goto EndCase;
					}
				}
			}
		}

		if (dot)
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;

		EndCase: ;
	}
	return 0;
}
