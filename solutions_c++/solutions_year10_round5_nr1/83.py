#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define NAME "A-large"
int d,n;
int a[128];

#define MAXP 1024000
bool iscomp[MAXP];
int pr[MAXP],prc;
void getPrimes() {
	CLEAR(iscomp); prc=0;
	for (int i = 2; i < MAXP; i++) if (!iscomp[i])	{
		pr[prc++]=i;
		if (i <= MAXP/i) for (int j = i*i; j < MAXP; j+=i)
			iscomp[j]=true;
	} }

template<class T> inline T gcd(T a,T b) {
	if(a<0)a=-a; if(b<0)b=-b; if(a<b)swap(a,b);
	while (b) {T t = b; b=a%b; a=t;} return a; }
template <typename T> T euclide(T a, T b, T &x, T &y) {
	if (a<0) { T g = euclide(-a,b,x,y); x=-x; return g; }
	if (b<0) { T g = euclide(a,-b,x,y); y=-y; return g; }
	if (a<b) return euclide(b,a,y,x);
	if (!b) { x = 1; y = 0; return a; }
	T x1, y1;
	T g = euclide(b, a%b, x1, y1);
	x = y1;
	y = x1 - (a/b)*y1;
// in oder to avoid overflow:
//	T d = x/b; x -= d*b; y += d*a;
	return g; }
template<class T> inline T inverse(T a, T n)
{	T x,y; euclide(a,n,x,y); return ((x%n)+n)%n;}

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	getPrimes();

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		fprintf(stderr,"Test #%d\n",tst+1);

		scanf("%d%d",&d,&n);
		REP(i,n)
			scanf("%d",a+i);
		int res;
		bool eq = true;
		REP(i,n)
			if (a[i]!=a[0])
				eq=false;
		if (n==1)
			res=-1;
		else if (eq)
			res=a[0];
		else if (n==2) //CHECK!
			res=-1;
		else
		{
			int pw10 = 1;
			REP(i,d)
				pw10*=10;
			res = -1;
			bool many = false;
			REP(i,prc)
			{
				int x = pr[i];
				if (x>=pw10) continue;
				bool ok = true;
				REP(i,n)
				{
					if (a[i]>=x)
						ok=false;
				}
				if (!ok) continue;
				LL A = (inverse((LL)(a[1]-a[0]+x)%x,(LL)x)*((LL)(a[2]-a[1]+x)%x))%x;
				LL B = a[1]-a[0]*A;
				B%=x;
				B+=x;
				B%=x;
				REP(i,n) if (i>0)
					if (a[i] != (A*a[i-1]+B)%x)
						ok=false;
				if (!ok) continue;
				LL next = (A*a[n-1]+B)%x;
				if (res==-1)
					res=next;
				else if (res!=next)
				{
					many=true;
					break;
				}
			}
			if (many)
				res=-1;
		}
		printf("Case #%d: ",tst+1);
		if (res==-1)
			printf("I don't know.\n");
		else
			printf("%d\n",res);
	}
	return 0;
}