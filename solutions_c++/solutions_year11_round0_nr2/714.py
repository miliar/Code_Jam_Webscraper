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

char buf[1 << 20];
char A[128][128];
char B[128][128];

int SolveTest(int test)
{
	CLEAR(A, -1);
	CLEAR(B, -1);

	int i, j;
	int N;

	scanf("%d", &N);
	FOR(i, 0, N)
	{
		scanf("%s", buf);
		A[ buf[0] ][ buf[1] ] = A[ buf[1] ][ buf[0] ] = buf[2];
	}

	scanf("%d", &N);
	FOR(i, 0, N)
	{
		scanf("%s", buf);
		B[ buf[0] ][ buf[1] ] = B[ buf[1] ][ buf[0] ] = 1;
	}

	scanf("%d%s", &N, buf);
	vector<char> v;
	FOR(i, 0, N)
	{
		if(SIZE(v) != 0 && A[ buf[i] ][ v.back() ] != -1)
		{
			v.back() = A[ buf[i] ][ v.back() ];
			continue;
		}

		FOR(j, 0, SIZE(v))
			if(B[ buf[i] ][ v[j] ] != -1)
				break;

		if(j == SIZE(v))
			v.PB(buf[i]);
		else
			v.clear();
	}

	printf("Case #%d: [", test + 1);
	FOR(i, 0, SIZE(v))
		printf("%c%s", v[i], i == SIZE(v) - 1 ? "]\n" : ", ");

	if(v.empty())
		printf("]\n");

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
