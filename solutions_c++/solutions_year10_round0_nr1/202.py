#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <cmath>

#include <cstdarg>

#pragma comment(linker,"/STACK:128000000")

#define DBG1
#define DBG2 1

void dbg(const char * fmt, ...)
{
#ifdef DBG1
#if DBG2
	va_list args;
	va_start(args, fmt);
	vfprintf(stderr, fmt, args);
	va_end(args);

	fflush(stderr);
#endif
#endif
}

using namespace std;

#define clr(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))

#define TASKNAME ""

typedef long long ll;
typedef unsigned long long ull;

typedef pair<int,int> pii;


int main()
{
#ifdef DBG1
#if DBG2
//	freopen(TASKNAME ".in", "r", stdin);
	freopen(TASKNAME ".out", "w", stdout);
	freopen(TASKNAME ".err", "w", stderr);
#endif
#endif

	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		printf("Case #%d: ", ii);
		int n, k;
		scanf("%d%d", &n, &k);
		int p = (1 << n);
		if (k % p == p - 1)
			printf("ON\n");
		else
			printf("OFF\n");
	}

	return 0;
}