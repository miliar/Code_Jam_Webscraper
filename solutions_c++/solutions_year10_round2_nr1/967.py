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
      unsigned N, M, nind,to_make=0; 
      cin>>N>>M;
      string made[10000], tomake[M];
      for(int nn=0;nn<N;nn++) cin>>made[nn];
      nind = N;
      for(int mm=0;mm<M;mm++) cin>>tomake[mm];
     
      for(int ii=0;ii<M;ii++){
        int psl =1;
        //cout<<"hellp"<<endl;
        while(psl!=string::npos && psl<tomake[ii].size()){      
          int sl = tomake[ii].find("/",psl);
          if(sl==string::npos){sl= tomake[ii].size();}
          string str = tomake[ii].substr(0,sl);
         //cout<<"sl"<<sl<<"str to make"<<str<<endl;
          int jj =0;
          for(jj=0; jj<nind;jj++)
             if(made[jj] == str ) break;
          if(jj == nind){made[nind++]=str; to_make++;}
          psl=sl+1;
        }
         
          
      }
     cout <<"Case #"<<cc<<": "<<to_make<<endl;
     }    
} 
