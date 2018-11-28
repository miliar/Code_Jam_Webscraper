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
	int x, s, r, t, n;
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);

	int i;

	vector<PII> v;
	FOR(i, 0, n)
	{
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);

		v.PB(PII(c, b - a));
		x -= b - a;
	}

	v.PB(PII(0, x));
	sort(ALL(v));

	double timeLeft = t;
	double res = 0;
	FOR(i, 0, SIZE(v))
	{
		double time = min((v[i].second + 0.0)/(v[i].first + r), timeLeft);
		res += (v[i].second - time*(v[i].first + r))/(v[i].first + s);
		res += time;
		timeLeft -= time;
	}

	printf("Case #%d: %.7lf\n", test + 1, res);
	return 0;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

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
