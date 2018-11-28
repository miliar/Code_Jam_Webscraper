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

  int T, N, K;

  scanf("%d", &T);
  for(int t=0; t<T; t++){

    scanf("%d %d", &N, &K);
    std::string * matrix = new std::string[N];

    bool rwin=false, bwin=false;

    getchar();
    for(int n=0; n<N; n++){
      char prev='.';
      int count=0;
      for(int n2=0; n2<N; n2++){
        char c = getchar();
        if(c != '.'){
          matrix[n].insert(matrix[n].begin(), c);
          if(c==prev){
            count++;
          }
          else count=0;
          if(count>=K-1){
            if(c == 'R') rwin=true;
            else bwin=true;
          }
          prev=c;
        }

      }
      char c=getchar(); 
    }
  
    //std::cout << bwin << " " << rwin << "\n"; 

    if(!(bwin && rwin)){
      for(int i=0; i<N; i++){ 
      char prev='.'; int count=0;
        for(int n=0; n<N; n++){
          if(i>matrix[n].size()-1){
            count=0; prev='.'; continue;
          }
          if(matrix[n][i] == prev){
            count++;
          }else count=0;
          prev = matrix[n][i];
          if(count>=K-1){
            if(prev=='R') rwin=true;
            else if(prev=='B') bwin=true;
          }
        }
      } 
    }

    //std::cout << bwin << " " << rwin << "\n"; 

    if(!(bwin && rwin)){
       for(int i=-N; i<N;i++){
         int count=0; char prev='.';
         for(int n=0; n<N; n++){

            int pos = n+i;
            if(pos<0) continue;

            if(pos>matrix[n].size()-1){
              count=0; prev='.'; continue;
            }
            if(matrix[n][pos] == prev){
                count++;
            }else count=0;
            prev = matrix[n][pos];
            if(count>=K-1){
                if(prev=='R') rwin=true;
                else if(prev=='B') bwin=true;
            }
         }
       }
    }

    //std::cout << bwin << " " << rwin << "\n"; 

    if(!(bwin && rwin)){
       for(int i=N; i>=-N;i--){
         int count=0; char prev='.';
         for(int n=0; n<N; n++){

            int pos = N-n+i;
            if(pos<0) continue;

            if(pos>matrix[n].size()-1){
              count=0; prev='.'; continue;
            }
            if(matrix[n][pos] == prev){
                count++;
            }else count=0;
            prev = matrix[n][pos];
            if(count>=K-1){
                if(prev=='R') rwin=true;
                else if(prev=='B') bwin=true;
            }
         }
       }
    }

    //std::cout << bwin << " " << rwin << "\n"; 

    printf("Case #%d: ", t+1);

    if(rwin && bwin) printf("Both\n");
    else if(rwin) printf("Red\n");
    else if(bwin) printf("Blue\n");
    else printf("Neither\n");

    delete [] matrix;
  }

  return 0;

}
