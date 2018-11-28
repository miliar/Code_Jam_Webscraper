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

#define MAXN 105
bool field[2][MAXN][MAXN]; //[x][y]


int r;
int mxw,mxh;
bool flag;

void printit(int cur)
{
  for (int i=1;i<=mxh;i++) 
    {
      for (int j=1;j<=mxw;j++) 
        printf("%c", field[cur][j][i]+'0');
      printf("\n");
    }
}

int step(int cur)
{
  memset(field[!cur], false, sizeof(field[!cur]));
  flag=false;
  for (int i=1;i<=mxw;i++) 
    for (int j=1;j<=mxh;j++) 
      {
        field[!cur][i][j]=(field[cur][i][j] && (field[cur][i-1][j] || field[cur][i][j-1])) || 
          (field[cur][i-1][j] && field[cur][i][j-1]);
        flag|=field[!cur][i][j];
      }
  return (!cur);
}



bool testc(int tc)
{
  scanf("%i ", &r);
  
  memset(field, false, sizeof(field));
  mxh=mxw=0;
  FOR(i,0,r)
    {
      int x1,y1,x2,y2;
      scanf("%i %i %i %i ", &x1,&y1,&x2, &y2);
      FOR(j,x1,x2+1) FOR(k,y1,y2+1)
        {
          field[0][j][k]=1;
        }
      mxh=max(mxh, y2);
      mxw=max(mxw, x2);
    }
  int cur=0;
  //  printit(cur);
  int cnt=1;
  for(;;cnt++)
    {
      //  printf("---------------\n");
      cur=step(cur);
      //printit(cur);
      if (!flag) break;
    }
  printf("Case #%i: %i\n",tc,cnt);
}


int main()
{
  int t;
  scanf("%i ",&t);
  FOR(i,0,t)
    testc(i+1);
  
  return 0;
}
