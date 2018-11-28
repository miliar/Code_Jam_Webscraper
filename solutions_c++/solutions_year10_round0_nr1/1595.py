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

#define Filename "a"
#define sqr(a) (a)*(a)
#define abs(a) ((a) < 0 ? -(a) : (a))
#define nextline for (int CcC = getchar();CcC != '\n' && CcC != EOF;CcC = getchar());

typedef long long lng;
typedef long double ldb;

const int INF = (1 << 30)-1;
const double EPS = 1e-9;

int T;

void Load()
{
	scanf("%d", &T);
}

bool go (int n, int k)
{
	int res = 1;
	for (int i = 2;i <= n;i++)
		res = res * 2 + 1;
	if (res > k) return false;
	if (k % (res+1) == res) return true;
	return false;
}

int main()
{
	freopen(Filename".in", "r", stdin);
	freopen(Filename".out", "w", stdout);
	Load();
	for (int i = 0;i < T;i++)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		bool ans = go (N, K);
		printf("Case #%d: ", i+1);
		if (ans) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
