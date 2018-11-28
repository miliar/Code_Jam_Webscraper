#include <stdio.h>
#include <iostream>

using namespace std;

int main(){
  int loop_num,N,S,P,t;
  //N:num of googlers, S:surprising, P:threshold, t:total

  string abc = "dadad";

  cin >> loop_num;
  

  for(int i=0;i<loop_num;i++){
    cin >> N >> S >> P;
    int count_num = 0;
    for(int j=0;j<N;j++){
      cin >> t;
      if(P+2*max(P-1,0)-1<t) count_num++;
      else if(P+2*max(P-2,0)-1<t && S>0){
	count_num++;
	S--;
      }
    }
    
    cout << "Case #" << (i + 1) << ": "<< count_num << endl;
    
  }
  
}
