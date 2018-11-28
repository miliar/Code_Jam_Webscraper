#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

//#pragma comment(linker, "/STACK:100000000")

struct Offer
{
	int x, y;
	int c;
	bool operator < (const Offer & O) const
	{
		return x < O.x;
	}
} A[320];

map<string, int> Col;

char buf[10000];

int main()
{
//	freopen("B-small.in", "r", stdin);
//	freopen("B-small.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		Col.clear();
		int N;
		scanf("%d", &N);
		int i;
		for (i = 0; i < N; ++i)
		{
			int a, b;
			scanf("%s%d%d", buf, &a, &b);
			--a;
			if (Col.find(buf) == Col.end())
			{
				int num = Col.size();
				Col[buf] = num;
			}
			A[i].x = a;
			A[i].y = b;
			A[i].c = Col[buf];
		}
		sort(A, A+N);
		int a, b, c;
		int sz = Col.size();
		int br = 1000000;
		for (a = 0; a < sz; ++a)
			for (b = a; b < sz; ++b)
				for (c = b; c < sz; ++c)
				{
					int p = 0;
					int x = 0;
					int bx = 0;
					int res = 0;
					while (x < 10000)
					{
						bx = x-1;
						while (p < N && A[p].x <= x)
						{
							if (A[p].c == a || A[p].c == b || A[p].c == c)
								bx = max(bx, A[p].y);
							++p;
						}
						if (bx > x)
						{
							++res;
							x = bx;
						}
						else
							break;
					}
					if (x >= 10000)
						br = min(br, res);
				}
		printf("Case #%d: ", t+1);
		if (br == 1000000)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", br);
		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
};
