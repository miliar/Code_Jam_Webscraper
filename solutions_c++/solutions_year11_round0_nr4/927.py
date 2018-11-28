#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <vector>
#include <map>
#include <string>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)

void openfiles()
{
#ifndef ONLINE_JUDGE
	string file = "D-large";
	//freopen("test.in", "rt", stdin);
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}


void montecarlo() {
	
	vector<int> v;
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	v.push_back(0);
	v.push_back(5);
	v.push_back(4);
	int n = v.size();
	int tries = 100000;
	int sum = 0;
	for (int i = 0; i < tries; i++) {
		if (i % 10000 == 0) cout << i << endl;
		vector<int> w = v; int j = 0;
		for (j = 0; ; j++) {
			int m = 0;
			vector<int> shuf;
			for (int k = 0; k < n; k++) {
				if (w[k] == k) m++;
				else shuf.push_back(w[k]);
			}
			if (m == n) break;
			for (int k = 0; k < n; k++) if (w[k] != k) {
				int p = rand() % shuf.size();
				w[k] = shuf[p];
				shuf.erase(shuf.begin() + p);
			}
		}
		sum += j;
	}
	cout << sum << "/" << tries << " = " << (double)sum/tries << endl;
}

void docycles() {
	int n = 4;
	vector<int> v(n);
	map<vector<int>, int> cycles;
	REP(i,n) v[i] = i;
	do {
		bool vis[10] = {0};
		int sum = 1;
		vector<int> cycle;
		for (int i = 0; i < n; i++) {
			if (vis[i] == true) continue;
			int cur = 1;
			vis[i] = true;
			for (int j = v[i]; j != i; j = v[j]) {
				vis[j] = true;
				cur++;
			}
			cycle.push_back(cur);
		}
		sort(cycle.begin(), cycle.end());
		cycles[cycle]++;
	} while (next_permutation(v.begin(), v.end()));
	for (map<vector<int>, int>::iterator ii = cycles.begin(); ii != cycles.end(); ++ii) {
		const vector<int>& w = ii->first;
		for (int i = 0; i < w.size(); i++) {
			cout << w[i] << " ";
		}
		cout << ": ";
		cout << ii->second << endl;
	}

}

void solve(int test)
{
	int n; scanf("%d ", &n);
	int out = 0;
	for (int i = 0; i < n; i++) {
		int a; scanf("%d ", &a);
		if (a != i + 1) out++;
	}
	printf("Case #%d: %d.000000\n", test, out);
}

int main()
{
	openfiles();
	int m; scanf("%d ",&m); REP(i,m) solve(i + 1);
	
	return 0;
}