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

int E[10][10];
int U[10] = {0};
int C[10];
int UC[10] = {0};
int N;
int CN;

bool check(int v, int cc, int st, int p)
{
	if (UC[C[v]] == 0)
		++cc;
	++UC[C[v]];
	U[v] = 1;
	bool res = true;
	if (p != st) {
		if (E[v][st] && cc < CN)
			res = false;
	}
	if (cc < CN) {
		int ko = 0;
		for (int i = 0; i < N && res; ++i)
			if (E[v][i] && !U[i])
			{
				++ko;
				res = res && check(i, cc, st, v);
			}
		if (ko == 0)
			res = false;
	}
	--UC[C[v]];
	U[v] = 0;
	return res;
}

int CCK[10] = {0};

bool setColAndCheck(int v, int cc)
{
	if (v == N)
	{
		if (cc < CN)
			return false;
		bool res = true;
		for (int i = 0; i < N && res; ++i)
			res = res && check(i, 0, i, i);
		return res;
	}
	for (int i = 0; i < CN; ++i)
	{
		C[v] = i;
		if (CCK[i] == 0)
			++cc;
		++CCK[i];
		bool res = setColAndCheck(v+1, cc);
		--CCK[i];
		if (CCK[i] == 0)
			--cc;
		if (res)
			return true;
	}
	return false;
}

int main()
{
//	freopen("-small.in", "r", stdin);
//	freopen("-small.out", "w", stdout);
//	freopen("-large.in", "r", stdin);
//	freopen("-large.out", "w", stdout);

	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int n, m;
		scanf("%d%d", &n, &m);
		N = n;
		CLEAR(E, 0);
		for (int i = 0; i < N; ++i)
			E[i][(i+1)%N] = E[(i+1)%N][i] = 1;
		int A[10];
		int B[10];
		for (int i = 0; i < m; ++i)
			scanf("%d", &A[i]);
		for (int i = 0; i < m; ++i)
			scanf("%d", &B[i]);
		for (int i = 0; i < m; ++i)
			E[A[i]-1][B[i]-1] = E[B[i]-1][A[i]-1] = 1;
/*
CN = 4;
C[0] = 0;
C[1] = 1;
C[2] = 2;
C[3] = 0;
C[4] = 1;
C[5] = 2;
C[6] = 3;
C[7] = 3;
bool xxx = setColAndCheck(8, 4);
*/

		CN = N-1;
		while (!setColAndCheck(0, 0))
			--CN;
		printf("Case #%d: %d\n", t+1, CN);
		for (int i = 0; i < N; ++i)
			printf("%d%c", C[i]+1, i == N-1 ? '\n' : ' ');

		fprintf(stderr, "%d/%d\n", t+1, T);
	}
	return 0;
}