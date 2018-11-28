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

bool B[110][110] = {0};
bool NB[110][110] = {0};

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
//	freopen("-large.in", "r", stdin);
//	freopen("-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0; t< T; ++t)
	{
		int K;
		scanf("%d", &K);
		CLEAR(B, 0);
		int X, Y;
		X = Y = 1;
		for (int i = 0; i < K; ++i)
		{
			int ax, ay, bx, by;
			scanf("%d%d", &ax, &ay);
			scanf("%d%d", &bx, &by);
			X = max(X, bx+1);
			Y = max(Y, by+1);
			for (int x = ax; x <= bx; ++x)
				for (int y = ay; y <= by; ++y)
					B[x][y] = 1;
		}
		int res = 0;
		while (K)
		{
			++res;
			int k = 0;
			for (int i = 1; i < X; ++i)
				for (int j = 1; j < Y; ++j)
					if (B[i-1][j] && B[i][j-1] || (B[i][j] && (B[i-1][j] || B[i][j-1])))
					{
						NB[i][j] = 1;
						++k;
					}
					else
						NB[i][j] = 0;
			for (int i = 1; i < X; ++i)
				for (int j = 1; j < Y; ++j)
					B[i][j] = NB[i][j];
			if (!k)
				break;
		}

		printf("Case #%d: %d\n", t+1, res);
		fprintf(stderr, "%d\n", t+1);
	}

	return 0;
}