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

#define MOD 10000

char buf[1 << 10];
char A[1 << 10];
int Res[32][1 << 10];

int F(int cnt, int pos)
{
	if(cnt == -1)
		return 1;
	if(pos == -1)
		return 0;

	int& res = Res[cnt][pos];
	if(res != -1)
		return res;

	res = F(cnt, pos - 1);
	if(A[cnt] == buf[pos])
		res += F(cnt - 1, pos - 1);

	res %= MOD;
	return res;
}

int SolveTest(int test)
{
	gets(buf);
	int len = strlen(buf);
	sprintf(A, "welcome to code jam");
	int N = strlen(A);

	CLEAR(Res, -1);
	printf("Case #%d: %04d\n", test + 1, F(N - 1, len - 1));
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
		SolveTest(t);

	return 0;
};
