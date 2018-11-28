#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;

int board[200][200];

int main() {
  int T;
  T = GETINT;
  FOR(test, T) {
    int r;
    r = GETINT;
    
    FOR(i, 200) FOR(j, 200) board[i][j] = 0;
    
    FOR(i, r) {
      int a, b, c, d;
      a = GETINT;
      c = GETINT;
      b = GETINT;
      d = GETINT;
      a--; b--; c--; d--;

      for(int j = a; j <= b; j++)
        for(int k = c; k <= d; k++)
          board[j][k] = 1;
    }

    int steps = 0;

    while(1) {

      // FOR(i, 10) {
      //   FOR(j, 10) fprintf(stderr, "%c", '0'+board[i][j]);
      //   fprintf(stderr, "\n");
      // }
      // fprintf(stderr, "---------------\n");


      bool hasBacteria = false;

      FOR(i, 200) FOR(j, 200) hasBacteria = hasBacteria || (board[i][j] > 0);

      if(!hasBacteria) break;
      steps++;

      for(int i = 200 - 1; i >= 0; i--)
        for(int j = 200 - 1; j >= 0; j--)
          if(board[i][j] == 1) {
            if( ((i == 0) || (board[i-1][j] == 0)) &&
                ((j == 0) || (board[i][j-1] == 0)))
              board[i][j] = 0;
          }
          else {
            if( ((i > 0) && (board[i-1][j] == 1)) &&
                ((j > 0) && (board[i][j-1] == 1)))
              board[i][j] = 1;            
          }
      
      // FOR(i, 200) FOR(j, 200) 
      //   if(board[i][j] == 2) board[i][j] = 1;
      //   else if(board[i][j] == 3) board[i][j] = 0;


    }
    printf("Case #%d: %d\n", 1+test, steps);
  }
  return 0;
}
