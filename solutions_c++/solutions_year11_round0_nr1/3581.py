/*
 * A.cpp
 *
 *  Created on: May 7, 2011
 *      Author: yassery
 */

#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

vector<pair<char, int> > v;

int getNext(char c, int ind) {
	for (int i = ind; i < v.size(); i++)
		if (v[i].first == c)
			return i;
	return -1;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
	freopen("test.txt", "wt", stdout);
#endif
	int TC, n;
	int x, y, nextB, nextO;
	char c;
	cin >> TC;
	for (int tt = 0; tt < TC; tt++) {

		v.clear();
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> c >> x;
			v.push_back(make_pair(c, x));
		}

		int curO = 1, curB = 1;
		int tot = 0;

		for (int i = 0; i < n; i++) {
			if (v[i].first == 'O') {
				x = abs(curO - v[i].second) + 1;
				curO = v[i].second;
				nextB = getNext('B', i + 1);
				if (nextB != -1) {
					y = abs(curB - v[nextB].second);
					y = min(y, x);
					if (curB > v[nextB].second)
						curB -= y;
					else
						curB += y;
				}
			} else {
				x = abs(curB - v[i].second) + 1;
				curB = v[i].second;
				nextO = getNext('O', i + 1);
				if (nextO != -1) {
					y = abs(curO - v[nextO].second);
					y = min(y, x);
					if (curO > v[nextO].second)
						curO -= y;
					else
						curO += y;
				}
			}
			tot += x;
		}
		printf("Case #%d: %d\n", tt+1, tot);
	}

	return 0;
}
