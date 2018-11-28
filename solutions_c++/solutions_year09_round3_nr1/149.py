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

int SolveTest(int test)
{
	char buf[1 << 10];
	gets(buf);
	int len = strlen(buf);
	int B[256];
	CLEAR(B, -1);
	int i;
	int cnt = 0;
	FOR(i, 0, len)
	{
		if(B[ buf[i] ] == -1)
			++cnt;

		B[ buf[i] ] = 0;
	}

	int N = max(2, cnt);
	CLEAR(B, -1);
	Int res = 0;
	cnt = 1;
	FOR(i, 0, len)
	{
		if(B[ buf[i] ] == -1)
		{
			B[ buf[i] ] = cnt;
			if(cnt == 1)
				cnt = 0;
			else if(cnt == 0)
				cnt = 2;
			else
				++cnt;
		}

		res *= N;
		res += B[ buf[i] ];
	}

	printf("Case #%d: %lld\n", test + 1, res);
	return 0;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	char buf[1 << 10];
	gets(buf);
	int T, t;
	sscanf(buf, "%d", &T);
	FOR(t, 0, T)
		SolveTest(t);

	return 0;
};
