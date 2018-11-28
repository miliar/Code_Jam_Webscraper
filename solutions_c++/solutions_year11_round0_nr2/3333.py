#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <stdio.h>
#include <string.h>
#include <vector>

int main(){

  int T;
  scanf("%d\n", &T);

  for(unsigned int c=1; c<=T; ++c){
 
    int N; 
    scanf("%d ", &N);

    char combs[26][26];
    memset(combs, 0, sizeof(combs));

    for(int i=0; i<N; ++i){
      //read in 3 char string for combination
      char a,b,c;
      scanf("%c%c%c ", &a, &b, &c);
      a-='A'; b-='A';
      combs[a][b] = c; combs[b][a] = c;
    }

    scanf("%d ", &N);
    std::vector<char> opps[26];

    for(int i=0; i<N; ++i){
      //read in 2 char string for opposition
      char a,b;
      scanf("%c%c ", &a, &b);
      a-='A'; b-='A';
      opps[a].push_back(b);
      opps[b].push_back(a);

    }

    char buffer[1028];
    scanf("%d ", &N);
    scanf("%s\n", buffer);

    //N characters, giving invocation;

    short elements[26];
    memset(elements, 0, sizeof(short)*26);

    for(int i=0; i<N; ++i){
   
      //Combination first, 26*26 boolean map, lookup last 2, if its in there, combine
      if(i && buffer[i-1]){
        if(combs[buffer[i]-'A'][buffer[i-1]-'A'] != 0){
          --elements[buffer[i-1]-'A'];
          buffer[i] = combs[buffer[i]-'A'][buffer[i-1]-'A'];
          buffer[i-1] = '\0';
        }
      } 

      //Opposition - if no combination, look up oppositions from list and check element list
      bool opped = false;
      if(i && buffer[i-1]){
        for(std::vector<char>::iterator iter = opps[buffer[i]-'A'].begin(); iter != opps[buffer[i]-'A'].end(); ++iter){
          if(elements[*iter]){
            //Clear
            //std::cout << "clear " << i << " " <<  ((char)(*iter+'A')) << buffer[i] << "\n";
            memset(elements, 0, sizeof(short)*26);
            memset(buffer, 0, i+1);
            opped = true;
            break;
          }
        }
        
      } 
  
      if(!opped) ++elements[buffer[i]-'A'];

    }

    bool printed = false;
    //unsigned int answer = std::max(time[0], time[1]);
    std::cout << "Case #" << c << ": [";
    for(int i=0; i<N; ++i){
      if(buffer[i]){
        if(printed) std::cout << ", ";
        std::cout << buffer[i];
        printed = true;
      }
    }
    std::cout << "]\n";
 
  }

}



