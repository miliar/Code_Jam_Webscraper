/*
 * Main.cpp
 *
 *  Created on: 2009-9-27
 *      Author: delguoqing
 */

#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define MAXN	100
#define MAXK	25

bool map[MAXN][MAXN];
int price[MAXN][MAXK];
int n, k;

void printVec(vector<int> &v)
{
	for(vector<int>::iterator it = v.begin(); it != v.end(); ++ it)
		printf("%d ", *it);
	printf("\n");
}

bool check(int x, int y) {
	int flag;

	if(price[x][0] < price[y][0] && price[x][1] < price[y][1])
		flag = -1;
	else if(price[x][0] > price[y][0] && price[x][1] > price[y][1])
		flag = 1;
	else
		return false;
	for(int i = 0; i < k - 1; ++ i)
		if(flag == -1 && (price[x][i] < price[y][i] && price[x][i + 1] < price[y][i + 1]))
			continue;
		else if(flag == 1 && price[x][i] > price[y][i] && price[x][i + 1] > price[y][i + 1])
			continue;
		else
			return false;
	return true;
}

vector<int> data[MAXN];
int minSet;

bool can(int i, int j) {
	for(vector<int>::iterator it = data[j].begin();
			it != data[j].end(); ++ it)
		if(! map[i][*it])
			return false;
	return true;
}

void dfs(int i, int j) {
	if(i == n) {
		minSet = min(minSet, j);

		return;
	}

	for(int m = 0; m < j; ++ m) {
		if(can(i, m)) {
			data[m].push_back(i);

			dfs(i + 1, j);

			data[m].pop_back();
		}
	}

	if(j + 1 < minSet) {
		data[j].push_back(i);

		dfs(i + 1, j + 1);

		data[j].pop_back();
	}

	return;
}


int main() {
	int cases;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d", &cases);
	for(int caseId = 1; caseId <= cases; ++ caseId) {
		printf("Case #%d: ", caseId);

		scanf("%d %d", &n, &k);
		for(int i = 0; i < n; ++ i)
			for(int j = 0; j < k; ++ j)
				scanf("%d", &price[i][j]);

		memset(map, false, sizeof(map));

		for(int i = 0; i < n; ++ i)
			for(int j = i + 1; j < n; ++ j)
				map[i][j] = map[j][i] = check(i, j);

		minSet = 0x7fffffff;
		dfs(0, 0);
		printf("%d\n", minSet);
	}
}
