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

int g[1000];
long long tot;
int next[1000];
int peo[1000];

int main()
{
	init();
	int a, b;
	int cases;
	scanf("%d", &cases);
	for (int i = 1; i <= cases; ++i)
	{
		printf("Case #%d: ", i);
		int R, K, N;
		scanf("%d %d %d", &R, &K, &N);
		tot = 0;
		for (int j = 0; j < N; ++j)
		{
			scanf("%d", &g[j]);
			tot += g[j];
		}
		if (tot <= K)
		{
			printf("%I64d\n", tot * R);
		}
		else
		{
			memset(next, -1, sizeof(next));
			memset(peo, -1, sizeof(peo));
			for (int j = 0; j < N; ++j)
			{
				int tmp = g[j];
				next[j] = (j + 1) % N;
				for (int k = (j + 1) % N; tmp + g[k] <= K; k = (k + 1) % N)
				{
					tmp += g[k];
					next[j] = (k + 1) % N;
				}
				peo[j] = tmp;
			}
			long long result = 0;
			int ind = 0;
			for (int j = 0; j < R; ++j)
			{
				result += peo[ind];
				ind = next[ind];
			}
			printf("%I64d\n", result);
		}
	}
	return 0;
}
