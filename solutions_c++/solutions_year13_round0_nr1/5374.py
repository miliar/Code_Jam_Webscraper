#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

int isWinning(char play, char tab[][5]){
  int ponto = 0;
  int flag;
  for(int i =0;i< 4;i++){
    flag = 0;
    for(int k =0;k<4;k++){
      if(tab[i][k] == '.'){
	ponto = 1;
	flag = 1;
	break;
      }
      if((tab[i][k] != play && tab[i][k] != 'T')){
	flag = 1;
	break;
      }
    }
    if(!flag)
      return 1;
    flag = 0;
    for(int k =0;k<4;k++){
      if((tab[k][i] != play && tab[k][i] != 'T')){
	flag = 1;
	break;
      }
    }
    if(!flag)
      return 1;
  }
  flag = 0;
  for(int k =0;k<4;k++){
    if(tab[k][k] != play && tab[k][k] != 'T'){
      flag = 1;
      break;
    }
  }
  if(!flag)
    return 1;
  flag = 0;
  for(int k =0;k<4;k++){
    if(tab[3-k][k] != play && tab[3-k][k] != 'T'){
      flag = 1;
      break;
    }
  }
  if(!flag)
    return 1;
  if(ponto)
    return 2;
    
  
  return 0;
}

int main(){
  int t;
  char tab[5][5];
  int k;
  
  scanf("%d", &t);
  
  for(int l = 0;l<t;l++){
    for(int j = 0;j<4;j++)
      scanf("%s", tab[j]);
    k = isWinning('O',tab);
    if(isWinning('X', tab) == 1)
      printf("Case #%d: X won\n", l+1);
    else if(k == 1)
      printf("Case #%d: O won\n", l+1);
    else if(!k)
       printf("Case #%d: Draw\n", l+1);
    else
	printf("Case #%d: Game has not completed\n", l+1);
      
    
    
    
  } 
  
  return 0;
}
