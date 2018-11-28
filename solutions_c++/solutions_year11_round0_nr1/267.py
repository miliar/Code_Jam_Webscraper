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

template <class T> void smin(T& a, const T& b) { if(a>b) a=b; }
template <class T> void smax(T& a, const T& b) { if(a<b) a=b; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a%b) : a; }
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

int test,t;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&test);
	int n;
	FOR(t,1,test+1)
	{
		scanf("%d",&n);
		int curt=0, j, k;
		char c;
		pii last[2];
		last[0] = last[1] = pii(0,1);
		REP(i,n)
		{
			scanf("%c%c%d",&c,&c,&j);
			if(c=='O')
				k = 0;else
				k = 1;
			curt++;
			curt = max(curt, last[k].X + abs(last[k].Y - j) + 1);
			last[k] = pii(curt, j);
		}
		printf("Case #%d: %d\n",t,max(last[0].X,last[1].X));
	}
	return 0;
}
