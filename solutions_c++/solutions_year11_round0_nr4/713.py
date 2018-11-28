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

double A[1 << 10][1 << 10][2];
double R[1 << 10];

int SolveTest(int test)
{
	int N;
	scanf("%d", &N);

	int i, j, k;
	int cnt = 0;
	FOR(i, 0, N)
	{
		int a;
		scanf("%d", &a);
		if(a != i + 1)
			++cnt;
	}

	CLEAR(A, 0);
	A[0][0][0] = 1;
	FOR(i, 1, cnt + 1)
		FOR(j, 0, i + 1)
			FOR(k, 0, 2)
			{
				double& res = A[i][j][k];
				res += A[i - 1][j][1]*(i - 1)/i;
				int jj = j;
				if(k == 0)
					--jj;
				if(jj >= 0)
					res += A[i - 1][jj][0]/i;
			}

	R[0] = 0;
	FOR(i, 1, cnt + 1)
	{
		double sum = 0;
		double res = 1;
		FOR(j, 1, i + 1)
			res += R[i - j]*A[i][j][0];

		R[i] = res / (1 - A[i][0][0]);
	}

	printf("Case #%d: %.7lf\n", test + 1, R[cnt]);
	return 0;
}

int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);

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
