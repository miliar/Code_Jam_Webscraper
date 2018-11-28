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

#define MAX 1000000

int P[MAX];
int S[12];


int poww(int x, int s, int mod)
{
	if (s == 0)
		return 1;
	int r = poww(x, s>>1, mod);
	r = (r*(Int)r) % mod;
	if (s & 1)
	{
		r = (r*(Int)x) % mod;
	}
	return r;
}

int inv(int x, int pmod)
{
	return poww(x, pmod-2, pmod);
}

int F2(int st10)
{
	int m = max(S[0], S[1]);

	int res = -1;
	for (int p = m+1; p < st10; ++p)
		if (P[p] == 0)
		{
			for (int a = 0; a < p; ++a)
			{
				int b = ((S[1] - a*(Int)S[0]) % p + p) % p;
				int nx = (S[1]*(Int)a+b) % p;
				if (res != -1 && res != nx)
					return -1;
				res = nx;
			}
		}
	return res;
}

int F(int D, int K)
{
	if (K == 1)
		return -1;
	int st10 = 1;
	for (int i = 0; i < D; ++i)
		st10 *= 10;

	if (S[0] == S[1])
	{
		int i;
		for (i = 1; i < K; ++i)
			if (S[i] != S[0])
				break;
		if (i < K)
			return -1;
		return S[0];
	}

	if (K == 2)
		return F2(st10);

	int m = S[0];
	for (int i = 0; i < K; ++i)
		m = max(m, S[i]);

	int res = -1;
	for (int p = m+1; p < st10; ++p)
		if (P[p] == 0)
		{
			int a = (S[1] - S[2] + p) % p * (Int)inv((S[0]-S[1]+p)%p, p);
			int b = ((S[1] - a*(Int)S[0]) % p + p) % p;
			int i;
			for (i = 1; i < K; ++i)
				if (S[i] != (S[i-1]*(Int)a + b) % p)
					break;
			if (i == K)
			{
				int nx = (S[K-1]*(Int)a+b) % p;
				if (res != -1 && res != nx)
					return -1;
				res = nx;
			}
		}
	return res;
}

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);
	CLEAR(P, 0);
	P[0] = P[1] = 1;
	for (int i = 2; i < MAX; ++i)
		if (P[i] == 0)
		{
			for (int j = i+i; j < MAX; j += i)
				P[j] = 1;
		}
	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int D, K;
		scanf("%d%d", &D, &K);
		for (int i = 0; i < K; ++i)
			scanf("%d", &S[i]);
		int res = F(D, K);
		printf("Case #%d: ", t+1);
		if (res == -1)
			printf("I don't know.\n");
		else
			printf("%d\n", res);
		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
}