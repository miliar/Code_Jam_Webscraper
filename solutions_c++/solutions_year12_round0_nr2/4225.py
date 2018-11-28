#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int T,N,S,p,go_dancer,i,j,pass;
    cin>>T;
    for(i=0;i<T;i++){

                     cin>>N;
                     cin>>S;
                     cin>>p;
                     pass=0;
                     
                     if(p==0){
                              for(j=0;j<N;j++) cin>>go_dancer;
                              pass=N;
                              cout<<"Case #"<<i+1<<": "<< pass<<endl;
                              continue;
                              }
                     
                     for(j=0;j<N;j++){
                                      cin>>go_dancer;
                                      if(p==1){
                                               if(go_dancer>0) pass++;
                                               continue;
                                               }
                                      else if(go_dancer>=((3*p)-2)) pass++;
                                      else if((go_dancer>=((3*p)-4))&&(S>0)) {pass++; S--;}
                                      }
                     cout<<"Case #"<<i+1<<": "<< pass<<endl;
                     }
    return EXIT_SUCCESS;
}
