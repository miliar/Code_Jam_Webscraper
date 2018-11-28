#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>


#define vi vector<int>
#define ll long long
#define SZ(A) (int)(A).size()
#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define pb push_back

using namespace std;

int R, C;
vector<string> picture;

void imprime () {
}

void solve () {
  int otherR = 0, otherC = 0, sizeR = 0, sizeC = 0;
  
  FOR(i,0,R) {
    FOR(j,0,C) {
      if (picture[i][j] == '#') {
        if (i+1 == R || j+1 == C) {
          printf ("Impossible\n");
          return;
        }
        if (picture[i][j+1] != '#' || picture[i+1][j] != '#' || picture[i+1][j+1] != '#') {
          printf ("Impossible\n");
          return;
        }
        picture[i][j] = '/';
        picture[i][j+1] = '\\';
        picture[i+1][j] = '\\';
        picture[i+1][j+1] = '/';
      }
    }
  }
  
  FOR(i,0,R) {
    FOR(j,0,C) {
      printf ("%c", picture[i][j]);
    }
    printf("\n");
  }
}

int main () {
  int T;
  scanf("%d", &T);
  
  FOR (t,0,T) {
    scanf ("%d%d", &R, &C);
    picture = vector<string> (R);
    FOR(i,0,R) {
      char st[55];
      scanf ("%s", st);
      picture[i] = string(st);
      //printf ("%s\n", picture[i].c_str());
    }
    
    printf ("Case #%d:\n", t+1);
    solve ();
    imprime ();
  }
  return 0;
}

