#include<iostream>
#include<stdio.h>
#include<assert.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>
#include<math.h>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#pragma comment(linker, "/STACK:16777216")
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define LL long long
#define bit __builtin_popcountll
#define sqr(x) (x) * (x)
using namespace std;
typedef pair<int, int> pii;
const double eps = 1e-9;
const double pi = acos(-1.0);
const int maxn = (int)1e4 + 10;
int d[maxn],l[maxn],n,D,dp[maxn];
bool can()
{
	memset(dp,0,sizeof(dp));
	dp[0] = d[0];
	for(int i = 0; i < n; i++)
	{
		if (dp[i] + d[i] >= D) return true;
		for(int j = i + 1; j < n; j++)
		{
			if (d[j] - d[i] > dp[i]) continue;
			dp[j] = max(dp[j],min(d[j] - d[i],l[j]));
		}
	}
	return false;
}
int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int T;
	scanf("%d",&T);
	for(int tt = 0; tt < T; tt++)
	{
		scanf("%d",&n);
		for(int i = 0; i < n; i++)
			scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&D);
		printf("Case #%d: ",tt + 1);
		if (can()) puts("YES"); else puts("NO");
	}
	return 0;
}
