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
#define  MAXM     (1<<7)  
#define  MAXN     510
#define  eps      1e-6
#define  MOD     10000
typedef __int64 int64;
FILE *fin;
FILE *fout;
char cs[MAXN];
char s[]="welcome to code jam";
int dp[MAXN][20];
int n;
int doit()
{
	clr(dp);
    dp[0][0]=1;
	int i,j;
	int m=strlen(cs);
	for (i=1;i<=m;i++)
	{
		REP(j,20) 
		{
			dp[i][j]+=dp[i-1][j];
           	while (dp[i][j]>=MOD) dp[i][j]-=MOD;
		}
		for (j=1;j<=19;j++)
		{
			if(cs[i-1]==s[j-1])
			{
				dp[i][j]+=dp[i-1][j-1];
				while (dp[i][j]>=MOD) dp[i][j]-=MOD;
			}
		}
	}
	int ret=dp[m][19];
    return ret;
}
int main()
{
   	fin=fopen("C-large.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	int N;
	n=strlen(s);
	fscanf(fin,"%d\n",&N);
    int rounds;
	for (rounds=1;rounds<=N;rounds++)
	{
		  fgets(cs,512,fin);
		  int ret=doit();
		  printf("Case #%d: %04d\n",rounds,ret);
          fprintf(fout,"Case #%d: %04d\n",rounds,ret);
	}
}
