#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <queue>
#include <functional>
#include <sstream>
#include <complex>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <ctime>
#include <iomanip>
#include <time.h>

using namespace std;


#ifdef ONLINE_JUDGE
void init()
{
}
#else
FILE* inputstream;
FILE* outputstream;
void init()
{
	inputstream = freopen("in.txt", "r", stdin);
	outputstream = freopen("output.txt", "w", stdout);
}
#endif

int data[200];
int D, I, M, N;
int memo[200][300];

int go(int idx, int pre)
{
	if (idx == N)
	{
		return 0;
	}
	int& ref = memo[idx][pre];
	if (ref != -1)
	{
		return ref;
	}
	ref = 99999999;
	ref = min(ref, go(idx + 1, pre) + D);
	for (int i = 0; i <= 255; ++i)
	{
		if (M == 0 && i != pre)
		{
			continue;
		}
		int cost = abs(i - data[idx]);
		int dif = abs(i - pre);
		if (dif > M)
		{
			cost += (dif - 1) / M * I;
		}
		ref = min(ref, go(idx + 1, i) + cost);
	}
	return ref;
}

int main()
{
	init();
	int cases;
	scanf("%d", &cases);
	for (int i = 1; i <= cases; ++i)
	{
		scanf("%d %d %d %d", &D, &I, &M, &N);
		for (int j = 0; j < N; ++j)
		{
			scanf("%d", &data[j]);
		}
		memset(memo, -1, sizeof(memo));
		int best = 99999999;
		for (int j = 0; j <= 255; ++j)
		{
			best = min(best, go(0, j));
		}
		printf("Case #%d: %d\n", i, best);
	}
	return 0;
}
