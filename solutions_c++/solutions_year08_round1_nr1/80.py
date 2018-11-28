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

Int A[1000];
Int B[1000];

int main()
{
//	freopen("A-small.in", "r", stdin);
//	freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int N;
		scanf("%d", &N);
		int i;
		for (i = 0; i < N; ++i)
			scanf("%lld", &A[i]);
		for (i = 0; i < N; ++i)
			scanf("%lld", &B[i]);
		sort(A, A+N);
		sort(B, B+N);
		reverse(B, B+N);
		Int res  = 0;
		for (i = 0; i < N; ++i)
			res += A[i]*B[i];
		printf("Case #%d: %lld\n", t+1, res);
		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
};
