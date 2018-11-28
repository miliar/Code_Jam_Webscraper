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

int SolveTest(int test)
{
	int N;
	scanf("%d", &N);
	int i, j;
	int A[64];
	FOR(i, 0, N)
	{
		char buf[64];
		scanf("%s", buf);
		int pos = N - 1;
		while(pos != -1 && buf[pos] == '0')
			--pos;

		A[i] = pos;
	}

	int res = 0;
	FOR(i, 0, N)
	{
		FOR(j, i, N)
			if(A[j] <= i)
				break;

		RFOR(j, j, i)
		{
			swap(A[j], A[j + 1]);
			++res;
		}
	}

	printf("Case #%d: %d\n", test + 1, res);

	return 0;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	char buf[1 << 10];
	gets(buf);
	int T, t;
	sscanf(buf, "%d", &T);
	FOR(t, 0, T)
		SolveTest(t);

	return 0;
};
