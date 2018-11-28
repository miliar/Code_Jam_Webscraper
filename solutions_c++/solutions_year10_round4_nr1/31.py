#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<string> VS;
const double pi=3.1415926535897932384626433832795;
const double eps=1e-8;

#define pb push_back
#define mp make_pair
#define sz size()
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((a),(b),sizeof(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)<(0)?-(a):(a))
#define HAS(x,k) ((x).find(k)!=(x).end())
#define sqr(a) ((a)*(a))
//#pragma comment(linker,"/STACK:200000000")

#define PREV(x) ((x)&((x)-1))
#define NEXT(x) (((x)<<1) - PREV(x))

char ch[1<<20];
string gs(){ scanf("%s",ch); return string(ch); }
string gl(){ gets(ch); return string(ch); }

int A[128][128];
int V[128][128];
int H[128][128];
int K;
int solve()
{
	int n=K*2-1;
	FOR(i,0,n) FOR(j,0,n)
	{
		int k=0;
		int ok=1;
		while(j-k>=0 && j+k<n && ok)
			if (A[i][j-k]!=-1 && A[i][j+k]!=-1 &&
				A[i][j-k]!=A[i][j+k]) ok=0;
			else ++k;
		H[i][j]=ok;
	}
	FOR(i,0,n) FOR(j,0,n)
	{
		int k=0;
		int ok=1;
		while(j-k>=0 && j+k<n && ok)
			if (A[j-k][i]!=-1 && A[j+k][i]!=-1 && 
				A[j-k][i]!=A[j+k][i]) ok=0;
			else ++k;
		V[i][j]=ok;
	}

	int best=1<<30;
	FOR(x,0,n) FOR(y,0,n)
	{
		int ok=1;
		FOR(k,0,n) if (!H[k][y]) ok=0;
		FOR(k,0,n) if (!V[k][x]) ok=0;
		if (ok)
		{
			int hh=K+ABS(n/2-x)+ABS(n/2-y);
			best=MIN(best,hh*hh-K*K);
		}
	}
	return best;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int tc=0; int t; scanf("%d",&t);
	while(t--)
	{
		++tc;
		CLR(A,-1);
		scanf("%d",&K);

		int p=K-1;
		int c=1;
		int pp=0;
		while(1)
		{
			FOR(i,0,c)
				scanf("%d",&A[pp][p+i*2]);
			if (c==K) break;
			++c; --p; pp++;
		}
		++pp;
		--c;
		++p;
		while(c>0)
		{
			FOR(i,0,c)
				scanf("%d",&A[pp][p+i*2]);
			--c; ++p; pp++;
		}
		
		printf("Case #%d: %d\n",tc,solve());
	}
	
	return 0;
}
