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
#define  MAXN      17
typedef __int64 int64;
FILE *fin;
FILE *fout;
int N,K;
int prc[MAXN][26];
bool isok[1<<16];
int dp[1<<16];
bool cando(int i1,int i2)
{
	int i;
    REP(i,K-1)
	{
//		if(prc[i1][i]==prc[i2][i]) return false;
//		if(prc[i1][i+1]==prc[i2][i+1]) return false;
		if(prc[i1][i+1]<prc[i2][i+1]&&prc[i1][i]<prc[i2][i]) continue;
		if(prc[i1][i+1]>prc[i2][i+1]&&prc[i1][i]>prc[i2][i]) continue;
		return false;
	}
	return true;
}
int main()
{
   	fin=fopen("C-small-attempt1.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	int T;
	fscanf(fin,"%d",&T);
    int rounds;
	for (rounds=1;rounds<=T;rounds++)
	{
		  fscanf(fin,"%d%d",&N,&K);
		  clr(isok);
		  REP(i,N) REP(j,K) fscanf(fin,"%d",&prc[i][j]);
		  REP(i,N) isok[1<<i]=true;
		  REP(i,N) REP(j,i)
		  {
			  if(cando(i,j))
			   isok[(1<<i)|(1<<j)]=true;
		  }
		  REP(i,1<<N)
		  {
			  if(i<2) continue;
			  REP(j,N)
			  {
				  if(i&(1<<j)) break;
			  }
			  bool flag=isok[i^(1<<j)];
			  int t=j;
              for (++j;j<N;j++)
              {
                  if(i&(1<<j))
				  {
					  if(!isok[(1<<t)|(1<<j)])
						  flag=false;
				  }
              }
			  if(flag) isok[i]=true;
		  }
		  REP(i,1<<N) dp[i]=inf;
		  dp[(1<<N)-1]=0;
		  REP(i,1<<N)
		  {
			  if(!isok[i]) continue;
			  for (j=(1<<N)-1;j>=0;j--)
			  {
				  if(j<i) break;
				  if((j&i)!=i) continue;
				  dp[j^i]=min(dp[j^i],dp[j]+1);
			  }
		  }
		  int ret=dp[0];
		  printf("Case #%d: %d\n",rounds,ret);
          fprintf(fout,"Case #%d: %d\n",rounds,ret);
	}
}
