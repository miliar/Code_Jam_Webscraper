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

using namespace std;

int gi() {  int t;  scanf("%i ", &t); return t; }
ll gll() {  ll t;  scanf("%lli ", &t); return t; }
double gd() {  double t;  scanf("%lf ", &t); return t; }

#define MAXW 102
#define MAXH 102

int height[MAXW][MAXH]; //[x][y];
char res[MAXW][MAXH]; //[x][y]
int dx[]={0, -1, 1, 0};
int dy[]={-1, 0, 0, 1};
int h,w;

void to(int fx, int fy, int &tx, int &ty)//from, to
{
  int lst = INF;
  tx=ty=-1;
  FOR(i,0,4)
    {
      int nx,ny;
      nx = fx + dx[i];
      ny = fy + dy[i];
      if (nx<0 || nx>=w || ny<0 || ny>=h)
          continue;
          
      if (height[nx][ny] >= height[fx][fy])
        continue;
      
      if (height[nx][ny] < lst)
        {
          tx = nx;
          ty = ny;
          lst = height[nx][ny];
        }
    }
}

char cur;
void dfs(int x,int y)
{
  //  printf("%i %i\n",x,y);
  if (x<0 || y<0 || x>=w || y>=h)
    return;
  if (res[x][y]!='-')
    return;

  res[x][y] = cur;
  
  int nx,ny;
  to(x,y,nx,ny);
  dfs(nx,ny);

  int tx,ty;
  FOR(i,0,4)
    {
      nx = x + dx[i];
      ny = y + dy[i];
      to(nx,ny,tx,ty);
      if (tx != x || ty != y)
        continue;
        
      dfs( nx,ny );
    }
}


void testc(int tc)
{
  scanf("%i %i ", &h, &w);
  FOR(y,0,h)
    FOR(x,0,w)
    scanf("%i ", & (height[x][y]));
  
  cur = 'a';
  memset(res,'-',sizeof(res));

  FOR(y,0,h)
    FOR(x,0,w)
    if (res[x][y] == '-')
      {
        dfs(x,y);
        cur++;
      }

  printf("Case #%i:\n",tc);
  FOR(y,0,h)
    {
      printf("%c", res[0][y]);
      FOR(x,1,w)
        printf(" %c", res[x][y]);
      printf("\n");
    }
}


int main()
{
  int tc;
  scanf("%i ", &tc);
  FOR(i,0,tc)
    testc(i+1);
  return 0;
}
