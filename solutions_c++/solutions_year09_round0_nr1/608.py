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

int W[5010][20];
char buf[100000];
int A[20];

int main()
{
//	freopen("A-small.in", "r", stdin);
//	freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int L, D, N;
	scanf("%d%d%d", &L, &D, &N);
	int i, j;
	for (i = 0; i < D; ++i)
	{
		scanf("%s", buf);
		for (j = 0; j < L; ++j)
			W[i][j] = (1<<(buf[j]-'a'));
	}
	for (i = 0; i < N; ++i)
	{
		scanf("%s", buf);
		int p = 0;
		for (j = 0; j < L; ++j)
		{
			A[j] = 0;
			if (buf[p] == '(')
			{
				++p;
				while (buf[p] != ')')
				{
					A[j] |= (1<<(buf[p]-'a'));
					++p;
				}
				++p;
			}
			else
			{
				A[j] |= (1<<(buf[p]-'a'));
				++p;
			}
		}
		int res = 0;
		for (j = 0; j < D; ++j)
		{
			int q;
			for (q = 0; q < L; ++q)
				if ((A[q] & W[j][q]) == 0)
					break;
			if (q >= L)
				++res;
		}
		printf("Case #%d: %d\n", i+1, res);
		fprintf(stderr, "%d\n", i+1);
	}
	return 0;
}