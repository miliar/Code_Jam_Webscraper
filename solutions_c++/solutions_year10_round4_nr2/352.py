#include <assert.h>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string>
#include <list>
#include <stack>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <list>
#define INF 0x3fffffff


typedef long long ll;
#define PII pair<int, int>
#define PLL pair<ll, ll>
#define PDD pair<double, double>
#define PIL pair<int, ll>
#define PLI pair<ll, int>
#define PID pair<int, double>
#define PDI pair<double, int>
#define PLD pair<ll, double>
#define PDL pair<double, ll>

#define PQ(x) priority_queue< x >  //highest first
#define PQR(x) priority_queue< x , vector< x > , greater < x > > //lowest first
#define V(x) vector< x > 
#define L(x) list< x > 
#define MP make_pair
#define PB push_back
#define IT(x) for (typeof((x).begin()) it = (x).begin() ; it != (x).end() ; it++)
#define IT2(x) for (typeof((x).begin()) it2 = (x).begin() ; it2 != (x).end() ; it2++)
#define FOR(i, a, b) for (int i = (a) ; i< (b) ; i++)
#define DEB(x...) fprintf(stderr,x);
//#define DEB

using namespace std;

#define MAXP 13
#define MAXN (1<<MAXP)
int M[MAXN];
int n,p;

int price[MAXP][MAXN]; //round
ll dp[MAXP][MAXN][MAXP]; //round
ll inft=10000000000ll;

bool testc(int tc)
{
  scanf("%i", &p);
  n=(1<<p);
  FOR(i,0,n)
    scanf("%i ", M+i);

  int a=(1<<(p-1));
  FOR(i,1,p+1)
    {
      FOR(j,0,a)
        scanf("%i ", &price[i][j]);
      a/=2;
    }

  FOR(i,0,n)  
    {
      for (int j=0;j<=M[i];j++)
        dp[0][i][j]=0;

      for (int j=M[i]+1;j<p+3;j++)
        dp[0][i][j]=inft;
    }
  
  a=(1<<(p-1));
  FOR(i,1,p+1)
    {
      FOR(j,0,a)
        {
          int t1=2*j,t2=2*j+1;
          
          for (int k=0;k<p+3;k++)
            dp[i][j][k]=price[i][j] + dp[i-1][t1][k] + dp[i-1][t2][k];
          for (int k=0;k<p+2;k++)
            dp[i][j][k]=min(dp[i][j][k], dp[i-1][t1][k+1] + dp[i-1][t2][k+1]);

          
          for (int k=0;k<p+2;k++)
            if (dp[i][j][k]>dp[i][j][k+1])assert(false);
          
            //DEB("dp[%i][%i][%i]=%lli\n", i, j, k, dp[i][j][k]);
        }

      a/=2;
    }
  printf("Case #%i: %lli\n", tc,dp[p][0][0]);
}


int main()
{
  int t;
  scanf("%i ",&t);
  FOR(i,0,t)
    testc(i+1);
  
  return 0;
}
