
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#ifdef _DEBUG
#define DBG printf
#else
#define DBG if(0) 
#endif

int A [1002];
int c[1002];
int n;

int stupidadd(int x, int y)
{
	int result = 0; 
	for(int i=0;i<32; ++i)
	{
		int a = (x >> i) & 0x1  ; 
		int b = (y >> i) & 0x01; 
		int c = (a & ~b) |  ( b & ~a);
		result = result | (c << i);
	}
	return result; 
}

void tobin(int x)
{
	for(int i=1;i<=n;++i)
	{
		c[i] = 0; 
		if ( x & ( 1 << (i-1) ))
		{
			c[i] = 1; 
		}
	}
}

int solve()
{
	bool found = false;
	int max = -1; 
	// try 2^n cases 
	for (int i=1; i < (1  << n) - 1; ++i)
	{
		tobin(i);
		int s0, s1, r0, r1; 
		s0=s1=r0=r1=0;
		for(int j=1; j<=n;++j)
		{
			if (c[j]) 
			{
				s1 = stupidadd(s1, A[j]);
				r1 = r1 + A[j];
			}
			else
			{
				s0 = stupidadd(s0, A[j]);
				r0 = r0 + A[j];
			}

		}
		if (s0 == s1)
		{
			found = true; 
			if (r0 > max)
				max = r0; 
			if (r1 > max) 
				max = r1; 
		}
	}
	return max; 
}

void init()
{
	for(int i=0;i<=1001;++i)
		A[i] = c[i] = 0;
}

int main()
{
	int ntc; 
	scanf("%d", &ntc);
	for(int tci = 1; tci <= ntc; ++tci)
	{
		init();
		scanf("%d", &n);
		for(int i=1;i<=n;++i)
			scanf("%d", A+i);
		int x = solve();
		if (x == -1)
			printf("Case #%d: NO\n", tci);
		else
			printf("Case #%d: %d\n", tci, x);
	}
	return 0; 
}