#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <algorithm>
#include <string>

#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PI;

#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SET(v,x) memset(v,x,sizeof v)
#define FOR(i,a,b) for(int _n(b),i(a);i<_n;i++) 
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define SZ(v) int(v.size())
#define SI ({int x;scanf("%d",&x);x;})

#define MX 1005

int a[MX];

void solve()
{
	int n = SI, sum = 0, xor = 0;
	REP(i,n) a[i]=SI,sum+=a[i],xor^=a[i];
	sort(a,a+n);
	if(xor!=0){ puts("NO"); return; }
	printf("%d\n",sum-a[0]);
}

int main()
{
	//freopen("C-small-attempt0.in","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("cout.out","w",stdout);
	
	int kases; scanf("%d",&kases);
	
	for(int kase=1;kase<=kases;kase++)
	{
		printf("Case #%d: ",kase);
		solve();
	}
	
	return 0;
}


