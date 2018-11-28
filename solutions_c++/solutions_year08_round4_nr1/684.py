
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) for(int i = 0; i < N; ++i)
#define RREP(i, N) for(int i = N - 1; i >= 0; --i)

#define ABS(N) (((N) < 0) ? (-(N)) : (N))
#define MIN(A, B) (((A) < (B)) ? (A) : (B))
#define MAX(A, B) (((A) > (B)) ? (A) : (B))
#define EPS 1e-7
#define ALL(V) V.begin(), V.end()
#define pb push_back
#define mp make_pair
#define Pi 3.14159265358979323846
#define SIZE(V) V.size()


typedef vector <int> VI;
typedef pair <int, int> PI;
typedef long long Long;
typedef unsigned int Uint;
typedef unsigned long long ULong;
typedef unsigned char Uchar;

struct st
{
	int res0;
	int res1;
	int isOr;
	int isCh;
};

st A[15][1 << 14];

int N;
int M;
int V;

void solve()
{
	scanf("%d%d", &M, &V);
	int c;
	int g;
	int level = 0;
	int cur = 0;
	int l1;
	int cur1;
	REP(i, (M - 1)/2)
	{
		scanf("%d%d", &g, &c);
		A[level][cur].isOr = 1 - g;
		A[level][cur].isCh = c;
		l1 = level;
		cur1 = cur;
		if(cur == (1 << level) - 1)
		{
			cur = 0;
			++level;
		}
		else
			++cur;
	}
	REP(i, (M + 1)/2)
	{
		scanf("%d", &c);
		if(c)
		{
			A[level][cur].res1 = 0;
			A[level][cur].res0 = -1;
		}
		else
		{
			A[level][cur].res1 = -1;
			A[level][cur].res0 = 0;
		}
		if(cur == (1 << level) - 1)
		{
			cur = 0;
			++level;
		}
		else
			++cur;
	}
	while(true)
	{
		A[l1][cur1].res0 = -1;
		A[l1][cur1].res1 = -1;
		int a0 = A[l1 + 1][cur1*2].res0;
		int a1 = A[l1 + 1][cur1*2].res1;
		int b0 = A[l1 + 1][cur1*2 + 1].res0;
		int b1 = A[l1 + 1][cur1*2 + 1].res1;
		int c0 = -1;
		int c1 = -1;
		if(A[l1][cur1].isOr)
		{
			if(a0 != -1 && b0 != -1)
			{
				if(c0 == -1 || c0 > a0 + b0)
					c0 = a0 + b0;
			}
			if(a1 != -1 || b1 != -1)
			{
				if(a1 != -1 && b1 != -1)
				{
					if(c1 == -1 || c1 > MIN(a1, b1))
						c1 = MIN(a1, b1);
				}
				else if(a1 != -1)
				{
					if(c1 == -1 || c1 > a1)
						c1 = a1;
				}
				else
				{
					if(c1 == -1 || c1 > b1)
						c1 = b1;
				}
			}
		}
		if(!A[l1][cur1].isOr)
		{
			if(a1 != -1 && b1 != -1)
			{
				if(c1 == -1 || c1 > a1 + b1)
					c1 = a1 + b1;
			}
			if(a0 != -1 || b0 != -1)
			{
				if(a0 != -1 && b0 != -1)
				{
					if(c0 == -1 || c0 > MIN(a0, b0))
						c0 = MIN(a0, b0);
				}
				else if(a0 != -1)
				{
					if(c0 == -1 || c0 > a0)
						c0 = a0;
				}
				else
				{
					if(c0 == -1 || c0 > b0)
						c0 = b0;
				}
			}
		}

		//
		if(!A[l1][cur1].isOr && A[l1][cur1].isCh)
		{
			if(a0 != -1 && b0 != -1)
			{
				if(c0 == -1 || c0 > a0 + b0 + 1)
					c0 = a0 + b0 + 1;
			}
			if(a1 != -1 || b1 != -1)
			{
				if(a1 != -1 && b1 != -1)
				{
					if(c1 == -1 || c1 > MIN(a1, b1) + 1)
						c1 = MIN(a1, b1) + 1;
				}
				else if(a1 != -1)
				{
					if(c1 == -1 || c1 > a1 + 1)
						c1 = a1 + 1;
				}
				else
				{
					if(c1 == -1 || c1 > b1 + 1)
						c1 = b1 + 1;
				}
			}
		}
		if(A[l1][cur1].isOr && A[l1][cur1].isCh)
		{
			if(a1 != -1 && b1 != -1)
			{
				if(c1 == -1 || c1 > a1 + b1 + 1)
					c1 = a1 + b1 + 1;
			}
			if(a0 != -1 || b0 != -1)
			{
				if(a0 != -1 && b0 != -1)
				{
					if(c0 == -1 || c0 > MIN(a0, b0) + 1)
						c0 = MIN(a0, b0) + 1;
				}
				else if(a0 != -1)
				{
					if(c0 == -1 || c0 > a0 + 1)
						c0 = a0 + 1;
				}
				else
				{
					if(c0 == -1 || c0 > b0 + 1)
						c0 = b0 + 1;
				}
			}
		}
		//
		A[l1][cur1].res0 = c0;
		A[l1][cur1].res1 = c1;
		if(l1 == 0 && cur1 == 0)
			break;
		if(cur1 == 0)
		{
			--l1;
			cur1 = (1 << l1) - 1;
		}
		else
			--cur1;
	}
	int res;
	if(V == 0)
		res = A[0][0].res0;
	else
		res = A[0][0].res1;
	if(res == -1)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", res);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &N);
	REP(i, N)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}