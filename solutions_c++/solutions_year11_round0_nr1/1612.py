#include<iostream>
using namespace std;
int main(){
    int Tm,BP,OP,lBT,lOT,T,N,P[200],i,j,d;
    char R[200];
    cin>>T;
    for(i=0;i<T;++i){
                     cin>>N;
                     for(j=0;j<N;++j)
                                     cin>>R[j]>>P[j];
                     Tm=0,lBT=0,lOT=0,OP=1,BP=1;
                     for(j=0;j<N;++j){
                                      if(R[j]=='O'){
                                                    d=(P[j]>OP ?(P[j]-OP) : (OP-P[j]));
                                                    if(d>(Tm-lOT))
                                                                 Tm=Tm+d-(Tm-lOT)+1;
                                                    else
                                                        Tm=Tm+1;
                                                    lOT=Tm;
                                                    OP=P[j];              
                                      }                 
                                      if(R[j]=='B'){
                                                    d=(P[j]>BP ?(P[j]-BP) : (BP-P[j]));
                                                    if(d>(Tm-lBT))
                                                                 Tm=Tm+d-(Tm-lBT)+1;
                                                    else
                                                        Tm=Tm+1;
                                                    lBT=Tm;
                                                    BP=P[j];              
                                      }
                     }
                     cout<<"Case #"<<i+1<<": "<<Tm<<"\n";
    }    
}
