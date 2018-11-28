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

#define base 100000000LL
#define MAX 7
#define LSTR "%08d"

Int Temp[MAX];
char buf[100];

struct Long
{
	int A[MAX];

	void clear()
	{
		memset(A, 0, sizeof(int) * MAX);
	}
	Long()
	{
		clear();
	}

	Long operator + (Long & L)
	{
		Long res;
		int i;
		int rem = 0;
		for (i = 0; i < MAX; ++i)
		{
			res.A[i] = A[i] + L.A[i] + rem;
			if (res.A[i] >= base)
			{
				res.A[i] -= base;
				rem = 1;
			}
			else
				rem = 0;
		}
		return res;
	}

	Long operator - (Long & L)
	{
		Long res;
		int i;
		int rem = 0;
		for (i = 0; i < MAX; ++i)
		{
			res.A[i] = A[i] - L.A[i] - rem;
			if (res.A[i] < 0)
			{
				res.A[i] += base;
				rem = 1;
			}
			else
				rem = 0;
		}
		return res;
	}

	bool operator < (Long & L)
	{
		int i;
		for (i = MAX-1; i > 0; --i)
		{
			if (A[i] != L.A[i])
				break;
		}
		return A[i] < L.A[i];
	}

	void operator = (Long & L)
	{
		int i;
		for (i = 0; i < MAX; ++i)
			A[i] = L.A[i];
	}

	Long operator * (Long & L)
	{
		CLEAR(Temp, 0);
		int i, j;
		for (i = 0; i < MAX; ++i)
			for (j = 0; i+j < MAX; ++j)
				Temp[i+j] += A[i] * (Int)L.A[j];
		Long res;
		Int rem = 0;
		for (i = 0; i < MAX; ++i)
		{
			Temp[i] += rem;
			res.A[i] = Temp[i] % base;
			rem = Temp[i] / base;
		}
		return res;
	}

	void div2()
	{
		int i;
		int rem = 0;
		for (i = MAX-1; i >= 0; --i)
		{
			A[i] += rem;
			if (A[i] & 1)
				rem = base;
			else
				rem = 0;
			A[i] >>= 1;
		}
	}

	Long operator / (Long & L)
	{
		Long ub, lb, cb;
		Long one;
		one.A[0] = 1;
		ub = *this + one;
		while (one < ub - lb)
		{
			cb = ub+lb;
			cb.div2();
			if (*this < cb * L)
				ub = cb;
			else
				lb = cb;
		}
		return lb;
	}

	Long operator % (Long & L)
	{
		Long res;
		res = *this - ((*this / L) * L);
		return res;
	}

	void read()
	{
		clear();
		scanf("%s", buf);
		int i;
		int st10 = 1;
		int p = 0;
		for (i = strlen(buf)-1; i >= 0; --i)
		{
			A[p] += st10 * (buf[i]-'0');
			st10 *= 10;
			if (st10 == base)
			{
				st10 = 1;
				++p;
			}
		}
	}

	void print()
	{
		int i;
		for (i = MAX-1; i > 0; --i)
			if (A[i])
				break;
		printf("%d", A[i]);
		for (i--; i >= 0; --i)
			printf(LSTR, A[i]);
	}
};

Long LGCD(Long A, Long B)
{
	Long C, L0;
	if (B < A)
	{
		C = B;
		B = A;
		A = C;
	}
	while (L0 < A)
	{
		C = B % A;
		B = A;
		A = C;
	}
	return B;
}

Long X[1010];
Long G;
Long R, LNil;

int main()
{
//	freopen("B-small.in", "r", stdin);
//	freopen("B-small.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
			X[i].read();
		int mi = 0;
		for (int i = 1; i < N; ++i)
			if (X[i] < X[mi])
				mi = i;
		G.clear();
		for (int i = 0; i < N; ++i)
			if (i != mi)
			{
				G = LGCD(G, X[i] - X[mi]);
			}
		R = X[mi] % G;
		if (LNil < R)
		{
			R = G - R;
		}
		printf("Case #%d: ", t+1);
		R.print();
		printf("\n");

		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
}