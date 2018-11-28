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

char A[128][128];
int W[128];
int L[128];
double R[128];

int SolveTest(int test)
{
	int N;
	scanf("%d", &N);
	int i, j;
	FOR(i, 0, N)
		scanf("%s", A[i]);

	CLEAR(W, 0);
	CLEAR(L , 0); 
	FOR(i, 0, N)
		FOR(j, 0, N)
		{
			if(A[i][j] == '1')
				++W[i];
			if(A[i][j] == '0')
				++L[i];
		}


	FOR(i, 0, N)
	{
		double r = 0;
		FOR(j, 0, N)
			if(A[i][j] != '.')
			{
				int w = W[j];
				int l = L[j];
				if(A[j][i] == '1')
					--w;
				else
					--l;

				r += (w + 0.0)/(w + l);
			}

		R[i] = r/(W[i] + L[i]);
	}

	printf("Case #%d:\n", test + 1);
	FOR(i, 0, N)
	{
		double a = (W[i] + 0.0)/(W[i] + L[i]);
		double b = R[i];
		double c = 0;
		FOR(j, 0, N)
			if(A[i][j] != '.')
				c += R[j];

		c /= (W[i] + L[i]);
		printf("%.7lf\n", a/4 + b/2 + c/4);
	}

	return 0;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

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
