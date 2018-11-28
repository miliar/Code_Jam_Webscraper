/*
 * A. Diamond Inheritance.cpp
 *
 *  Created on: May 6, 2012
 *      Author: ahmed
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
/*#include <hash_map>
using namespace __gnu_cxx;*/
typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > adjL;
int oo = (int) 1e9;
adjL adj;
int src;
int vis[1009];
int isD(int idx) {
	vis[idx] = src;
	for (int i = 0; i < (int)adj[idx].size(); ++i) {
		if(vis[adj[idx][i]] ==  src)
			return 1;
		if(isD(adj[idx][i]))
			return 1;
	}
	return 0;
}
int main()
{
		freopen("A-large.in", "rt", stdin);
		freopen("b.txt", "wt", stdout);
	int t, n, m, to;
	scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii) {
		printf("Case #%d: ", ii+1);
		memset(vis, -1, sizeof vis);
		scanf("%d", &n);
		adj = adjL(n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &m);
			for (int j = 0; j < m; ++j) {
				scanf("%d", &to);
				--to;
				adj[i].pb(to);
			}
		}
		for (int i = 0; i < n; ++i) {
			src = i;
			if(isD(i)) {
				printf("Yes\n");
				goto out;
			}
		}
		printf("No\n");
		out:;

	}

	return 0;
}

/*
3
3
1 2
1 3
0
5
2 2 3
1 4
1 5
1 5
0
3
2 2 3
1 3
0
 */
