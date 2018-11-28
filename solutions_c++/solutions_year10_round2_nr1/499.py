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

//External
//#include <gmpxx.h>

using namespace std;

int main(int argc, char * argv[]){

  int T, N, M;

  scanf("%d", &T);
  for(int t=0; t<T; t++){

    scanf("%d %d\n", &N, &M);
    std::map<std::string, bool> dirs;
 
    for(int n=0; n<N; n++){
      char dir[101];
      scanf("%s\n", dir);
      dirs[dir] = true;
    }

    int count=0;

    for(int m=0; m<M; m++){
    
      char dir[101];
      scanf("%s\n", dir);
    
      for(int i=1; i<101; i++){
        if(dir[i] == '/' || dir[i] == '\0'){
           //std::cout << std::string(dir, 0, i) << "\n";;
           if(dirs.find(std::string(dir, 0, i)) == dirs.end()){
             dirs[std::string(dir, 0, i)] = true;
             count++;
           }
        }
        if(!dir[i]) break;
      }
    }

    printf("Case #%d: %d\n", t+1, count);

  }

  return 0;

}
