#include<iostream>
using namespace std;
int main(){
    int N,P,G,i,T,j;
    cin>>T;
    for(i=0;i<T;++i){
           cin>>N>>P>>G;
           if(P==0 && G==100) cout<<"Case #"<<i+1<<": Broken\n";
           else if(P>0 && P<100 && (G==0 || G==100)) cout<<"Case #"<<i+1<<": Broken\n";
           else if(P==100 && G==0) cout<<"Case #"<<i+1<<": Broken\n";
           else {
                if(P==100)
                          cout<<"Case #"<<i+1<<": Possible\n";
                else{
                     for(j=1;j<=N;j=j+1){
                                         if(j*1.0*P/100-j*P/100 == 0){
                                                                cout<<"Case #"<<i+1<<": Possible\n";
                                                                break;
                                         }
                     }
                     if(j>N)
                            cout<<"Case #"<<i+1<<": Broken\n";     
                }     
           }                
    }
}
