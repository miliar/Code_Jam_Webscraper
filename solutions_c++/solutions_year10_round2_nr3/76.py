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

#pragma comment(linker, "/STACK:40000000")

#define MOD 100003LL

Int RC[510][510];

Int C(int n, int m)
{
	if (m > n)
		return 0;
	if (n == m || m == 0)
		return 1;
	if (RC[n][m] != -1)
		return RC[n][m];
	return RC[n][m] = (C(n-1, m-1) + C(n-1, m)) % MOD;
}

Int R[510][510];

Int F(int n, int k)
{
	if (k == 1)
	{
		return 1;
	}
	Int & res = R[n][k];
	if (res != -1)
		return res;
	res = 0;
	for (int p = 1; p < k; ++p)
	{
		res = (res + F(k, p) * C(n-k-1, k-p-1)) % MOD;
	}
	return res;
}

int G(int n)
{
	int i;
	int res = 0;
	for (i = 1; i < n; ++i)
		res = (res + F(n, i)) % MOD;
	return res;
}

int main()
{
//	freopen("C-small.in", "r", stdin);
//	freopen("C-small.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	CLEAR(R, -1);
	CLEAR(RC, -1);

	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int n;
		scanf("%d", &n);
		int res = G(n);
		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}