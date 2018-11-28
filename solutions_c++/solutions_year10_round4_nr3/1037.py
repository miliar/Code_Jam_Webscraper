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
#define  MAXN      100
typedef __int64 int64;
FILE *fin;
FILE *fout;
int N;
bool cs[MAXN][MAXN];
bool ncs[MAXN][MAXN];
bool isok(bool a[][MAXN])
{
    int i,j;
	REP(i,N) REP(j,N) if(a[i][j]) return false;
	return true;
}
void doit()
{
    int i,j;
	REP(i,N) REP(j,N)
	{
		ncs[i][j]=cs[i][j];
		if(cs[i][j])
		{
			if(i>0&&cs[i-1][j]||j>0&&cs[i][j-1]) continue;
			ncs[i][j]=false;
		}
		else
		{
            if(i>0&&cs[i-1][j]&&j>0&&cs[i][j-1])
				ncs[i][j]=true;
		}
	}
	REP(i,N) REP(j,N) cs[i][j]=ncs[i][j];
}
int main()
{
   	fin=fopen("C-small-attempt0.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	int T;
	fscanf(fin,"%d",&T);
    int rounds;
	N=100;
	for (rounds=1;rounds<=T;rounds++)
	{
		int R;
		  fscanf(fin,"%d",&R);
		  REP(i,R)
		  {
			  int x1,y1,x2,y2;
			  fscanf(fin,"%d%d%d%d",&x1,&y1,&x2,&y2);
			  x1--,x2--,y1--,y2--;
			  for (j=x1;j<=x2;j++)
			  {
				  for (k=y1;k<=y2;k++)
				  {
					  cs[j][k]=true;
				  }
			  }
		  }
		  int ret=0;
		  while (!isok(cs))
		  {
			  ret++;
			  doit();
		  }
                printf("Case #%d: %d\n",rounds,ret);
                fprintf(fout,"Case #%d: %d\n",rounds,ret);
	}
}
