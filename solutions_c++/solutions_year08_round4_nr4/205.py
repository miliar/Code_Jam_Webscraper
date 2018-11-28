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

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);

	int T, t;
	scanf("%d", &T);
	FOR(t, 0, T)
	{
		int N;
		char buf[1 << 10];

		scanf("%d%s", &N, buf);

		int M = strlen(buf);
		int res = M;
		int I[16];

		int i, j;
		FOR(i, 0, N)
			I[i] = i;

		do
		{
			char prev = 0;
			int r = 0;
			FOR(i, 0, M/N)
				FOR(j, 0, N)
				{
					char pos = buf[ i*N + I[j] ];
					if(pos != prev)
						++r;

					prev = pos;
				}

			res = min(res, r);
		}
		while(next_permutation(I, I + N));

		printf("Case #%d: %d\n", t + 1, res);
	}

	return 0;
};
