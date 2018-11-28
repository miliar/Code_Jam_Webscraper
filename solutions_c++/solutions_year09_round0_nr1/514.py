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

string S[1 << 14];
string A[1 << 14];
char buf[1 << 14];

int F(int from, int to, int pos, int cnt)
{
	if(from >= to)
		return 0;
	if(pos == cnt)
		return to - from;

	int res = 0;
	int i;
	FOR(i, 0, SIZE(A[pos]))
	{
		char c = A[pos][i];
		while(from < to && S[from][pos] < c)
			++from;
		int temp = from;
		while(temp < to && S[temp][pos] == c)
			++temp;

		res += F(from, temp, pos + 1, cnt);
	}

	return res;
}

int SolveTest(int test)
{
	int L, D, N;
	scanf("%d%d%d", &L, &D, &N);
	int i, j, k;
	FOR(i, 0, D)
	{
		scanf("%s", buf);
		S[i] = buf;
	}

	sort(S, S + D);

	FOR(i, 0, N)
	{
		scanf("%s", buf);
		int len = strlen(buf);
		stringstream temp;
		int cnt = 0;
		FOR(k, 0, len)
		{
			if(cnt == 0)
				temp << ' ';
			if(buf[k] != '(' && buf[k] != ')')
				temp << buf[k];
			if(buf[k] == '(')
				++cnt;
			if(buf[k] == ')')
				--cnt;
		}

		string s = temp.str();
		stringstream ss(s);
		
		FOR(j, 0, L)
		{
			ss >> A[j];
			sort(ALL(A[j]));
			A[j].resize(unique(ALL(A[j])) - A[j].begin());
		}

		printf("Case #%d: %d\n", i + 1, F(0, D, 0, L));
	}

	return 0;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	SolveTest(-1);

	return 0;
};
