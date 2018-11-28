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
#define   inf         100000000
#define  MAXN      110
#define  MAXM      300
typedef __int64 int64;
FILE *fin;
FILE *fout;
int N,D,I,M;
int a[MAXN];
int dp[MAXN][MAXM];
int jisuan(int a,int b)
{
	if(a>b) swap(a,b);
	if(b-a<=M) return 0;
	if(M==0) return inf;
	int n=(b-a+M-1)/M;
	return (n-1)*I;
}
int main()
{
   	fin=fopen("B-small-attempt0.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	int T;
	fscanf(fin,"%d",&T);
	int rounds;
	for (rounds=1;rounds<=T;rounds++)
	{
		  fscanf(fin,"%d%d%d%d",&D,&I,&M,&N);
		  REP(i,N) fscanf(fin,"%d",&a[i+1]);
		  REP(i,MAXN) REP(j,MAXM) dp[i][j]=inf;
          REP(i,MAXM) dp[0][i]=0;
		  for (i=1;i<=N;i++)
		  {
			  REP(j,MAXM) dp[i][j]=min(dp[i][j],dp[i-1][j]+D);
			  REP(j,MAXM) REP(k,MAXM)
			  {
				  if(abs(j-k)<=M)
					  dp[i][j]=min(dp[i][j],dp[i-1][k]+abs(j-a[i]));
			  }
			  REP(k,MAXM)
			  {
				  j=a[i];
				  int v=jisuan(k,j);
				  dp[i][j]=min(dp[i][j],dp[i-1][k]+v);
			  }
		  }
		  int ret=inf;
		  REP(i,MAXM) ret=min(ret,dp[N][i]);
                printf("Case #%d: %d\n",rounds,ret);
                fprintf(fout,"Case #%d: %d\n",rounds,ret);
	}
	return 0;
}
