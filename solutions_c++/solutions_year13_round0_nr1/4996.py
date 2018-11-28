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
#define  MAXN     5
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
int T,N,M;
char cs[MAXN][MAXN];
bool isdraw()
{
    REP(i,4)REP(j,4) if(cs[i][j]=='.') return false;
    return true;
}
bool dui0(char c)
{
    int cntc=0,cntt=0;
    REP(i,4) if(cs[i][i]==c) cntc++;else if(cs[i][i]=='T') cntt++;
    if(cntc==4||cntc==3&&cntt==1) return true;
    return false;
}
bool dui1(char c)
{
    int cntc=0,cntt=0;
    REP(i,4) if(cs[3-i][i]==c) cntc++;else if(cs[3-i][i]=='T') cntt++;
    if(cntc==4||cntc==3&&cntt==1) return true;
    return false;
}
bool testit(char c)
{
    REP(i,4)
    {
        int cntc=0,cntt=0;
        REP(j,4) if(cs[i][j]==c) cntc++;else if(cs[i][j]=='T') cntt++;
        if(cntc==4||cntc==3&&cntt==1) return true;
    }
    REP(i,4)
    {
        int cntc=0,cntt=0;
        REP(j,4) if(cs[j][i]==c) cntc++;else if(cs[j][i]=='T') cntt++;
        if(cntc==4||cntc==3&&cntt==1) return true;
    }
    if(dui0(c)) return true;
    if(dui1(c)) return true;
    return false;
}
int main()
{
   	fin=fopen("A-large.in","r");
	fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
    	rep(rds,1,T+1)
	{
         	 printf("Case #%d: ",rds);
          	fprintf(fout,"Case #%d: ",rds);
		  REP(i,4)  fscanf(fin,"%s",cs[i]);
		  if(testit('X'))
		  {
		      fprintf(fout,"X won\n");
            printf("X won\n");
		  }
		  else if(testit('O'))
		  {
		      fprintf(fout,"O won\n");
            printf("O won\n");
		  }
		  else if(isdraw())
		  {
		      fprintf(fout,"Draw\n");
            printf("Draw\n");
		  }
		  else
		  {
		       fprintf(fout,"Game has not completed\n");
            printf("Game has not completed\n");
		  }
	}
}
