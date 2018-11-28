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
#define   max(a,b)    ((a)>(b)?(a):(b))
#define   min(a,b)    ((a)<(b)?(a):(b))
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(i=(a);i<(b);i++)
#define   REP(i,n)     rep(i,0,n)
#define   clr(a)      memset((a),0,sizeof (a));
#define   mabs(a)     ((a)>0?(a):(-(a))) 
#define   inf         1000000000
#define  MAXN      60
typedef __int64 int64;
FILE *fin;
FILE *fout;
__int64 shu[MAXN];
int M;
int N,K;
char cs[MAXN][MAXN];
char ncs[MAXN][MAXN];
char ts[MAXN];
char eds[MAXN][MAXN];
int dx[]={1,0,1,1};
int dy[]={0,1,-1,1};
void chuli()
{
    int i,j;
	for (i=N-1;i>=0;i--)
	{
		REP(j,N)
		{
			ncs[j][N-1-i]=cs[i][j];
		}
	}
//	REP(i,N) printf("%s\n",ncs[i]);
	REP(i,N)
	{
		REP(j,N) ts[j]='.';
		int top=N-1;
       for (j=N-1;j>=0;j--)
       {
		   if(ncs[j][i]!='.')
			   ts[top--]=ncs[j][i];
       }
       REP(j,N) eds[j][i]=ts[j];
	}
}
bool check(char c)
{
	int i,j,k,p;
    REP(i,N) REP(j,N)
	{
		REP(k,4)
		{
			int x=i,y=j;
			REP(p,K)
			{
				if(x<0||x>=N||y<0||y>=N) break;
				if(eds[x][y]!=c)
					break;
				x+=dx[k];y+=dy[k];
			}
			if(p==K)
			 return true;
		}
	}
	return false;
}
int main()
{
   	fin=fopen("A-large.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	fscanf(fin,"%d",&M);
    int rounds;
	for (rounds=1;rounds<=M;rounds++)
	{
		  fscanf(fin,"%d%d",&N,&K);
		  REP(i,N) fscanf(fin,"%s",cs[i]);
		  chuli();
		  bool fr=check('R');
		  bool fb=check('B');
		  if(fr&&fb)
		  {
               printf("Case #%d: Both\n",rounds);
               fprintf(fout,"Case #%d: Both\n",rounds);
		  }
		  else if(fr)
		  {
               printf("Case #%d: Red\n",rounds);
               fprintf(fout,"Case #%d: Red\n",rounds);
		  }
		  else if(fb)
		  {
               printf("Case #%d: Blue\n",rounds);
                fprintf(fout,"Case #%d: Blue\n",rounds);
		  }
		  else 
		  {
               printf("Case #%d: Neither\n",rounds);
                fprintf(fout,"Case #%d: Neither\n",rounds);
		  }
                
	}
	return 0;
}
