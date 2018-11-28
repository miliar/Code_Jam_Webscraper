//#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include <memory.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef double DD;
typedef long double LD;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define VAR(V,init) __typeof(init) V=(init)
#define FUP(I,A,B) for(int I=(A);I<=(B);I++)
#define FDN(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define FALL(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define ALL(X) (X).begin(),(X).end()
#define CLE(a,b) memset(a,b,sizeof(a))
#define MINN(a,b) ((a)>(b)?(b):(a))
#define MAXX(a,b) ((a)<(b)?(b):(a))
#define PB push_back
#define PF push_front
#define CB pop_back
#define CF pop_front
#define MP make_pair
#define FI first
#define SE second
#define SZ(X) ((int)(X.size()))
#define deb(A) //A
/////////////////

#define MAX_M 100
#define MAX_N 500000

struct par
{
	LL v,ile;
	par(){}
	par(LL vv, LL iile)
	{
		v =vv;
		ile = iile;
	}
};

vector<par> D[MAX_N];

LL t,n,m,x,y,z,A[MAX_M],S[MAX_N],res;
int mm = 1000000007;

LL find(LL a, LL b)
{
	REP(u,SZ(D[a]))
		if(b == D[a][u].v)
			return u;
	return -1;
}

LL count(LL a, LL b)
{
	LL r = 0;
	REP(u,SZ(D[a]))
		if(b > D[a][u].v)
			r = (r+D[a][u].ile)%mm;
	return r;
}

int main()
{
	scanf("%lld",&t);
	REP(i,t)
	{
		scanf("%lld%lld%lld%lld%lld",&n,&m,&x,&y,&z);
		REP(j,m)
			scanf("%lld",&A[j]);
		FUP(j,0,n-1)
		{
			S[j]=A[j%m];
			A[j%m] = (x * A[j%m] + y * (j+1))%z;
		}
		REP(j,n+1)
			D[j].clear();
		D[0].PB(par(-1000000001ll,1));
		REP(j,n)
		{
			FDN(k,j+1,0)
			{
				LL cou = count(k,S[j]);
				LL f = find(k+1,S[j]);
				if(f == -1)
					D[k+1].PB(par(S[j],cou));
				else
					D[k+1][f].ile = (D[k+1][f].ile + cou) % mm;
			}
		}
		deb(REP(j,n)printf("%lld ",S[j]);printf("\n"););
		res = 0;
		deb(REP(j,n+1){printf("j=%d\n",j);REP(k,SZ(D[j]))printf("(%lld, %lld)\n",D[j][k].v,D[j][k].ile);});
		FUP(j,1,n)
			REP(k,SZ(D[j]))
				res = (res + D[j][k].ile) % mm;
		printf("Case #%d: %lld\n",i+1,res);
	}
	return 0;
}
