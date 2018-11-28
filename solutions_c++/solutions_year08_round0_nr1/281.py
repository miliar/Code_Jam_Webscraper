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
#include <list>
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

int R[1010][110];
map<string, int> Map;
int A[1010];

char buf[10000];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int S, Q;
		scanf("%d", &S);
		int i;
		gets(buf);
		Map.clear();
		for (i = 0; i < S; ++i)
		{
			gets(buf);
			Map[buf] = i;
		}
		scanf("%d", &Q);
		gets(buf);
		for (i = 0; i < Q; ++i)
		{
			gets(buf);
			if (Map.find(buf) != Map.end())
				A[i] = Map[buf];
			else
				A[i] = -1;
		}
		int j;
		for (i = 0; i <= Q; ++i)
			for (j = 0; j < S; ++j)
				R[i][j] = 1000000;
		for (i = 0; i < S; ++i)
			R[0][i] = 0;
		int k;
		for (i = 0; i < Q; ++i)
			for (j = 0; j < S; ++j)
			{
				if (A[i] != j)
					R[i+1][j] = min(R[i+1][j], R[i][j]);
				for (k = 0; k < S; ++k)
					if (j != k && A[i] != k)
						R[i+1][k] = min(R[i+1][k], R[i][j]+1);
			}
		int res = 1000000;
		for (i = 0; i < S; ++i)
			res = min(res, R[Q][i]);
		printf("Case #%d: %d\n", t+1, res);
	}

	return 0;
}