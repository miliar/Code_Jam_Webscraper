
#define _CRT_SECURE_NO_DEPRECATE 

#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 
#include <bitset>

using namespace std; 

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 1e-7
#define Pi 3.14159265358979

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PI;

struct Pos
{
	int x;
	int cnt;
} a[500];
int n;
int d;

bool can(Long T)
{
	Long prev=-(1LL<<52);

	REP(i,n)
	{
		Long p=max(prev+d,a[i].x-T);

		Long cur=p+1LL*(a[i].cnt-1)*d;

		Long lastD=cur-a[i].x;

		if (ABS(lastD) > T)
			return false;

		prev=cur;
	}

	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	cin>>T;
	REP(tests,T)
	{
		scanf("%d%d",&n,&d);
		REP(i,n)
		{
			scanf("%d%d",&a[i].x,&a[i].cnt);
			a[i].x*=2;
		}
		d*=2;

		Long Min=0;
		Long Max=1LL<<52;

		while (Max-Min>1)
		{
			Long cur=(Max+Min)>>1;

			if (can(cur))
				Max=cur; else
				Min=cur;
		}

		printf("Case #%d: ",tests+1);
		if (can(Min))
		{
			printf("%lld.%d\n",Min/2,5*(Min%2));
			continue;
		}

		if (can(Max))
		{
			printf("%lld.%d\n",Max/2,5*(Max%2));
			continue;
		}

		throw -1;
	}
	return 0;
}
