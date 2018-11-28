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
#define  MAXL     20
#define  MAXD     5010
#define  eps      1e-6
#define  MAXN      40
typedef __int64 int64;
FILE *fin;
FILE *fout;
char cs[MAXN][MAXN];
int N;
int64 shu[MAXN];
int64 yi=1;
int  solve()
{
	int i,j,k;
	int ret=0;
	REP(i,N)
	{
        for(j=i;j<N;j++)
		{
			if(shu[j]<(yi<<(i+1)))
				break;
		}
		for (k=j;k>i;k--)
		{
			swap(shu[k],shu[k-1]);
		}
		ret+=j-i;
	}
	return ret;
}
int main()
{
   	fin=fopen("A-large.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	int T;
	fscanf(fin,"%d",&T);
    int rounds;
	for (rounds=1;rounds<=T;rounds++)
	{
		  fscanf(fin,"%d",&N);
		  REP(i,N) fscanf(fin,"%s",cs[i]);
		  REP(i,N)
		  {
			  shu[i]=0;
			  REP(j,N)
			  {
                  if(cs[i][j]=='1') shu[i]|=(yi<<j);
			  }
		  }
		  int ret=solve();
		  printf("Case #%d: %d\n",rounds,ret);
          fprintf(fout,"Case #%d: %d\n",rounds,ret);
	}
}
