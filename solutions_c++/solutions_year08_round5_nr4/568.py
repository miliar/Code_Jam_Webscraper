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

int R, C;
map<int, bool> m;
map<int, int> m1;

int find1(int n)
{
	int r = n / C;
	int c = n % C;
	if (r < 0 || c < 0) return 0;
	if (r == 0 && c == 0) return 1;
	if (m[n]) return 0;
	
	if (m1.count(n)) return m1[n];

	int &ret = m1[n] = 0;
	
	if (r > 0 && c > 1)
		ret += find1((r-1)*C + (c-2));
	if (r > 1 && c > 0)
		ret += find1((r-2)*C + (c-1));

    ret %= 10007;

	return ret;
}

void solve()
{
	int n;
	m.clear();
	m1.clear();
	scanf("%d%d%d",&R,&C, &n);
	REP(i,n){
		int r, c;
		scanf("%d%d",&r,&c);
		r--; c--;
		m[r*C + c] = true;
	}

	printf("%d\n", find1(R*C - 1));
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

