#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>

#define REP(i, to) for(int i=0; i<to; i++)

using namespace std;
typedef unsigned int uInt;
typedef long long int llInt;

llInt L, t, N, C;
llInt M[1048576];
llInt A[1024];

llInt min(llInt a, llInt b){
  return (a<b)?a:b;  
}
llInt max(llInt a, llInt b){
  return (a>b)?a:b;  
}

void algorithm2(int test){
    llInt total_dist = 0;
    REP(i, N) total_dist += M[i];
    
    llInt result = total_dist * 2;
    llInt dist = 0;
    if(L==1) {
      REP(i, N){
        llInt cutdown = 0;
        if(dist*2 > t) cutdown = M[i];
        else if((dist+M[i])*2 > t){
          cutdown = dist + M[i] - (t >> 1);     
        }
        if(total_dist * 2 - cutdown < result){
          result = total_dist * 2 - cutdown;
          //cout << "Reduce dist2: " << M[i] << " by: " << cutdown << endl;  
        }
        dist += M[i];
      }
    }
    
    printf("Case #%d: %lld\n", test+1, result);
}

int main()
{
  int T;
  scanf("%d", &T);
  REP(test, T){
    priority_queue<llInt> PQ;
    scanf("%lld%lld%lld%lld", &L, &t, &N, &C);
    REP(i, C) scanf("%lld", &A[i]);
    REP(i, N) M[i]=A[i%C];
    
    //if(L<=1 && N<=1000) {
      //algorithm2(test);
      //continue;  
    //}
    
    llInt total_dist = 0;
    llInt total_cutdown = 0;
    llInt result_cutdown = 0; 
    REP(i, N) total_dist += M[i];
    llInt dist = total_dist;
    
    //For each first speed-upper. 
  if(L>0){
    for(int i=N-1; i>=0; i--){
      dist -= M[i];
      
      //if(t+1==38)
      //cout << "D: " << dist << " TC: " << total_cutdown << " M["<<i<<"]: " << M[i] << endl;
      
      llInt cutdown = 0;
      if(dist*((llInt)2) > t) cutdown = M[i];
      else {if((dist+M[i])*((llInt)2) > t){
        cutdown = dist + M[i] - (t >> 1);   
        //cout << "second: " << cutdown << endl;
      } else{
        //No cutdown, no speed up. 
        break;  
      }}
      
      if(total_cutdown + cutdown > result_cutdown){
        result_cutdown = total_cutdown + cutdown;
        //cout << "Reduce dist1: " << M[i] << " by: " << cutdown << endl;  
      }
        
      PQ.push(-M[i]);
      total_cutdown += cutdown;
      if(PQ.size() > L-1){
        total_cutdown -= -PQ.top();
        PQ.pop();  
      }
    }
  }
    
    llInt result = (total_dist << 1) - result_cutdown;
    printf("Case #%d: %lld\n", test+1, result);
  }
  return 0;
}
