#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    int N;
    cin>>N;
    
    int res=0, lasto=1, lastb=1;
    int bo=0, bb=0;
    for(int i=0;i<N;++i){
      int p; char c;
      cin>>c>>p;
      
      if(c=='O'){ 
        bo -= abs(p-lasto);
        
        res += max(0,-bo)+1;
        bb += max(0,-bo)+1;
        
        bo=0;
        lasto = p;
      }
      else { 
        bb -= abs(p-lastb);
        
        res += max(0,-bb)+1;
        bo += max(0,-bb)+1;
        
        bb=0;
        lastb = p;
      }
      
    }

    
    cout<<"Case #"<<t<<": "<<res<<endl;
  }
  
  return 0;
}