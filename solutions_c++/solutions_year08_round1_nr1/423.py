#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>

using namespace std;

vector<int> vecA, vecB;
int N;

int did[9];
int found;
int fmin;

void btrack(int depth)
{
	if (depth == N)
	{
		if (fmin > found)
			fmin = found;
		return;
	}

	int i;
	for (i = 0;i < N;i++)
	{
		if (did[i])
			continue;
		did[i] = true;
		found += vecA[depth] * vecB[i];
		btrack(depth + 1);
		did[i] = false;
		found -= vecA[depth] * vecB[i];
	}
}

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		scanf("%d", &N);
		int i;
		vecA.clear();
		vecB.clear();
		for (i =0 ;i < N;i++)
		{
			int p;
			scanf("%d", &p);
			vecA.push_back(p);
		}
		for (i =0 ;i < N;i++)
		{
			int p;
			scanf("%d", &p);
			vecB.push_back(p);
		}
		sort(vecA.begin(), vecA.end());
		sort(vecB.begin(), vecB.end());
		reverse(vecB.begin(), vecB.end());
		long long ans = 0;
		for (i = 0;i < N;i++)
			ans += vecA[i] * (long long)vecB[i];
		printf("Case #%d: %I64d\n", ti, ans);
/*		fmin = 0x7FFFFFFF;
		btrack(0);
		if (fmin != ans)
			printf("INCORRECT\n");*/
	}
	return 0;
}