#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

typedef pair<int, long long> pill;

int ntest;
int N, M;
long long na[105], ta[105];
long long nb[105], tb[105];
map<pair<pill, pill>, long long> dp;

long long go(int a, long long aleft, int b, long long bleft, int prev)
{
	if(a == N || b == M)
		return 0LL;
	if(dp.count(make_pair(pill(a, aleft), pill(b, bleft))))
		return dp[make_pair(pill(a, aleft), pill(b, bleft))];
	//if(dp[a][b][prev] != -1)
	//	return dp[a][b][prev];
	long long maxi = 0LL;
	if(ta[a] == tb[b])
	{
		if(aleft < bleft)
			maxi = max(maxi, aleft + go(a + 1, na[a + 1], b, bleft - aleft, 0));
		else
			maxi = max(maxi, bleft + go(a, aleft - bleft, b + 1, nb[b + 1], 1));
	}
	else
	{
		maxi = max(maxi, go(a + 1, na[a + 1], b, bleft, 2));
		maxi = max(maxi, go(a, aleft, b + 1, nb[b + 1], 3));
	}
	//dp[a][b][prev] = maxi;
	dp[make_pair(pill(a, aleft), pill(b, bleft))] = maxi;
	return maxi;
}

int main()
{
	scanf("%d", &ntest);
	for(int test = 1;test <= ntest;++test)
	{
		dp.clear();
		scanf("%d %d", &N, &M);
		for(int i = 0;i < N;++i)
			scanf("%lld %lld", &na[i], &ta[i]);
		for(int i = 0;i < M ;++i)
			scanf("%lld %lld", &nb[i], &tb[i]);
		printf("Case #%d: %lld\n", test, go(0, na[0], 0, nb[0], 0));
	}
}
