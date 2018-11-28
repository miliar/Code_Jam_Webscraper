#include <cstdio>
#include <string>
#include <iostream>  
using namespace std;

char tab [4][4];

bool check(char symbol){  
  int i, j;
  bool ok,test;
  ok = false;
  for (i = 0; i < 4; ++i){
    test = true;
    for (j = 0; j < 4; ++j){
      if (!((tab[i][j] == 'T') || (tab[i][j] == symbol)))
        test = false;
    }
    if (test)
      ok = true;
  }
  
  if (!ok)
  for (i = 0; i < 4; ++i){
    test = true;
    for (j = 0; j < 4; ++j){
      if (!((tab[j][i] == 'T') || (tab[j][i] == symbol))){
        test = false;
      }
      
    }
    if (test)
      ok = true;
  }


  if (!ok){
    test = true;
    for (i = 0; i < 4; ++i){
      if (!((tab[i][i] == 'T') || (tab[i][i] == symbol)))
        test = false;
    }  
    if (test)
    ok = true;
  }
  
  
  if (!ok){
    test = true;
    for (i = 0; i < 4; ++i){
      if (!((tab[3-i][i] == 'T') || (tab[3-i][i] == symbol)))
        test = false;
    }  
    if (test)
    ok = true;
  }
  
  return ok;
}


int main(){
  int T, i, j,t;
  scanf("%d", &T);
  char c;
  bool nie, draw;
  scanf("%c", &c);
  for (t = 1; t <= T; t++){
    for (i = 0; i < 4; ++i){
      for ( j = 0; j < 4; ++j){
        scanf("%c", &c);
        tab[j][i] = c;
      }
      scanf("%c", &c);
    }
    scanf("%c", &c);

/*
    for (i = 0; i < 4; ++i){
      for ( j = 0; j < 4; ++j){
        printf("%c", tab[j][i]);
       
      }
      printf("\n");
    }
    */
    
    nie = false;
    if (check ('X'))
    printf("Case #%d: X won\n",t);
    else{
      if (check ('O'))
        printf("Case #%d: O won\n",t);    
      else
        nie = true;
    }
    
    if (nie){
      draw = false;
      for (i = 0; i < 4; ++i){
        for ( j = 0; j < 4; ++j){
          if (tab[j][i] == '.')
            draw = true;
        }

      }
      if (draw)
        printf("Case #%d: Game has not completed\n",t); 
      else
        printf("Case #%d: Draw\n",t); 
    }
  }
  return 0;
}
