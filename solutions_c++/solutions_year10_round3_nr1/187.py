#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <algorithm>
#include <cassert>
#include <memory.h>

using namespace std;

#define pb push_back
#define mp make_pair
typedef long long lint;
const int INF = 2000000000;

int n;
pair<int, int> f[1005];
bool solve(int case_num)
{
	int ans = 0;

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d%d", &f[i].first, &f[i].second);

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (i != j)
			{
				bool ok1 = f[i].first > f[j].first;
				bool ok2 = f[i].second > f[j].second;
				if ((ok1 && !ok2) || (!ok1 && ok2))
					ans++;
			}

	printf("Case #%d: ", case_num);
	//answer
	printf("%d", ans / 2);
	//======
	printf("\n");
	return true;
}

int main()
{
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
	int tn;
	scanf("%d", &tn);
	for (int i = 0; i < tn; i++)
		solve(i + 1);
	return 0;
}