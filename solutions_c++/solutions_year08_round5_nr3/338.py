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

#define MAX_N 10
#define MAX_M 10
#define INF 1000000000

int n,m,c,res,X[]={-1,-1,1,1},Y[]={0,-1,-1,0},D[1<<12][20];
bool P[MAX_N][MAX_M],ok;
char z;

bool exist(int x,int y)
{
	return x>=0 && x<n && y>=0 && y<m;
}

void REK(int x, int mas, int masn, int p2, int s, int p)
{
	//deb(printf("x=%d p=%d s=%d\n",x,p,s););
	if(x==n)
	{
		deb(printf("mas=%d masn=%d s=%d Dn=%d D=%d\n",mas,masn,s,D[masn][p],D[mas][p-1]););
		D[masn][p] = MAXX(D[masn][p],D[mas][p-1]+s);
		return;
	}
	if(!P[x][p-1])
	{
		REK(x+1,mas,masn,p2>>1,s,p);
		return;
	}
	ok = true;
	if(x>0)
		ok &= (((mas&(p2<<1))==0) && ((masn&(p2<<1))==0));
	if(x+1<n)
		ok &= (((mas&(p2>>1))==0));
	//deb(printf("ok=%d\n",ok););
	if(ok)
		REK(x+1,mas,masn+p2,p2>>1,s+1,p);
	REK(x+1,mas,masn,p2>>1,s,p);
}

int main()
{
	scanf("%d",&c);
	REP(t,c)
	{
		scanf("%d%d\n",&m,&n);
		REP(i,m)
		{
			REP(j,n)
			{
				z=getchar();
				P[j][i]=(z=='.');
			}
			scanf("\n");
		}
		//deb(REP(i,m){REP(j,n)printf("%d",P[j][i]);printf("\n");});
		REP(i,m+1)
			REP(j,1<<n)
				D[j][i]=0;
		FUP(i,1,m)
			REP(j,1<<n)
				REK(0,j,0,1<<(n-1),0,i);
		deb(REP(i,m+1){printf("i=%d\n",i);REP(j,1<<n)printf("D[%d][%d]=%d\n",j,i,D[j][i]);});
		res=0;
		REP(j,1<<n)
			res=MAXX(res,D[j][m]);
		printf("Case #%d: %d\n",t+1,res);
	}
	return 0;
}
