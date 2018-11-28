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

#define N 1010

int sign[2] = {1,-1};

int test,t;
int a[N],n;
double f[N],p[N];
double rfact[N];

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d",&test);
	/*rfact[0] = 1;
	FOR(i,1,N)
		rfact[i] = rfact[i-1]/i;
	REP(i,N)
		FOR(j,2,i+1)
			p[i] += sign[j%2] * rfact[j];
	f[1] = 0;
	FOR(i,2,N)
	{
		double sum = 1;
		FOR(j,1,i)
			sum += p[i-j]*rfact[j]*f[i-j];
		f[i] = sum/(1-p[i]);
	}*/
	FOR(t,1,test+1)
	{
		scanf("%d",&n);
		REP(i,n)
			scanf("%d",&a[i]);
		int j=0;
		REP(i,n)
			j += (a[i]!=i+1);
		//printf("Case #%d: %.9lf\n",t,f[j]);
		printf("Case #%d: %.9lf\n",t,(double)j);
	}
	return 0;
}
