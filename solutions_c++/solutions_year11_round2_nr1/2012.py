#include<iostream>
using namespace std;
int main(){
    int T,N,i,j,total,win,k,l,ototal;
    double WP[100],OWP[100],OOWP[100];
    char input[100][100];
    cin>>T;
    for(i=1;i<=T;++i){
                      cin>>N;
                      for(j=0;j<N;++j){
                                       for(k=0;k<N;++k)
                                       cin>>input[j][k];                 
                      }  
                      for(j=0;j<N;++j){
                                       total=0;win=0;
                                       for(k=0;k<N;++k){
                                                        if(input[j][k]=='1'){
                                                                             total++; win++;
                                                        }
                                                        else if(input[j][k]=='0')
                                                        total++;
                                                        
                                       }
                                       WP[j]=win*1.0/total;
                      } 
                      for(l=0;l<N;++l){
                                       OWP[l]=0.0;ototal=0;
                                       for(j=0;j<N;++j){
                                                        
                                                        if(input[l][j]!='.'){
                                                                 ototal++;
                                                                 total=0;win=0;
                                                                 for(k=0;k<N;++k){
                                                                                  if(l!=k){
                                                                                           if(input[j][k]=='1'){
                                                                                           total++; win++;
                                                                                           }
                                                                                  else if(input[j][k]=='0')
                                                                                  total++;
                                                                                  }
                                                                 }
                                                        OWP[l]+=win*1.0/total;
                                                        }
                                                        
                                       }
                                       OWP[l]=OWP[l]/ototal;
                      }
                      cout<<"Case #"<<i<<": \n";
                       for(l=0;l<N;++l){
                                       OOWP[l]=0.0;ototal=0;
                                       for(j=0;j<N;++j){
                                                        
                                                        if(input[l][j]!='.'){
                                                                 ototal++;
                                                                 OOWP[l]+=OWP[j]; 
                                                        }
                                       }
                                       OOWP[l]=OOWP[l]/ototal;
                                       cout<<0.25*WP[l]+0.50*OWP[l]+0.25*OOWP[l]<<"\n";   
                       }  
                              
    }    
}
