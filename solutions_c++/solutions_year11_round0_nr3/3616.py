#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main(){
  int T;
  cin >> T;
  for(int cases=1;cases<=T;++cases){
    int N;
    cin >> N;
    int C[N];
    int w=0;;
    
    for(int i=0;i<N;++i){
      cin >> C[i];
      w ^= C[i];
    }
    int m=C[0];
    if(w==0){
      for(int i=0;i<N;++i){
        m = min(m,C[i]);
        w += C[i];
      }
      w -= m;
      cout << "Case #"<<cases<<": "<<w << endl;
    }
    else{
      cout << "Case #"<<cases<<": "<<"NO" << endl;
    }
    
  }
  
  return 0;
}