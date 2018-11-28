#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <set>
using namespace std;
#define FOR(i, n) for (int i = 0; i < (int) (n); i++)

typedef set<pair<int, int> > SII;
typedef set<pair<int, int> >::iterator itSII;

int solve(void)
{
	set<pair<int, int> > ss;
	int r, x1, y1, x2, y2;
	scanf("%d", &r);
	while (r--) {
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int y = y1; y <= y2; y++)
			for (int x = x1; x <= x2; x++)
				ss.insert(make_pair(x, y));
	}
	int T = 0;
	while (ss.size()) {
		T++;
		set<pair<int, int> > news;
		for (itSII it = ss.begin(); it != ss.end(); ++it) {
			int x = it->first;
			int y = it->second;
			if (ss.find(make_pair(x-1, y)) != ss.end() || ss.find(make_pair(x, y - 1)) != ss.end())
				news.insert(make_pair(x, y));
			if (ss.find(make_pair(x + 1, y - 1)) != ss.end())
				news.insert(make_pair(x+1, y));
		}
		ss = news;
	}
	return T;
}

int main(void)
{
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: %d\n", tc, solve());
	}
	return 0;
}
