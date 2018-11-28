#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<deque>
#include<map>
#include<functional>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOREACH(i,x) for(typeof(x)::iterator it=(x).begin(); it!=(x).end(); ++it)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define pb	push_back
#define mp	make_pair
#define eps	1e-15
#define inf 0x3FFFFFFF

typedef long long int int64_t;
typedef long long int lint;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;


void solve()
{
	int n, m, a;
	scanf("%d%d%d",&n,&m,&a);
	
	REP(i,n+1)
		REP(j,m+1)
			REP(k,n+1)
				REP(l, m+1) {
				int x1 = i;
				int y1 = j;
				int x2 = k;
				int y2 = l;
				if (abs(x1*y2 - y1*x2) == a){
					printf("0 0 %d %d %d %d\n",x1, y1, x2, y2);
					return;
				}
				}
	printf("IMPOSSIBLE\n");
}

int main(void)
{
	int t;

	scanf("%d",&t);
	
	REP(i,t) {
		printf("Case #%d: ", i+1);
		solve();
	}
}

