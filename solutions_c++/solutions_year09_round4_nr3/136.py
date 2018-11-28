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

#define FOR(i, a, b) for(i = a; i < b; i++)
#define RFOR(i, a, b) for(i = a - 1; i >= b; i--)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size()) 
#define ALL(a) (a).begin(),(a).end() 

#define PB push_back
#define MP make_pair

int E[256][256];
int A[128][128];
int B[256];
int gN;

int dfs(int a)
{
	if(a == gN - 1)
		return 1;
	
	B[a] = 1;

	int i;
	FOR(i, 0, gN)
		if(B[i] == 0 && E[a][i] > 0 && dfs(i))
		{
			--E[a][i];
			++E[i][a];
			return 1;
		}

	return 0;
}


int SolveTest(int test)
{
	int N, K;
	scanf("%d%d", &N, &K);

	int i, j, k;
	FOR(i, 0, N)
		FOR(j, 0, K)
			scanf("%d", &A[i][j]);

	CLEAR(E, 0);
	FOR(i, 0, N)
		FOR(j, 0, N)
		{
			FOR(k, 0, K)
				if(A[i][k] >= A[j][k])
					break;

			if(k == K)
				E[i][N + j] = 1;
		}

	FOR(i, 0, N)
		E[N + N][i] = 1;
	FOR(i, 0, N)
		E[N + i][N + N + 1] = 1;

	gN = N + N + 2;
	int flow = 0;
	while(true)
	{
		CLEAR(B, 0);
		if(!dfs(N + N))
			break;

		++flow;
	}

	printf("Case #%d: %d\n", test + 1, N - flow);
	return 0;
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	char buf[1 << 10];
	gets(buf);
	int T, t;
	sscanf(buf, "%d", &T);
	FOR(t, 0, T)
		SolveTest(t);

	return 0;
};
