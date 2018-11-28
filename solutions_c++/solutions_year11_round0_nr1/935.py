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
	string file = "A-large";
	//freopen("test.in", "rt", stdin);
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}

int moveto(int cur, int allowed, int target) {
	if (abs(cur - target) <= allowed) return target;
	if (cur < target) return cur + allowed;
	return cur - allowed;
}

void solve(int test)
{
	int n; scanf("%d ", &n);
	vector<int> blue, orange;
	vector<pair<int, char> > locs;
	for (int i = 0; i < n; i++) {
		int a; char c;
		scanf("%c %d ", &c, &a);
		if (c == 'O') orange.push_back(a);
		if (c == 'B') blue.push_back(a);
		locs.push_back(make_pair(a, c));
	}

	int posblue = 1, posorange = 1;
	int ii = 0, jj = 0;
	int t = 0;
	for (int i = 0; i < n; i++) {
		if (locs[i].second == 'O') {
			int d = abs(locs[i].first - posorange) + 1; // move and press
			t += d; jj++;
			if (ii < blue.size()) posblue = moveto(posblue, d, blue[ii]);
			posorange = locs[i].first;
		}
		else if (locs[i].second == 'B') {
			int d = abs(locs[i].first - posblue) + 1; // move and press
			t += d; ii++;
			if (jj < orange.size()) posorange = moveto(posorange, d, orange[jj]);
			posblue = locs[i].first;
		}
	}
	printf("Case #%d: %d\n", test, t);
}

int main()
{
	openfiles();
	int n; scanf("%d ",&n); REP(i,n) solve(i + 1);
	
	return 0;
}