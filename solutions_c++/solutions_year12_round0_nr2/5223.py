/*
 * B.cpp
 *
 *  Created on: Apr 14, 2012
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
map<int, set<vector<int> > > S;
map<int, set<vector<int> > > T;
int P;
vector<int> v;

int solve(int ind, int s) {

	if (ind == v.size()){
		if(s)return -10000000;
		return 0;
	}
	set<vector<int> >::iterator it;
	int sol = 0;
	if (s) {
		it = S[v[ind]].begin();
		for (it; it != S[v[ind]].end(); it++) {
			sol = max(sol, solve(ind + 1, s - 1) + ((*it)[2] >= P));
		}
	}

	it = T[v[ind]].begin();
	for (it; it != T[v[ind]].end(); it++) {
		sol = max(sol, solve(ind + 1, s) + ((*it)[2] >= P));
	}

	return sol;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
	freopen("test.txt", "wt", stdout);
#endif

	for (int i = 0; i <= 10; i++) {
		for (int j = 0; j <= 10; j++) {
			if (abs(i - j) > 2)
				continue;
			for (int k = 0; k <= 10; k++) {
				if (abs(i - k) > 2 || abs(j - k) > 2)
					continue;

				vector<int> v;
				v.push_back(i);
				v.push_back(j);
				v.push_back(k);
				sort(v.begin(), v.end());

				if (abs(i - k) == 2 || abs(i - j) == 2 || abs(j - k) == 2)
					S[i + j + k].insert(v);
				else
					T[i + j + k].insert(v);
			}
		}
	}

	int T, N, s;
	cin >> T;
	for (int tt = 0; tt < T; tt++) {
		cin >> N >> s >> P;
		v.clear();
		v.resize(N);
		for (int i = 0; i < N; i++) {
			cin >> v[i];
		}
		cout << "Case #"<<tt+1 << ": " << solve(0, s) << endl;
	}



	return 0;
}
