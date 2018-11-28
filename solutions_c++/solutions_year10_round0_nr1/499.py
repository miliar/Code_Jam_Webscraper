#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#define INF (2000000000)

const int nmax = 50;

int a[nmax];

void solveTest()
{
	int n, k;
	scanf("%d%d", &n, &k);
	int i;
	for(i = 0; i < n; ++i)
	{
		a[i] = k & 1;
		k >>= 1;
	}
	for(i = 0; i < n; ++i)
	{
		if (!a[i])
		{
			printf("OFF\n");
			return;
		}
	}
	printf("ON\n");
}

int main()
{
	int t;
	int i;
	freopen("A.txt", "r", stdin);
	freopen("A_out_large.txt", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		solveTest();
	}
	return 0;
}
