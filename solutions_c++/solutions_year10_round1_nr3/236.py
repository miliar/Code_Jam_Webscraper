#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define REP(i,n) for (int i = 0; i < (n); ++i)
#define FORE(i,c) for (typeof(c.begin()) i = c.begin(); i != c.end(); ++i)
using namespace std;

int T;
int lho[1000001];
int A1, A2, B1, B2;


bool f(int a, int b)
{
	if (b*2 <= a) return true;
	return lho[b] < a-b;
}

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin), freopen("C-small2.out", "w", stdout);
	freopen("C-large.in", "r", stdin), freopen("C-large.out", "w", stdout);
	
	for (int i = 1; i <= 1000000; i++)
	{
		int lo = 0, hi = i;
		while (lo < hi)
		{
			int mid = (lo+hi+1)/2;
			if (f(i, mid))
				lo = mid;
			else
				hi = mid-1;
		}
		lho[i] = lo;
	}
	scanf("%d", &T);
	REP(t, T)
	{
		scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
		long long res = 0;
		for (int a = A1; a <= A2; a++)
		{
			long long l = max(0, B1);
			long long r = min(lho[a], B2);
			if (l <= r)
			{
				res += r-l+1;
			}
		}
		for (int a = B1; a <= B2; a++)
		{
			long long l = max(0, A1);
			long long r = min(lho[a], A2);
			if (l <= r)
			{
				res += r-l+1;
			}
		}
		printf("Case #%d: %lld\n", t+1, res);
	}
}
