#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define RESET(a,c) memset(a,(c),sizeof(a))
#define CT(mask,k) ( ((mask) >> (k)) & 1 )


template<class T> inline int BC(T x) {
	int ret = 0;
	for( ; x ; x &= x-1) ++ret;
	return ret;
}
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

int mem[1<<16][4][4];

int R, C, BASE_BC;
int f(int x, int y) { return x*C + y; }

int dx2[]={-1,-1,0,1,1,1,0,-1}, dy2[]={0,1,1,1,0,-1,-1,-1};
//czy pierwszy wygrywa
int go(int mask, int x, int y)
{ 
  int &ret = mem[mask][x][y];
  if(ret != -1) return ret;

//  int who = (BC(maks) - BASE_BC ) % 2;
  
  int found = 0;
  REP(i, 8) {
    int nx = x + dx2[i], ny = y + dy2[i];
    if(nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
    if( CT(mask, f(nx, ny))) continue;
    
    found = max( found, 1-go(mask | (1<<f(nx,ny)), nx, ny));
  }
  
  ret = found;
  return ret;
}
void solve(void)
{
  scanf("%d %d\n", &R, &C);
  char buff[3000];
  int st = 0;
  int sx = -1, sy = -1;
  REP(i, R) {
    gets(buff);
    REP(j, C) if(buff[j] == '#' || buff[j] == 'K') {
      st |= (1<<f(i,j));
      if(buff[j] == 'K') sx = i, sy = j;
   }
  }
  RESET(mem,-1);
  BASE_BC = BC(st);
  printf("%c\n", (go(st, sx, sy) == 1) ? 'A' : 'B');

}

int main(void)
{
	int T, C = 1;
	scanf("%d", &T);
	while(T--) { printf("Case #%d: ",C++); solve(); }
	return (0);
}
