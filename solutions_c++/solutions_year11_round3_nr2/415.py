#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
using namespace std;
 
#define DEBUG(x) //x
#define REP(i,a) for(int i=0;i<int(a);i++)
#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define VI vector<int>
#define size(x) int((x).size())
#define all(x) (x).begin(), (x).end()
#define MK(x, y) make_pair(x, y)
#define PB push_back
 
typedef pair<int, int> pii;
typedef long long ll;

ll v[1000010], sum[1000010];
ll dp[1500][4];
ll l, t, n, c;

long long go(int star, int x)
{
	if(star == n)
		return 0;

	if(dp[star][x] != -1)
		return dp[star][x];
		
	ll ret = 2*v[star] + go(star+1, x);
	if(sum[star] > t/2 && x){
		int k;
		if(star == 0)
			k = t;
		else 
			k = max(t-2*sum[star-1], 0ll);
		ret = min(ret, (k/2 + v[star]) + go(star+1, x-1));
	}
	return dp[star][x] = ret;
}

int solve()
{
	scanf("%lld %lld %lld %lld\n", &l, &t, &n, &c);
	for(int i = 0; i < c; i++) 
		scanf("%lld", &v[i]);
	for(int i = c; i < n; i++)
		v[i] = v[i%c];
	sum[0] = v[0];
	for(int i = 1; i < n; i++)
		sum[i] = sum[i-1] + v[i];

	memset(dp,-1,sizeof dp);
	printf("%lld\n", go(0,l));
}


/*********/

int main(void){
	int T,t;
	scanf("%d",&T);
	REP(t,T){
		printf("Case #%d: ",t+1);
		solve();
	}
	return 0;
}

