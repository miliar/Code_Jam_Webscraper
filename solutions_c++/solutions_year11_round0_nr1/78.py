#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

void move(int &x, int y)
{
	if (y > x) ++x;
	else if (y < x) --x;
}

int run()
{
	vector<pair<int, int> > vp[2];
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		char s[10];
		int x;
		scanf("%s %d", s, &x);
		if (s[0] == 'O') {
			vp[0].push_back(make_pair(x, i));
		}
		else {
			vp[1].push_back(make_pair(x, i));
		}
	}
	int t = 0;
	for (int i = 0, j = 0, x = 1, y = 1; i < sz(vp[0]) || j < sz(vp[1]); ++t) {
		if (i < sz(vp[0]) && j < sz(vp[1])) {
			if (vp[0][i].second < vp[1][j].second) {
				if (x == vp[0][i].first) {
					++i;
				}
				else {
					move(x, vp[0][i].first);
				}
				move(y, vp[1][j].first);
			}
			else {
				if (y == vp[1][j].first) {
					++j;
				}
				else {
					move(y, vp[1][j].first);
				}
				move(x, vp[0][i].first);
			}
		}
		else if (i < sz(vp[0])) {
			if (x == vp[0][i].first) {
				++i;
			}
			else {
				move(x, vp[0][i].first);
			}
		}
		else {
			if (y == vp[1][j].first) {
				++j;
			}
			else {
				move(y, vp[1][j].first);
			}
		}
	}
	return t;
}

int main()
{
	freopen("A0.in", "r", stdin);
	freopen("A0.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, run());
	}
	return 0;
}