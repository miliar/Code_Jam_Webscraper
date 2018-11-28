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

int G[1010];
int P[1010];
Int S[1010];
int NP[1010];
Int NS[1010];

int main()
{
//	freopen("C-small.in", "r", stdin);
//	freopen("C-small.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int R, K, N;
		scanf("%d%d%d", &R, &K, &N);
		for (int i = 0; i < N; ++i)
			scanf("%d", &G[i]);
		int i = 0;
		Int sum = 0;
		for (int j = 0; j < N; ++j)
		{
			while (i < N && sum + G[(j+i)%N] <= K)
			{
				sum += G[(i+j)%N];
				++i;
			}
			P[j] = (j+i) % N;
			S[j] = sum;
			sum -= G[j];
			--i;
		}
		Int res = 0;
		int pos = 0;
		while (R)
		{
			if (R & 1)
			{
				res += S[pos];
				pos = P[pos];
			}
			R >>= 1;
			for (i = 0; i < N; ++i)
			{
				NP[i] = P[P[i]];
				NS[i] = S[i] + S[P[i]];
			}
			for (i = 0; i < N; ++i)
			{
				P[i] = NP[i];
				S[i] = NS[i];
			}
		}
		printf("Case #%d: %lld\n", t+1, res);
	}
	return 0;
}