#include<iostream>
using namespace std;
int P[100];
char R[100];



int eval(int a){
    return((a<0)?0:a);
    }

int solve(){
     int N,i;
     char now,prev;
     int prevB=1,prevO=1,nextB=1,nextO=1;
     cin>>N;
     for(i=0;i<N;i++){
                cin>>R[i]>>P[i];
                }
     int sumO=0,sumB=0,tempO=0,tempB=0;
     for(i=0;i<N;i++){ if(i==0) prev=R[i];
                       now=R[i];
                      if(now=='B'){
                                   nextB=P[i];
                                   if(prev=='O')
                                   { tempB=eval(abs(nextB-prevB)-tempO)+1;
                                    sumO+=tempO;
                                    tempO=0;
                                    }
                                    else{
                                         tempB+=abs(nextB-prevB)+1; 
                                         }
                                    prevB=nextB;
                                    prev='B';

}
                      
                      if(now=='O'){
                                   nextO=P[i];
                                   if(prev=='B')
                                   { tempO=eval(abs(nextO-prevO)-tempB)+1;
                                    sumB+=tempB;
                                    tempB=0;
                                    }
                                    else{
                                         tempO+=abs(nextO-prevO)+1;
                                         
                                         }
                                    prevO=nextO;
                                    prev='O';

                                     }
                                     }
     return (sumO+sumB+tempO+tempB);
     
     }

int main(){
    int times,i=0;
    cin>>times;
    for(int i=1;i<=times;i++){
                   cout<<"Case #"<<i<<": "<<solve();
                   if(i!=times) cout<<endl;
                   }
    return 0;
    }
