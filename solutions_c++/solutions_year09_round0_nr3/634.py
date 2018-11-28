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

#define MOD 10000

int R[510][22];
char S[10000];
char * W = "welcome to code jam";

int main()
{
//	freopen("C-small.in", "r", stdin);
//	freopen("C-small.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	int T, t;
	scanf("%d", &T);
	gets(S);
	for (t = 0; t < T; ++t)
	{
		gets(S);
		CLEAR(R, 0);
		R[0][0] = 1;
		int N = strlen(S);
		int M = strlen(W);
		int i, j;
		for (i = 0; i < N; ++i)
			for (j = 0; j <= M; ++j)
			{
				R[i+1][j] += R[i][j];
				if (R[i+1][j] >= MOD)
					R[i+1][j] -= MOD;
				if (S[i] == W[j])
				{
					R[i+1][j+1] += R[i][j];
					if (R[i+1][j+1] >= MOD)
						R[i+1][j+1] -= MOD;
				}
			}
		printf("Case #%d: %04d\n", t+1, R[N][M]);
		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
}