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

int P[110][30];
int A[110][110];
int R[16][1<<16];

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
//	freopen("-large.in", "r", stdin);
//	freopen("-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0 ;t < T; ++t)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		int i, j;
		for (i = 0; i < N; ++i)
			for (j = 0; j < K; ++j)
				scanf("%d", &P[i][j]);
		CLEAR(A, 0);
		for (i = 0; i < N; ++i)
			for (j = 0; j < N; ++j)
				if (P[i][0] < P[j][0])
				{
					int k;
					for (k = 1; k < K; ++k)
						if (P[i][k] >= P[j][k])
							break;
					if (k == K)
						A[i][j] = 1;
				}

		CLEAR(R, -1);
		for (i = 0; i < N; ++i)
			R[i][(1<<i)] = 1;
		int mask;
		int all = (1<<N)-1;
		for (mask = 0; mask < all; ++mask)
			for (i = 0; i < N; ++i)
				if (R[i][mask] != -1)
				{
					for (j = 0; j < N; ++j)
						if ((mask & (1<<j)) == 0)
						{
							int nm = (mask | (1<<j));
							int nr = R[i][mask] + (1-A[i][j]);
							if (R[j][nm] == -1 || R[j][nm] > nr)
								R[j][nm] = nr;
						}
				}
		int res = 1000;
		for (i = 0; i < N; ++i)
			res = min(res, R[i][all]);
		printf("Case #%d: %d\n", t+1, res);
		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
}