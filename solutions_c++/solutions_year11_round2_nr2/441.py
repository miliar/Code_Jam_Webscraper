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

Int X[1 << 10];
Int C[1 << 10];

int SolveTest(int test)
{
	int N, D;
	scanf("%d%d", &N, &D);
	D <<= 1;
	int i;
	FOR(i, 0, N)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		X[i] = a + a;
		C[i] = b;
	}

	Int Min = -1, Max = 1LL << 44;
	while(Max - Min > 1)
	{
		Int Mid = (Max + Min) >> 1;
		Int pos = -(1LL << 60);
		FOR(i, 0, N)
		{
			pos = max(pos + D, X[i] - Mid) + (C[i] - 1)*D;
			if(pos - X[i] > Mid)
				break;
		}

		if(i == N)
			Max = Mid;
		else
			Min = Mid;
	}

	printf("Case #%d: %.7lf\n", test + 1, (Max + 0.0)/2);

	return 0;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

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
