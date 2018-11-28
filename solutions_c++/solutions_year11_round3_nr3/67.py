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
	string file = "C-small-attempt0";
	//string file = "C-large";
	//freopen("test.in", "rt", stdin);
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}

void solve(int test)
{
	int n, a, b;
	scanf("%d %d %d ", &n, &a, &b);

	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);

	printf("Case #%d: ", test);
	for (int i = a; i <= b; i++) {
		bool ok = true;
		for (int j = 0; j < n && ok; j++) {
			if (v[j] % i == 0 || i % v[j] == 0) continue;
			ok = false;
		}
		if (ok) {
			printf("%d\n", i);
			return;
		}
	}
	printf("NO\n");
}

int main()
{
	openfiles();
	int n; scanf("%d ",&n); REP(i,n) solve(i + 1);
	
	return 0;
}