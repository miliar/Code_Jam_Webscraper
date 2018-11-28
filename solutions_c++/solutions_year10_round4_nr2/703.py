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

int M[1024];
int money[10][512];
long long memo[10][512][10];

long long go(int level, int pos, int still)
{
	if (level < 0)
	{
		if (still < M[pos])
		{
			return (1LL << 50);
		}
		return 0;
	}
	long long& ref = memo[level][pos][still];
	if (ref != -1)
	{
		return ref;
	}
	ref = (1LL << 50);
	int pos1 = pos * 2;
	int pos2 = pos * 2 + 1;
	for (int j = 0; j <= still + 1; ++j)
	{
		for (int k = 0; k <= still + 1; ++k)
		{
			ref = min(ref, go(level -1, pos1, j) + go(level - 1, pos2, k) + money[level][pos]);
		}
	}
	for (int j = 0; j <= still; ++j)
	{
		for (int k = 0; k <= still; ++k)
		{
			ref = min(ref, go(level -1, pos1, j) + go(level - 1, pos2, k));
		}
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
		int P;
		scanf("%d", &P);
		for (int j = 0; j < (1 << P); ++j)
		{
			scanf("%d", &M[j]);
			M[j] = P - M[j];
		}
		int base = (1 << (P - 1));
		for (int j = 0; j < P; ++j)
		{
			for (int k = 0; k < base; ++k)
			{
				scanf("%d", &money[j][k]);
			}
			base /= 2;
		}
		memset(memo, -1, sizeof(memo));
		printf("Case #%d: %I64d\n", i, go(P-1, 0, 0));
	}
	return 0;
}
