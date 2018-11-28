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
#define inf 20000

typedef long long int int64_t;
typedef long long int lint;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

struct Node
{
	int interior;
	int andgate;
	int changable;
	int value;
	Node() {};
	Node(int a, int d, int b, int c) {
		interior = a;
		andgate = d;
		changable = b;
		value = c;
	}
};

Node array[20001];

int memo[20001][2];

int find(int k, int expect)
{
	Node n = array[k];
	if (memo[k][expect] != -1) return memo[k][expect];
	int &ret = memo[k][expect];
	if (!n.interior) 
		return (n.value == expect ? 0 : inf);
	ret = inf;
		if (n.andgate) {
			if (expect)
				ret = min(ret, find(k*2, 1) + find(k*2+1, 1));
			else {
				ret = min(ret, find(k*2, 0) + find(k*2+1, 0));
				ret = min(ret, find(k*2, 0) + find(k*2+1, 1));
				ret = min(ret, find(k*2, 1) + find(k*2+1, 0));
			}
		}
		else {
			if (!expect)
				ret = min(ret, find(k*2, 0) + find(k*2+1, 0));
			else {
				ret = min(ret, find(k*2, 1) + find(k*2+1, 1));
				ret = min(ret, find(k*2, 0) + find(k*2+1, 1));
				ret = min(ret, find(k*2, 1) + find(k*2+1, 0));
			}
		}
	if (n.changable) {
		if (!n.andgate) {
			if (expect)
				ret = min(ret, find(k*2, 1) + find(k*2+1, 1) + 1);
			else {
				ret = min(ret, find(k*2, 0) + find(k*2+1, 0) + 1);
				ret = min(ret, find(k*2, 0) + find(k*2+1, 1) + 1);
				ret = min(ret, find(k*2, 1) + find(k*2+1, 0) + 1);
			}
		}
		else {
			if (!expect)
				ret = min(ret, find(k*2, 0) + find(k*2+1, 0) + 1);
			else {
				ret = min(ret, find(k*2, 1) + find(k*2+1, 1) + 1);
				ret = min(ret, find(k*2, 0) + find(k*2+1, 1) + 1);
				ret = min(ret, find(k*2, 1) + find(k*2+1, 0) + 1);
			}
		}
	}
	return ret;
}

void solve()
{

	int m, v;

	scanf("%d%d",&m,&v);
	memset(memo, -1, sizeof(memo));
	REP(i, m) {
		if (i < (m-1)/2) {
			int g, c;
			scanf("%d%d",&g,&c);
			array[i+1] = Node(1, g, c, 0);
		} else {
			int t;
			scanf("%d",&t);
			array[i+1] = Node(0, 0, 0, t);
		}
	}
	int ret = find(1, v);

	if (ret >= inf)
		printf("IMPOSSIBLE\n");
	else printf("%d\n", ret);
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

