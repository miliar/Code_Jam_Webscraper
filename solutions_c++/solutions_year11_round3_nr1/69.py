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
	//string file = "A-small-attempt0";
	string file = "A-large";
	//freopen("test.in", "rt", stdin);
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}

void solve(int test)
{
	int n, m; scanf("%d %d ", &n, &m);
	vector<vector<char> > G(n + 1, vector<char>(m + 1, '.'));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%c ", &G[i][j]);

	bool fail = false;
	int di[] = {1, 1, 0, 0};
	int dj[] = {1, 0, 1, 0};
	char ch[] = {'/', '\\', '\\', '/'};
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (G[i][j] == '#') {
				for (int k = 0; k < 4; k++) {
					if (G[i + di[k]][j + dj[k]] != '#') {
						fail = true;
					}
					G[i + di[k]][j + dj[k]] = ch[k];
				}
			}
		}
	}
	printf("Case #%d:\n", test);
	if (fail) {
		printf("Impossible\n");
		return;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << G[i][j];
		}
		cout << endl;
	}
}

int main()
{
	openfiles();
	int n; scanf("%d ",&n); REP(i,n) solve(i + 1);
	
	return 0;
}