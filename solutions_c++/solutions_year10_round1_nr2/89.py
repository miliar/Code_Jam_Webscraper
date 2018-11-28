#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <climits>
#include <sstream>
#include <cstring>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#include <map>
#include <set>

#define INF (INT_MAX/3)
#define MAXN 128

typedef long long lint;

using namespace std;

int div(int a, int maxdist, int inscost)
{
	if (maxdist == 0) {
		if (a == 0)
			return 0;
		return INF;
	}

	int ret = 0;
	
	while (a > maxdist) {
		ret ++;
		a -= maxdist;
	}

	return ret * inscost;
}

int pd[MAXN][256];
int solve(vector <int>& list, int delcost, int inscost, int maxdist)
{
	int ret = INF;
	
	for (int i = 0; i < list.size(); i++)
		for (int j = 0; j < 256; j++)
			pd[i][j] = INF;
	memset(pd[list.size()], 0, sizeof(pd[list.size()]));

	for (int i = list.size()-1; i >= 0; i--)
		for (int j = 0; j < 256; j++)
			for (int k = 0; k < 256; k++) {
				if (abs(k - j) <= maxdist)
					pd[i][j] = min(pd[i][j], abs(k-list[i]) + pd[i+1][k]);
				pd[i][j] = min(pd[i][j], abs(k-list[i]) + delcost + pd[i+1][j]);
				pd[i][j] = min(pd[i][j], abs(k-list[i]) + div((abs(k - j)),maxdist, inscost) + pd[i+1][k]);
			}

	for (int j = 0; j < 256; j++)
		ret = min(ret, pd[0][j]);

	return ret;
} 

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int delcost, inscost, maxdist, size;
		vector <int> list;

		scanf("%d %d %d %d", &delcost, &inscost, &maxdist, &size);
		
		for (int i = 0; i < size; i++) {
			int x;
			scanf("%d", &x);
			list.push_back(x);
		}

		printf("Case #%d: %d\n", t+1, solve(list, delcost, inscost, maxdist));
	}

	return 0;
}
