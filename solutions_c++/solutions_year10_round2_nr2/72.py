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

int X[55];
int V[55];

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
		int N, K, B, Tm;
		scanf("%d%d%d%d", &N, &K, &B, &Tm);
		for (int i = 0; i < N; ++i)
			scanf("%d", &X[i]);
		for (int i = 0; i < N; ++i)
			scanf("%d", &V[i]);
		int res = 0;
		int b = 0;
		int g = 0;
		for (int i = N-1; i >= 0 && g < K; --i)
		{
			if ((B-X[i]) <= Tm * V[i])
			{
				++g;
				res += b;
			}
			else
				++b;
		}
		printf("Case #%d: ", t+1);
		if (g >= K)
			printf("%d\n", res);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}