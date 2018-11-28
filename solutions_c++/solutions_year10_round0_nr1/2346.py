#include <iostream>
using namespace std; 

int main(){
    unsigned cas;
    cin >> cas;
    for(unsigned cc=1;cc<=cas;cc++){
      unsigned N;
      unsigned long long K;
      cin>>N>>K;
      bool *pwr = new bool[N];
      bool *st  = new bool[N];
      for(unsigned t=0;t<N;t++){
        pwr[t] = 0;
        st[t]  = 0;
      }
      pwr[0] = 1; 
      
      for(unsigned long long clk=0;clk<K;clk++){
          for(unsigned  t=0;t<N;t++){
             if(pwr[t]==1){
                  st[t] = !st[t]; //toggle
             }    
             if(t>0){
               pwr[t] = pwr[t-1] & st[t-1];
             }
             //optimistion.. if next flop cant be powered on & was not powered on, 
             //no need to go further down the link
             if(t!=(N-1) && !(pwr[t] & st[t]) && !pwr[t+1]) break;                                         
          }
      }
    if(pwr[N-1]&st[N-1])
      cout <<"Case #"<<cc << ": "<<"ON"<<endl;
    else 
      cout <<"Case #"<<cc << ": "<<"OFF"<<endl;
    delete(pwr);
    delete(st);      
    }
}
