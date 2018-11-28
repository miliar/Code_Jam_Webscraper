#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#define INF (2000000000)

int p[2][2];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	for(int tt = 0; tt < t; ++tt)
	{
		int n;
		scanf("%d", &n);
		p[0][0] = p[1][0] = 0;
		p[0][1] = p[1][1] = 1;
		int time = 0;
		char c;
		int ps;
		for(int i = 0; i < n; ++i)
		{
			cin >> c >> ps;
			int ind = c == 'O' ? 0 : 1;
			p[ind][0] = time = max(p[ind][0] + abs(ps - p[ind][1]), time) + 1;
			p[ind][1] = ps;
		}
		printf("Case #%d: %d\n", tt + 1, time);
	}
	return 0;
}