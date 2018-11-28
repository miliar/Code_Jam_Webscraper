#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

const int P = 10007;
const int NIL = (-1);
const int INF = 1000*1000*1000+10;
const long long LINF = (long long)(INF)*(long long)(INF)+10LL; 

typedef unsigned U;
typedef long long LL;
typedef long double LD;
typedef unsigned long long UL;

typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<long long> VL;
typedef pair<int,int> PI;
typedef VI::iterator VIT;
typedef VL::iterator VLT;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,b,e) for (int i=(b); i<=(e); i++)
#define FORD(i,b,e) for (int i=(b); i>=(e); i--)
#define FORALL(i,c) for (__typeof(c.begin()) i=(c.begin()); i!=c.end(); i++)
#define FOREACH FORALL
#define SIZE(c) ((int)(x.size()))
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

LL gcd(LL a, LL b) { return b ? gcd(b,a%b) : a; }
LL binpow(LL a, LL d, LL mod)
{
	if (!d) return 1;
	static LL tmp = binpow(a,d/2,mod);
	tmp = (tmp * tmp) % mod;
	return d&1 ? (tmp*a)%mod : tmp;
}
#define rev_prime(a,p) binpow(a,p-2,p)
#define coprimes(a,b) (gcd(a,b)==1)

int BC(UL x) { return x ? 1+BC(x^(x&((~x)+1))) : 0; }
const int N = 1000;

bool c[N][N];
int d[N][N];
int h,w;

int rec(int x, int y)
{
	if (c[x][y]) return 0;
	if (x==h && y==w) return 1;
	if (x>=h) return 0;
	if (y>=w) return 0;
	if (d[x][y]!=NIL) return d[x][y];

	d[x][y] = (rec(x+1,y+2)+rec(x+2,y+1))%P;
	return d[x][y];
}




inline void single_case(int case_number)
{
	scanf("%d%d",&h,&w);
	int r;
	scanf("%d",&r);
	REP(i,1+h) REP(j,1+w) c[i][j]=0;
	while (r--)
	{
		int x,y;
		scanf("%d%d",&x,&y);
		c[x][y]=1;
	}
	REP(i,1+h) REP(j,1+w) d[i][j]=NIL;

	printf("Case #%d: ",case_number+1);
	printf("%d\n",rec(1,1));

}

int main()
{
	int j = 1;
	scanf("%d",&j);//*/
	REP(i,j) single_case(i);
	return 0;
}

