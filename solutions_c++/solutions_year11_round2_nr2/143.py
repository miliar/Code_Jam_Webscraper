#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cctype>
#include <memory>
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
typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef pair<int,int> PII;

#define FOR(i,n,m) for(i=(n); i<(m); ++i)
#define RFOR(i,n,m) for(i=(n)-1; i>=(m); --i)
#define CLEAR(x,y) memset((x), (y), sizeof(x))
#define COPY(x,y) memcpy((x),(y),sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

int N;
Int P[1100000];
Int D;

inline Int abs(Int x)
{
	if (x < 0)
		return -x;
	return x;
}

bool good(Int time)
{
	Int st = -100000000000000LL;
	for (int i = 0; i < N; ++i)
	{
		Int np = st + D;
		if (np < P[i] - time)
			np = P[i] - time;
		else
		{
			if (abs(np - P[i]) > time)
				return false;
		}
		st = np;
	}
	return true;
}

int main()
{
//	freopen("-small.in", "r", stdin);
//	freopen("-small.out", "w", stdout);
//	freopen("-large.in", "r", stdin);
//	freopen("-large.out", "w", stdout);

	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int C, d;
		N = 0;
		scanf("%d%d", &C, &d);
		D = d*2;
		for (int i = 0; i < C; ++i)
		{
			int p, v;
			scanf("%d%d", &p, &v);
			while (v--)
			{
				P[N++] = p*2;
			}
		}
		Int ub, lb, cb;
		ub = 20000000000000LL;
		lb = -1;
		while (ub - lb > 1)
		{
			cb = ((ub+lb) >> 1);
			if (good(cb))
				ub = cb;
			else
				lb = cb;
		}
		printf("Case #%d: %.10lf\n", t+1, (double)ub / 2.0);

		fprintf(stderr, "%d/%d\n", t+1, T);
	}

	return 0;
}