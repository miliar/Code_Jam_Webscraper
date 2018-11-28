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

inline void F(int N, int M, int A)
{
	int x, y, xx, yy;
	for (x = 0; x <= N; ++x)
		for (y = 0; y <= M; ++y)
			for (xx = 0; xx <= N; ++xx)
				for (yy = 0; yy <= M; ++yy)
					if (x*yy - xx*y == A)
					{
						printf("0 0 %d %d %d %d\n", x, y, xx, yy);
						return ;
					}
	printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
//	freopen("-large.in", "r", stdin);
//	freopen("-large.out", "w", stdout);

	int T, t;
	scanf("%d", &T);
	for (t = 0;t < T; ++t)
	{
		int N, M, A;
		scanf("%d%d%d", &N, &M, &A);
		printf("Case #%d: ", t+1);
		F(N, M, A);
		fprintf(stderr, "%d\n", t+1);
	}

	return 0;
};
