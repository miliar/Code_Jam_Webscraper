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

char B[55][55];
int A[55];
int P[55];

int main()
{
//	freopen("A-small.in", "r", stdin);
//	freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0 ;t < T; ++t)
	{
		int N;
		scanf("%d", &N);
		int i, j;
		for (i = 0; i < N; ++i)
			scanf("%s", B[i]);
		for (i = 0; i < N; ++i)
		{
			A[i] = N-1;
			while (A[i] > 0 && B[i][A[i]] == '0')
				--A[i];
		}
		CLEAR(P, -1);
		for (i = 0; i < N; ++i)
		{
			for (j = 0; j < N; ++j)
				if (P[j] == -1 && A[j] <= i)
				{
					P[j] = i;
					break;
				}
		}
		int res = 0;
		for (i = 0; i < N; ++i)
			for (j = i+1; j < N; ++j)
				if (P[i] > P[j])
					++res;
		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}