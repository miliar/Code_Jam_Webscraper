//#include<iostream>
#include<cstdio>
#include<cctype>
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
#define deb(A) A
/////////////////

#define MAX_N 50
#define MAX_M 50

int c,n,m,x1,x2,x3,y1,y2,y3;
LL a;

LL pole(LL x1, LL y1, LL x2, LL y2, LL x3, LL y3)
{
	return (y3-y1)*(x2-x1)-(x3-x1)*(y2-y1);
}

bool exist,f;

int main()
{
	scanf("%d",&c);
	REP(i,c)
	{
		scanf("%d%d%lld",&n,&m,&a);
		n++; m++;
		exist = false;
		f = true;
		REP(x,n)
			if(f)
			REP(y,m)
				if(f)
				REP(xx,n)
					if(f)
					REP(yy,m)
						if(pole(0,0,x,y,xx,yy)==a)
						{
							exist = true;
							f = false;
							x2=x; y2=y;
							x3=xx; y3=yy;
							break;
						}
		printf("Case #%d: ",i+1);
		if(exist)
			printf("%d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
