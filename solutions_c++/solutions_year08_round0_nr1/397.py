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

char buf[1 << 20];
char Name[128][1 << 10];
int A[128];
int Res[1 << 10][1 << 10];

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	int T, t;
	gets(buf);
	sscanf(buf, "%d", &T);
	FOR(t, 0, T)
	{
		int N, M;
		gets(buf);
		sscanf(buf, "%d", &N);

		int i, j;
		FOR(i, 0, N)
			gets(Name[i]);

		gets(buf);
		sscanf(buf, "%d", &M);

		FOR(i, 0, M)
		{
			gets(buf);
			FOR(j, 0, M)
				if(strcmp(buf, Name[j]) == 0)
					break;

			A[i] = j;
		}

		FOR(i, 0, N)
			Res[i][0] = 0;

		int res = 0;
		FOR(i, 1, M + 1)
		{
			FOR(j, 0, N)
			{
				Res[j][i] = M;
				if(j == A[i - 1])
					continue;

				Res[j][i] = min(Res[j][i], min(Res[j][i - 1], res + 1));
			}

			res = M;
			FOR(j, 0, N)
				res = min(res, Res[j][i]);
		}

		printf("Case #%d: %d\n", t + 1, res);
	}
	
	return 0;
};
