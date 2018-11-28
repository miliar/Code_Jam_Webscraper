#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string.h>
using namespace std;
char mass[4][4];
int check(char c){
    bool f = true,f1=true,f0=false;
    for(int i = 0;i< 4; i ++){
      bool f2=true,f3 = true;
      for(int j = 0;j < 4;j ++){
        if(mass[i][j] == '.'){
          f0 = true;
        }
        if(mass[i][j] != c && mass[i][j] != 'T'){
          f2 = false;
          //break;
        }
        if(mass[j][i] != c && mass[i][j] != 'T'){
          f3 = false;
        }
      }
      if(f2 || f3){
        return 1;
      }
      if(mass[i][i] != c && mass[i][i] != 'T'){
        f = false;
      }
      if(mass[i][3-i] != c && mass[i][3-i] != 'T'){
        f1 = false;
      }
    }
    if(f1||f){
      return 1;
    }
    if(f0){
      return -1;
    }
    return 0;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    char c;
    scanf("%c",&c);
    for(int i = 0;i < n; i ++){
      for(int j = 0; j < 4; j ++){
        scanf("%c%c%c%c%c",&mass[j][0],&mass[j][1],&mass[j][2],&mass[j][3],&c);
      }
      scanf("%c",&c);
      int ans = check('X');
      if(ans == 1){
        printf("%s%d%s\n","Case #",i+1,": X won");
        continue;
      }
      int ans2 = check('O');
      if(ans2 == 1){
        printf("%s%d%s\n","Case #",i+1,": O won");
        continue;
      }
      if(ans == -1 && ans2 == -1){
        printf("%s%d%s","Case #",i+1,": Game has not completed\n");
        continue;
      }
      printf("%s%d%s\n","Case #",i+1,": Draw");
    }
}
