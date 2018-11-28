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

#define INF (1 << 20)
#define MAX (1 << 17)

int A[MAX];
int B[MAX];
int Res[2][MAX];

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T, t;
	scanf("%d", &T);
	FOR(t, 0, T)
	{
		int N, V;
		scanf("%d%d", &N, &V);

		int i, j, k, l;
		FOR(i, 0, N)
			Res[0][i] = Res[1][i] = INF;

		FOR(i, 0, (N - 1) >> 1)
			scanf("%d%d", &A[i], &B[i]);

		FOR(i, (N - 1) >> 1, N)
		{
			int a;
			scanf("%d", &a);
			Res[a][i] = 0;
		}

		RFOR(i, (N - 1) >> 1, 0)
		{
			int temp[] = {INF, INF};
			temp[ A[i] ] = 0;
			if(B[i])
				temp[ A[i] ^ 1 ] = 1;

			FOR(j, 0, 2)
				FOR(k, 0, 2)
					FOR(l, 0, 2)
					{
						int pos = (j == 0 ? k | l : k & l);
						Res[pos][i] = min(Res[pos][i], temp[j] + Res[k][ (i << 1) + 1 ] + Res[l][ (i << 1) + 2 ]);
					}
		}

		if(Res[V][0] == INF)
			printf("Case #%d: IMPOSSIBLE\n", t + 1);
		else
			printf("Case #%d: %d\n", t + 1, Res[V][0]);
	}

	return 0;
};
