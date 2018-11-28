#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>

#define REP(i, to) for(int i=0; i<to; i++)

using namespace std;
typedef unsigned int uInt;
typedef long long int llInt;

char M[64][64];
int R, C;

int main()
{
  int T;
  scanf("%d", &T);
  REP(t, T){
    scanf("%d%d", &R, &C);
    REP(r, R) scanf("%s", &M[r]);
    REP(r, R+1) M[r][C] = '.';
    REP(c, C+1) M[R][c] = '.';
    
    bool ok = true;
    REP(r, R) REP(c, C) {
      if(M[r][c]!='#') continue;
      
      if(M[r+1][c] != '#' || M[r+1][c+1] != '#' || M[r][c+1] != '#'){
        ok = false; 
      }
      M[r][c] = '/';
      M[r+1][c] = '\\';
      M[r+1][c+1] = '/';
      M[r][c+1] = '\\';
    }
    
    printf("Case #%d:\n", t+1);
    if(ok){
      REP(r, R) {
        REP(c, C){
          putchar(M[r][c]);
        }
        printf("\n");  
      }  
    }
    else{
      printf("Impossible\n");
    }
  }
  
  return 0;
}
