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

int A[1 << 10];
int PA[1 << 10];
Int SA[1 << 10];
int PB[1 << 10];
Int SB[1 << 10];
int PR[1 << 10];
Int SR[1 << 10];

void F(int PA[], Int SA[], int PB[], Int SB[], int PC[], Int SC[], int N)
{
	int i, j;
	FOR(i, 0, N)
	{
		PC[i] = PB[ PA[i] ];
		SC[i] = SA[i] + SB[ PA[i] ];
	}
}

int SolveTest(int test)
{
	int N, K, R;
	scanf("%d%d%d", &R, &K, &N);

	int i, j;
	FOR(i, 0, N)
		scanf("%d", &A[i]);

	FOR(i, 0, N)
	{
		int sum = 0;
		FOR(j, 0, N)
		{
			if(sum + A[(i + j) % N] > K)
				break;

			sum += A[(i + j) % N];
		}

		PA[i] = (i + j) % N;
		SA[i] = sum;
	}

	FOR(i, 0, N)
	{
		PR[i] = i;
		SR[i] = 0;
	}

	for(i = 1; i <= R; i <<= 1)
	{
		if(i & R)
		{
			F(PA, SA, PR, SR, PB, SB, N);
			FOR(j, 0, N)
			{
				PR[j] = PB[j];
				SR[j] = SB[j];
			}
		}

		F(PA, SA, PA, SA, PB, SB, N);
		FOR(j, 0, N)
		{
			PA[j] = PB[j];
			SA[j] = SB[j];
		}
	}

	printf("Case #%d: %lld\n", test + 1, SR[0]);
	return 0;
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

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
