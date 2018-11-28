#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void solve(void){
  int R,C;
  char table[64][64];
  cin >> R >> C;
  for(int i=0; i<R; i++){
    for(int j=0; j<C; j++){
      cin >> table[i][j];
    }
  }

  for(int i=0; i<R-1; i++){
    for(int j=0; j<C-1; j++){
      if(table[i][j]!='#') continue;
      if((table[i][j+1]!='#') || (table[i+1][j]!='#') || (table[i+1][j+1]!='#')){
        printf("\nImpossible\n");
        return;
      }else{
        table[i][j] = '/';
        table[i][j+1] = '\\';
        table[i+1][j] = '\\';
        table[i+1][j+1] = '/';
      }
    }
  }

  for(int i=0; i<R; i++){
    if(table[i][C-1]=='#'){
       printf("\nImpossible\n");
       return;
    }
  }
  for(int j=0; j<C; j++){
    if(table[R-1][j]=='#'){
       printf("\nImpossible\n");
       return;
    }
  }

  printf("\n");
  for(int i=0; i<R; i++){
    for(int j=0; j<C; j++){
      printf("%c", table[i][j]);
    }
    printf("\n");
  }
}

int main(void){
  int testCaseCount;
  cin >> testCaseCount;
  for(int i=1; i<=testCaseCount; i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
