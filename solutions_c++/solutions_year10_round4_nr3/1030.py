#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <list>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <string.h>

//External
//#include <gmpxx.h>

using namespace std;

int main(int argc, char * argv[]){

  int C, R;
  int size=101;
  bool matrix[size*size];
  bool matrix2[size*size];

  scanf("%d", &C);
  for(int c=0; c<C; c++){
    memset(matrix, 0, size*size*sizeof(bool));
    scanf("%d", &R);
    for(int r=0; r<R; r++){
 
      int x1, y1, x2, y2;
      scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
      for(int y=y1; y<=y2; y++){
        memset(matrix+(y*size+x1), 1, (x2-x1+1)*sizeof(bool));
      }

    }
 
    int s=0;
    while(true){
      bool * mp = matrix; bool * nmp = matrix2;
      if(s%2 != 0){
        memcpy(matrix, matrix2, size*size*sizeof(bool)); 
      }else{
        mp=matrix2; nmp=matrix;
        memcpy(matrix2, matrix, size*size*sizeof(bool));
      }
      /*for(int i=0; i<10; i++){
        for(int j=0; j<10; j++){
          std::cout << mp[i*size+j];
        }
        std::cout << "\n";
      }*/

      bool alive=false; 
      for(int y=0; y<size; y++){
        for(int x=0; x<size; x++){
          if(mp[y*size+x]){
            alive=true;
            if((!y || !nmp[(y-1)*size+x]) && (!x || !nmp[y*size+x-1])){
              mp[y*size+x] = 0;
            }
          }else{
            if((y && nmp[(y-1)*size+x]) && (x && nmp[y*size+x-1])){
              mp[y*size+x] = 1;
            }
          }
        }
      }
      if(!alive) break;
      s++;
    }
  
    printf("Case #%d: %d\n", c+1, s);

  }

  return 0;

}
