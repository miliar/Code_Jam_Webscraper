#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>
using namespace std;
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(int i=(a);i<(int)(b);i++)
#define   per(i,a,b)  for(int i=((a)-1);i>=(int)(b);i--)
#define   PER(i,n)     per(i,n,0)
#define   REP(i,n)     rep(i,0,n)
#define   FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define   clr(a)      memset((a),0,sizeof (a))
#define   SZ(a)         ((int)((a).size()))
#define   CLEAR(a, v)    memset((a), (v), sizeof(a))
#define   ALL(v)          (v).begin(), (v).end()
#define   mabs(a)       ((a)>0?(a):(-(a)))
#define   inf         1000000001
#define  MAXN     561
#define  eps      1e-6
#define   PB push_back
#define   FI 		first
#define   SE 		second
#define   MP 		make_pair
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
typedef long long int64;
FILE *fin;
FILE *fout;
//int64 inf=100000000000000000LL;
int T,R,C,D;
char cs[MAXN][MAXN];
long double a[MAXN][MAXN];
long double bx[MAXN][MAXN];
long double cy[MAXN][MAXN];
long double sz[MAXN][MAXN];
int solve(int x,int y)
{
    int ret=0;
    for(int d=2;;d++)
    {
        int ex=x+d,ey=y+d;
        if(ex>R+1||ey>C+1) return ret;
        long double zx=(x+ex)/2.0,zy=(y+ey)/2.0;
        long double cshu=sz[ex][ey]-sz[ex][y-1]-sz[x-1][ey]+sz[x-1][y-1];
        long double beichux=bx[ex][ey]-bx[ex][y-1]-bx[x-1][ey]+bx[x-1][y-1];
        long double beichuy=cy[ex][ey]-cy[ex][y-1]-cy[x-1][ey]+cy[x-1][y-1];
        cshu-=a[x][y]+a[x][ey]+a[ex][y]+a[ex][ey];
        beichux-=a[x][y]*x+a[x][ey]*x+a[ex][y]*ex+a[ex][ey]*ex;
        beichuy-=a[x][y]*y+a[x][ey]*ey+a[ex][y]*y+a[ex][ey]*ey;
        beichux-=cshu*zx;
        beichuy-=cshu*zy;
        if(beichux>1||beichuy>1) continue;
        double t1=beichux,t2=beichuy;
        if(fabs(t1)<1e-8&&fabs(t2)<1e-8) ret=max(ret,d+1);
    }
    return ret;
}
int main()
{
   	fin=fopen("B-large.in","r");
	fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
    rep(rds,1,T+1)
	{
          printf("Case #%d: ",rds);
          fprintf(fout,"Case #%d: ",rds);
		  fscanf(fin,"%d%d%d",&R,&C,&D);
		  REP(i,R) fscanf(fin,"%s",cs[i]);
		  clr(a);clr(sz);
		  REP(i,R) REP(j,C) sz[i+1][j+1]=a[i+1][j+1]=cs[i][j]-'0'+D;
		  REP(i,R+2) REP(j,C+2) bx[i][j]=a[i][j]*i,cy[i][j]=a[i][j]*j;
		  rep(i,1,R+2) rep(j,1,C+2)
		  {
		      bx[i][j]=bx[i-1][j]+bx[i][j-1]-bx[i-1][j-1]+a[i][j]*i;
		      cy[i][j]=cy[i-1][j]+cy[i][j-1]-cy[i-1][j-1]+a[i][j]*j;
		      sz[i][j]=sz[i-1][j]+sz[i][j-1]-sz[i-1][j-1]+a[i][j];
		  }
		  int ret=0;
		  rep(i,1,R+2)rep(j,1,C+2)
		  {
		      int tret=solve(i,j);
		      ret=max(ret,tret);
		  }
		  if(ret<3)
		  {
            printf("IMPOSSIBLE\n");
            fprintf(fout,"IMPOSSIBLE\n");
		  }
		  else
		  {
            printf("%d\n",ret);
            fprintf(fout,"%d\n",ret);
		  }
	}
}
