
//Author Phinfinity
#include<iostream>
#include<cstdio>
#include<vector>
#include<cassert>
#include<sstream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<string>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<climits>
using namespace std;
#define pop_count(n) __builtin_popcount(n)
#define FOR(i,a,b) for(int i= (int)a; i< (int)b; ++i)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define ALL(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
#define MP make_pair

typedef pair<int,int> PI;
typedef vector<int> VI;
typedef long long LL;
#define INF 1000000000

char board[4][5];
char check_line(int sx, int sy, int dx, int dy) {
   char a[4];
   for (int i = 0; i < 4; i++) {
      a[i] = board[sx][sy];
      sx += dx;
      sy += dy;
   }
   int xcnt = 0, ocnt = 0, tcnt = 0;
   for (int i = 0; i < 4; i++)
      if (a[i] == 'X')
	 xcnt++;
   for (int i = 0; i < 4; i++)
      if (a[i] == 'O')
	 ocnt++;
   for (int i = 0; i < 4; i++)
      if (a[i] == 'T')
	 tcnt++;
   if (xcnt == 4 || (xcnt == 3 && tcnt == 1))
      return 'X';
   if (ocnt == 4 || (ocnt == 3 && tcnt == 1))
      return 'O';
   return '.';
}
bool is_draw() {
   for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
	 if(board[i][j] == '.')
	    return false;
   return true;
}
int main()
{
   int t;
   scanf("%d",&t);
   for (int tit = 1; tit <= t; tit++) {
      printf("Case #%d: ", tit);
      for (int i = 0; i < 4; i++)
	 scanf("%s", board[i]);
      char result[100];
      result[0] = 0;
      for (int i = 0; i < 4; i++) {
	 char r = check_line(i, 0, 0, 1);
	 if ( r == 'X')
	    sprintf(result, "X won");
	 else if ( r == 'O')
	    sprintf(result, "O won");
      }
      for (int i = 0; i < 4; i++) {
	 char r = check_line(0, i, 1, 0);
	 if ( r == 'X')
	    sprintf(result, "X won");
	 else if ( r == 'O')
	    sprintf(result, "O won");
      }
      char r = check_line(0, 0, 1, 1);
      if ( r == 'X')
	 sprintf(result, "X won");
      else if ( r == 'O')
	 sprintf(result, "O won");
      r = check_line(0, 3, 1, -1);
      if ( r == 'X')
	 sprintf(result, "X won");
      else if ( r == 'O')
	 sprintf(result, "O won");
      if(result[0] == 0) {
	 if(is_draw())
	    printf("Draw\n");
	 else
	    printf("Game has not completed\n");
      } else {
	 printf("%s\n",result);
      }
   }
   return 0;
}
