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
	string file = "C-large";
	//freopen("test.in", "rt", stdin);
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}

void solve(int test)
{
	int n; scanf("%d ", &n);
	vector<int> v(n);
	int xr = 0, sum = 0;
	for (int i = 0; i < n; i++) {
		scanf("%d ", &v[i]);
		xr ^= v[i];
		sum += v[i];
	}

	printf("Case #%d: ", test);
	if (xr != 0) {
		printf("NO\n");
		return;
	}

	sort(v.begin(), v.end());
	printf("%d\n", sum - v[0]);
}

int main()
{
	openfiles();
	int n; scanf("%d ",&n); REP(i,n) solve(i + 1);
	
	return 0;
}