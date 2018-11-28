#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>

#define D(x) cout << #x " is " << x << endl

using namespace std;

int main(){
  int T;
  scanf("%d", &T);
  int C = 1;
  while(T--){
    int N;
    scanf("%d", &N);
    vector<int>O;
    vector<int>B;
    vector<pair<char, int> >ALL(N);
    int button;
    char robot;
    
    int posO = 1, posB = 1, nextO = 0, nextB = 0;
    int res = 0;
    
    for(int i=0;i<N;++i){
      cin >> robot >> button;
      if(robot == 'O'){
        O.push_back(button);
      }else if(robot == 'B'){
        B.push_back(button);
      }
      ALL[i] = make_pair(robot, button);
    }
    
    for(int i=0;i<N;++i){
      int destB,distB,destO,distO;
      destB = distB = destO = distO = -1;
      if(nextB < B.size()){ 
        destB = B[nextB];
        distB = abs(destB - posB);
      }
      
      if(nextO < O.size()){ 
        destO = O[nextO];
        distO = abs(destO - posO);
      }
      
      //printf("Robot B is on %d has to go to %d distance %d\n", posB, destB, distB);
      //printf("Robot O is on %d has to go to %d distance %d\n", posO, destO, distO);
      
      // Se mueve B
      if(ALL[i].first == 'B'){
        int time = (distB + 1);
        res += time;
        nextB++;
        posB = destB;
        if(time >= distO){
          posO = destO;
        }else{
          if(posO < destO){
            posO += time;
          }else{
            posO -= time;
          }
        }
        //printf("Moved B to %d, took %d time, moved O to %d\n", posB, time, posO);
      }else{
        // Se mueve O
        int time = (distO + 1);
        res += time;
        nextO++;
        posO = destO;
        if(time >= distB){
          posB = destB;
        }else{
          if(posB < destB){
            posB += time;
          }else{
            posB -= time;
          }
        }
        //printf("Moved O to %d, took %d time, moved B to %d\n", posO, time, posB);
      }
      //puts("");
    }
    printf("Case #%d: %d\n", C++, res);
  }
}
