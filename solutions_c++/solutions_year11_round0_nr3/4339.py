#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

#define INF 1000000000

map<pair<int, pair<pair<int, int>, pair<int, int> > >, int> f;
int T, N, can[1000];

int doit(int id, int a, int b, int c, int d)
{
	if(id == N)
	{
		if(a == b && c && d)
			return 0;
		return -INF;
	}
	if(f.count(make_pair(id, make_pair(make_pair(a, b), make_pair(c, d)))) > 0)
		return f[make_pair(id, make_pair(make_pair(a, b), make_pair(c, d)))];
	return f[make_pair(id, make_pair(make_pair(a, b), make_pair(c, d)))] = max(doit(id + 1, a, b ^ can[id], c, 1), doit(id + 1, a ^ can[id], b, 1, d) + can[id]);
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for(int tc = 1; tc <= T; ++tc)
	{
		scanf("%d", &N);
		for(int i = 0; i < N; ++i)
			scanf("%d", &can[i]);
		f.clear();
		int res = doit(0, 0, 0, 0, 0);
		printf("Case #%d: ", tc);
		if(res < 1)
			printf("NO\n");
		else
			printf("%d\n", res);
	}
	return 0;
}