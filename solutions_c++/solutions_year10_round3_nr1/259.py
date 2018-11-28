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
      unsigned N;
      cin>>N; 
      int A[N], B[N];
      for(int nn=0;nn<N;nn++) cin>>A[nn]>>B[nn];
      unsigned inter=0;
      
      for(int ii=0;ii<N;ii++)
       for(int jj=ii+1;jj<N;jj++){
         if((double(B[ii]-B[jj])/double(A[jj]-A[ii]))>0) inter++;
        }               
          
     cout <<"Case #"<<cc<<": "<<inter<<endl;
     }    


} 
