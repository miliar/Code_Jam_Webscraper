#include <iostream>
#include <sstream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define CL(a, v) memset(a, v, sizeof(a))
#define sz(a) (int)a.size()
#define pb push_back
#define REP(i, n) for(int i=0; i<n; ++i)
#define FOR(i, a, b) for(int i=a; i<b; ++i)
#define FORD(i, a, b) for(int i=a; i>=b; --i)
#define X first
#define Y second
#define INF 1000000000

template <class T> void smin(T& a, const T& b) { if(a>b) a=b; }
template <class T> void smax(T& a, const T& b) { if(a<b) a=b; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a%b) : a; }
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define N 1010

int test,t;
int n;
int a[N];

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&test);
	FOR(t,1,test+1)
	{
		printf("Case #%d: ",t);
		scanf("%d",&n);
		REP(i,n)
			scanf("%d",&a[i]);
		int x = 0, m = INF, sum = 0;
		REP(i,n)
		{
			x ^= a[i];
			sum += a[i];
			m = min(m, a[i]);
		}
		if(x)
			printf("NO\n");else
			printf("%d\n", sum - m);
	}
	return 0;
}
