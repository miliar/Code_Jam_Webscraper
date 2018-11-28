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

#define MAX_W 100
#define MAX_H 100

int P[MAX_W][MAX_H],r,c,w,h,n,x,y,X[]={2,1},Y[]={1,2};
bool A[MAX_W][MAX_H];

bool exist(int x, int y)
{
	return x>=0 && x<h && y>=0 && y<w && A[x][y];
}

int main()
{
	scanf("%d",&n);
	REP(i,n)
	{
		scanf("%d%d%d",&h,&w,&r);
		REP(j,h)
			REP(k,w)
			{
				P[j][k]=0;
				A[j][k]=true;
			}
		REP(j,r)
		{
			scanf("%d%d",&x,&y);
			x--; y--;
			A[x][y]=false;
		}
		P[h-1][w-1]=1;
		FDN(k,w-1,0)
			FDN(j,h-1,0)
				if(A[j][k])
					REP(l,2)
						if(exist(j+X[l],k+Y[l]))
							P[j][k]=(P[j][k]+P[j+X[l]][k+Y[l]])%10007;
		deb(REP(j,w)REP(k,h)printf("%d%c",P[j][k],(k+1<h?' ':'\n')););
		printf("Case #%d: %d\n",i+1,P[0][0]);
	}
	return 0;
}
