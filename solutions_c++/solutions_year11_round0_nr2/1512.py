#include<iostream>
using namespace std;
int main(){
    int T,i,j,k,C,D,N,l,flag,a;
    char CC[36][4],DD[28][3],List[100],NN[100];
    cin>>T;
    for(i=0;i<T;++i){
                     cin>>C;
                     for(k=0;k<C;++k)
                     cin>>CC[k];
                     cin>>D;
                     for(k=0;k<D;++k)
                     cin>>DD[k];
                     cin>>N;
                     if(N>0)
                     cin>>NN;
                     l=0;
                     for(j=0;j<N;++j){
                                      List[l]=NN[j];
                                      ++l;
                                      if(l>1){
                                              flag=0;
                                              for(a=0;a<C;++a){
                                                       if((CC[a][0]==List[l-1] && CC[a][1]==List[l-2]) ||(CC[a][1]==List[l-1] && CC[a][0]==List[l-2])){
                                                                            List[l-2]=CC[a][2];
                                                                            --l;
                                                                            flag=1;
                                                                            break;                     
                                                       }
                                                                                     
                                              }
                                              if(flag==0){
                                              for(a=0;a<D;++a){
                                                      if(DD[a][0]==List[l-1]){
                                                                           for(k=0;k<l-1;++k){
                                                                                              if(DD[a][1]==List[k])
                                                                                                                l=0;                   
                                                                           }                     
                                                      }
                                                      else if(DD[a][1]==List[l-1]){
                                                                           for(k=0;k<l-1;++k){
                                                                                              if(DD[a][0]==List[k])
                                                                                                                l=0;                   
                                                                           }                     
                                                      }        
                                              }}        
                                      }
                                                               
                     }
                     cout<<"Case #"<<i+1<<": [";
                     for(k=0;k<l;++k){
                                      cout<<List[k];
                                      if(k<l-1)
                                      cout<<", ";
                     }cout<<"]\n";
    }   
}
