#include<iostream>
using namespace std;
int main(){
    int T,N,i,j;
    long unsigned int C[1000],S,m,Ex;
    cin>>T;
    for(i=0;i<T;++i){
                     cin>>N;
                     for(j=0;j<N;++j)
                                     cin>>C[j];
                     S=0,Ex=0,m=10000000;
                     for(j=0;j<N;++j){
                                      S=S + C[j];
                                      Ex=Ex ^ C[j];
                                      if(m>C[j])
                                                m=C[j];
                     }
                     if(Ex != 0)
                     cout<<"Case #"<<i+1<<": NO\n";
                     else
                     cout<<"Case #"<<i+1<<": "<<S-m<<"\n";      
    }   
}
