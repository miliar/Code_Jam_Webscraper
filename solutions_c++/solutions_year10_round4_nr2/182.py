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

Int INF = (1LL<<60);

int K[1<<10];
int P[1<<11];
Int R[11][1<<11];
int N;

Int F(int p, int k)
{
	if (k > 10)
		return INF;
	if (p >= (1<<N))
	{
		if (K[p - (1<<N)] >= k)
			return 0;
		return INF;
	}
	Int& res = R[k][p];
	if (res != -1)
		return res;
	res = F((p << 1), k+1) + F((p << 1) + 1, k+1);
	Int r2 = F((p << 1), k) + F((p << 1) + 1, k) + P[p];
	res = min(res, r2);
	res = min(res, INF);
	return res;
}

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
		CLEAR(R, -1);
		scanf("%d", &N);
		for (int i = 0; i < (1<<N); ++i)
			scanf("%d", &K[i]);
		for (int i = N-1; i >= 0; --i)
		{
			int k = (1<<i);
			for (int j = 0; j < k; ++j)
				scanf("%d", &P[k+j]);
		}
		Int res = F(1, 0);
		printf("Case #%d: %lld\n", t+1, res);
		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
}