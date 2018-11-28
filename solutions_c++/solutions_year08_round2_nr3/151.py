#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define PB push_back
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define MP make_pair
#define PRESENT(container, element) (container.find(element) != container.end())
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define CLEAR(c,n) memset(c,n,sizeof(c))
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double PI=acos(-1.0);
const double EPS=1e-11;
const int INF=1000000000;

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	int t, k, n, d[100], card[5000];
	scanf("%d", &t);
	REP(ic,t) {
		scanf("%d%d", &k, &n);
		REP(i,n) scanf("%d",d+i);
		queue<int> q;
		REP(i,k) q.push(i);
		REP(i,k) {
			REP(j,i) q.push(q.front()), q.pop();
			card[q.front()]=i+1; q.pop();
		}

		printf("Case #%d:", ic+1);
		REP(i,n) printf(" %d", card[d[i]-1]);
		printf("\n");
	}
	return 0;
}
