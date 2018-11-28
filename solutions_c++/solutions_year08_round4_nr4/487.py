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

char S[1100];
char A[1100];

int main()
{
	freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
//	freopen("-large.in", "r", stdin);
//	freopen("-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0;t <T ; ++t)
	{
		int K;
		scanf("%d", &K);
		scanf("%s", S);
		VInt v;
		int i;
		for (i = 0; i < K; ++i)
			v.PB(i);
		int N = strlen(S);
		int res = N+N;
		do
		{
			for (i = 0; i*K < N; ++i)
			{
				int j;
				for (j = 0; j < K; ++j)
					A[i*K+j] = S[i*K+v[j]];
			}
			int r = 1;
			for (i = 1; i < N; ++i)
				if (A[i] != A[i-1])
					++r;
			res = min(res, r);
		} while (next_permutation(ALL(v)));
		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
};
