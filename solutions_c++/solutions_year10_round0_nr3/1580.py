#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <ctime>
#include <map>
#include <queue>
#include <stack>
#include <string>

using namespace std;

#define Filename "c"
#define sqr(a) (a)*(a)
#define abs(a) ((a) < 0 ? -(a) : (a))
#define nextline for (int CcC = getchar();CcC != '\n' && CcC != EOF;CcC = getchar());

typedef long long lng;
typedef long double ldb;

const int INF = (1 << 30)-1;
const double EPS = 1e-9;

queue <pair <int, int> > q, next;

int T, R, N, K;

void Load()
{
	scanf("%d", &T);
}

lng Solve()
{
	lng res = 0;
	int step = 0;
	for (step = 1;step <= R;step++)
	{
		int ost = K;
		while (!q.empty() && q.front().first <= ost)
		{
			next.push(q.front());
			res += q.front().first;
			ost -= q.front().first;
			q.pop();
		}
		while (!next.empty()) { q.push(next.front()); next.pop(); }
		if (q.front().second == 0) break;
	}
	if (step == R+1) return res;
	int mn = R / step;
	res *= mn;
	R %= step;
	for (step = 1;step <= R;step++)
	{
		int ost = K;
		while (!q.empty() && q.front().first <= ost)
		{
			next.push(q.front());
			res += q.front().first;
			ost -= q.front().first;
			q.pop();
		}
		while (!next.empty()) { q.push(next.front()); next.pop(); }
	}
	return res;
}

int main()
{
	freopen(Filename".in", "r", stdin);
	freopen(Filename".out", "w", stdout);
	Load();
	for (int i = 0;i < T;i++)
	{
		cerr << i << " ";
		scanf("%d%d%d", &R, &K, &N);
		while (!q.empty()) q.pop();
		while (!next.empty()) next.pop();
		for (int j = 0;j < N;j++)
		{
			int a;
			scanf("%d", &a);
			q.push(make_pair(a, j));
		}
		printf("Case #%d: %I64d\n", i+1, Solve());
	}
	return 0;
}
