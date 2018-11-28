#include <iostream>
#include <string>
#include <cmath>
using namespace std;
typedef unsigned long long ULL;
typedef long long LL; 


int main(){
     unsigned cas;
     cin >> cas;
     
     for(int cc=1;cc<=cas;cc++){
      LL L,P,C;
      cin>>L>>P>>C;
      LL tmp=L;
      LL pwr=0;
      while(tmp<P){tmp*=C; pwr++;}
          
     cout <<"Case #"<<cc<<": "<< ceil(log2(pwr))<<endl;
     }    


} 
