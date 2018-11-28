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

const int N = 11;
const U M = 1<<N;

int d[2][M];

bool is_ok(U a, U b)
{
	if (a==0) return 1;
	REP (i,N) if ((((a&(3<<i))==(3<<i)))) return 0;
	//	printf("isok %u %u\n",a,b);
	if (((a&1)>0)&&((b&2)>0)) return 0;
//	printf("semiok\n");
	FOR(i,1,N) if ((a&(1<<i))>0) if (((b&(1<<(i-1)))>0)||((b&(1<<(i+1)))>0)) return 0;
//	printf("OK!\n");
	return 1;
}

inline void single_case(int case_number)
{
	int n,m;
	scanf("%d%d",&m,&n);
	REP(i,M) d[0][i]=0;
	char w[M];
	FOR(i,1,m)
	{
		scanf("%s",w);
		REP(a,(1<<n)) d[i&1][a]=0;
		REP(a,(1<<n)) REP(b,(1<<n)) if (is_ok(a,b)) d[i&1][a]=max(d[i&1][a],__builtin_popcount(a)+d[1^(i&1)][b]);
		REP(a,(1<<n)) 
		{
			//printf("d[%d][%d]=%d\n",i,a,d[i&1][a]);

			REP(j,n) if (w[j]=='x' && ((a&(1<<j))>0)) d[i&1][a]=0;
//			printf("d[%d][%d]=%d\n",i,a,d[i&1][a]);
		}
	}
	int best = 0;
	REP(i,(1<<n)) best=max(best,d[m&1][i]);

	printf("Case #%d: ",case_number+1);
	printf("%d\n",best);
}

int main()
{
	int j = 1;
	scanf("%d",&j);//*/
	REP(i,j) single_case(i);
	return 0;
}

