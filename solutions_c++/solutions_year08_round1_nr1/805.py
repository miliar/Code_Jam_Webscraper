#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>

#define pb push_back
#define mp make_pair
#define REP(i,n) for(int i=0; i<(n); ++i)
#define sz size()

using namespace std;

typedef vector<int> vi;
typedef long long ll;

vector<ll> a,b;

ll go(int cur, int index)
{
	if(cur >= a.sz) return 0LL;
	ll ret = -9000000000000LL;

	REP(i,b.sz) {
//		printf("-%d-%d-\n",(1 << i) & index,index);
		if(((1 << i) & index) == 0) {
			ll asum = go(cur+1,index | (1 << i))+a[cur]*b[i];
			if(asum > ret) ret = asum;
		}
	}
	//printf("%d %I64d\n",cur,ret);
	return ret;
}

void solve()
{
	int n,s;
	scanf("%d",&n);

	a.clear();
	b.clear();

	REP(i,n) {
		scanf("%d",&s);
		a.pb(s);
	}

	REP(i,n) {
		scanf("%d",&s);
		b.pb(-s);
	}
	/*
	sort(a.begin(),a.end());
	sort(b.begin(),b.end());
	ll sum = 0;
	REP(i,n) {
		sum += a[i] * b[i];
	}
	ll min = sum;
	*/

	printf("%I64d\n",-go(0,0));
}

int main()
{
	int t;
	scanf("%d",&t);
	REP(i,t) {
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;

}
