#include<iostream>
using namespace std;
int main()
{
    int T,N,i,j,k,k1,t,x,A,A1,B,B1,R;
    int input[20][2];
    cin>>T;
    for(i=0;i<T;i++) {
                      cin>>N;
                      for(j=0;j<N;j++) cin>>input[j][0];
                      R=0;
                      for(k=0;k<(2<<N-1);k++) {
                                               t=0;
                                               k1=k;
                                               while(k1) {
                                                          input[t][1]=k1%2;
                                                          k1/=2;
                                                          t++;                                                         
                                                         }
                                               for(;t<N;t++) input[t][1]=0;
                                               A=B=A1=B1=0;
                                               for(x=0;x<N;x++) if(input[x][1]) {A^=input[x][0];A1+=input[x][0];} else {B^=input[x][0];B1+input[x][0];}
                                               if(A==B && A) {
                                                         if(A1>R) R=A1;
                                                         if(B1>R) R=B1;
                                               }
                                              }
                      cout<<"Case #"<<i+1<<": ";
                      if(R) cout<<R<<endl; else cout<<"NO"<<endl;
                     }
    return 0;
}
