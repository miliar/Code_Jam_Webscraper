#include<iostream>
#include<algorithm>
#include<string.h>
#include <vector>
#include<queue>  
#include<cstdio>
using namespace std;

class State{  
public:  
  int index,number;  
         
  State( int index=0, int number=0): index(index), number(number){}  

};  



int main(){

  
  int T;
  cin >> T;

  for(int i=0;i<T; ++i){
    long long  R,k;
    int N;
    queue<State> SQ;
    cin >> R >> k >> N;
       

    for(int j=0;j<N; ++j){
      int temp;
      cin >> temp;
      SQ.push( State(j,temp));
    }

    int memo[1000];
    int next[1000];
    int mask[1000];

    memset(memo,-1,sizeof(memo));
    memset(next,-1,sizeof(next));
    memset(mask,0,sizeof(mask));

    int sum=0;
    int index;
    
    index=SQ.front().index;
    
    while(1){

      if(sum+SQ.front().number <=k){
        if(mask[SQ.front().index] == 0){
          State buf = SQ.front(); SQ.pop();
          
          //mask shori
          mask[buf.index] = 1;

          sum=sum+buf.number;
          SQ.push(buf);

        }else{
          if (memo[index] > -1)
            break;
          memo[index] = sum;
          sum=0;
          next[index]=SQ.front().index;
          index=SQ.front().index;
          
          memset(mask,0,sizeof(mask));
        }
               
      }else{
        if(memo[index] < 0){
          memo[index] = sum;
          sum=0;
          next[index]=SQ.front().index;
          //
          //
          index=SQ.front().index;
          memset(mask,0,sizeof(mask));
        }else{
          break;
        }

        
      }
    }
    
    index=0;
    sum=0;
    for(int x=0;x<R ; ++x){
      sum=sum+memo[index];
      index=next[index];

    }
    cout << "Case #"<<i+1<<": "<< sum<<endl;
  }
  return 0;
}
