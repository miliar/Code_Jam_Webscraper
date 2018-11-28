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

typedef long long Int;
typedef pair<int,int> PII;
typedef vector<int> VInt;

#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair

int P[1 << 20];

Int F(Int n)
{
	if(n == 1)
		return 0;

	CLEAR(P, -1);
	Int res = 1;
	Int i, j;
	for(i = 2; i*i <= n; ++i)
	{
		if(P[i] == 0)
			continue;

		for(j = i + i; j < (1 << 20); j += i)
			P[j] = 0;

		Int t = i*i;
		while(t <= n)
		{
			++res;
			t *= i;
		}
	}

	return res;
}

int SolveTest(int test)
{
	Int n;
	scanf("%lld", &n);
	printf("Case #%d: %lld\n", test + 1, F(n));
	return 0;
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	int T, t;
	char buf[1 << 7];
	gets(buf);
	sscanf(buf, "%d", &T);
	FOR(t, 0, T)
	{
		fprintf(stderr, "Solving %d/%d\n", t + 1, T);
		SolveTest(t);
	}

	return 0;
};
