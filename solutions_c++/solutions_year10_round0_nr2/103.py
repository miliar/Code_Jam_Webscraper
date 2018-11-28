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

#define MAX 64
#define BASE 1000
#define STR_OUT "%03d"
struct Long
{
	int A[MAX];

	Long(char buf[])
	{
		CLEAR(A, 0);
		int len = strlen(buf);
		int i;
		FOR(i, 0, len)
		{
			(*this) *= 10;
			A[0] += buf[i] - '0';
		}
	}

	Long(int a = 0)
	{
		CLEAR(A, 0);
		A[0] = a;
	}

	void operator *= (Long a)
	{
		Long b = *this;
		CLEAR(A, 0);
		int i, j;
		FOR(i, 0, MAX)
			FOR(j, 0, MAX - i)
				A[i + j] += a.A[i]*b.A[j];

		FOR(i, 0, MAX - 1)
		{
			A[i + 1] += A[i]/BASE;
			A[i] %= BASE;
		}
	}

	void operator += (const Long& a)
	{
		int i;
		FOR(i, 0, MAX)
			A[i] += a.A[i];

		FOR(i, 0, MAX - 1)
			if(A[i] >= BASE)
			{
				++A[i + 1];
				A[i] -= BASE;
			}
	}

	void operator -= (const Long& a)
	{
		int i;
		FOR(i, 0, MAX)
			A[i] -= a.A[i];

		FOR(i, 0, MAX - 1)
			if(A[i] < 0)
			{
				--A[i + 1];
				A[i] += BASE;
			}
	}

	void operator %= (Long a)
	{
		if(!((*this) < a))
		{
			Long b;
			b += a;
			b += a;
			(*this) %= b;
			if(!((*this) < a))
				(*this) -= a;
		}
	}

	void operator /= (Long a)
	{
		if((*this) < a)
		{
			CLEAR(A, 0);
			return;
		}

		Long b;
		b += a;
		b += a;
		Long old;
		old = *this;

		(*this) /= b;
		(*this) *= 2;

		Long c;
		c = *this;
		c *= a;
		old -= c;

		if(!(old < a))
			(*this) += Long(1);
	}

	int operator < (const Long& a)
	{
		int i;
		RFOR(i, MAX, 0)
			if(A[i] != a.A[i])
				return A[i] < a.A[i];

		return 0;
	}

	void Out()
	{
		int i;
		RFOR(i, MAX, 1)
			if(A[i])
				break;

		printf("%d", A[i]);
		RFOR(i, i, 0)
			printf(STR_OUT, A[i]);
	}
};

Long gcd(Long a, Long b)
{
	if(Long(0) < a)
	{
		b %= a;
		return gcd(b, a);
	}

	return b;
}

Long A[1 << 10];

int SolveTest(int test)
{
	int N;
	scanf("%d", &N);

	char buf[1 << 7];
	int i;
	FOR(i, 0, N)
	{
		scanf("%s", buf);
		A[i] = Long(buf);
	}

	sort(A, A + N);

	Long g = 0;
	FOR(i, 0, N - 1)
	{
		Long a = A[i + 1];
		a -= A[i];
		g = gcd(g, a);
	}

	Long a = A[0];
	a %= g;
	if(Long(0) < a)
	{
		g -= a;
		a = g;
	}

	printf("Case #%d: ", test + 1);
	a.Out();
	printf("\n");
	return 0;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int T, t;
	char buf[1 << 7];
	gets(buf);
	sscanf(buf, "%d", &T);
	FOR(t, 0, T)
	{
		fprintf(stderr, "Solving %d/%d\n", t + 1, T);
		SolveTest(t);
	}

	return 0;
};
