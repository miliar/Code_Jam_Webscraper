
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

using namespace std;

vector<vector<int> > graph;
int src;
int isvis[1010];
int isDiamond(int idx) {
	isvis[idx] = src;
	for (int i = 0; i < (int)graph[idx].size(); ++i)
		if(isvis[graph[idx][i]] ==  src || isDiamond(graph[idx][i]))
			return 1;
	return 0;
}
int main()
{
		freopen("A-large.in", "rt", stdin);
		freopen("a.txt", "wt", stdout);
	int t, n, m, to;
	scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii) {
		printf("Case #%d: ", ii+1);
		memset(isvis, -1, sizeof isvis);
		scanf("%d", &n);
		graph = vector<vector<int> >(n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &m);
			for (int j = 0; j < m; ++j) {
				scanf("%d", &to);
				--to;
				graph[i].push_back(to);
			}
		}
		int flg = 0;
		for (int i = 0; i < n; ++i) {
			src = i;
			if(isDiamond(i)) {
				printf("Yes\n");
				flg = 1;
				break;
			}
		}
		if(!flg)
			printf("No\n");
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
