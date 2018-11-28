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

#define MAX 5000000
#define INF 100000000

int R[MAX+110000];

int B[110];

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
//	freopen("B-large.in", "r", stdin);
//	freopen("B-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		Int L;
		int N;
		scanf("%lld%d", &L, &N);
		for (int i = 0; i < N; ++i)
			scanf("%d", &B[i]);
		R[0] = 0;
		int M = (int)min((Int)MAX, L);
		for (int i = 1; i <= M; ++i)
			R[i] = INF;

		for (int i = 0; i < N; ++i)
		{
			int x = B[i];
			for (int j = 0; j < M; ++j)
				R[j+x] = min(R[j+x], R[j]+1);
		}
		Int res = -1;
		if (M >= L)
		{
			if (R[L] != INF)
				res = R[L];
		}
		else
		{
			Int rest = L - M;
			for (int i = 0; i < N; ++i)
			{
				Int x = B[i];
				Int st = (rest+x-1) / x;
				Int cnt = st;
				for (Int r = L - st*x; r >= 0; r -= x, ++cnt)
					if (R[r] != INF)
					{
						Int nr = cnt + R[r];
						if (res == -1 || res > nr)
							res = nr;
					}
			}

		}

		printf("Case #%d: ", t+1);
		if (res == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%lld\n", res);

		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
}