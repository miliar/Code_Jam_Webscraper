#include<iostream>
using namespace std;
int main(){
    int T,R,C,i,j,k,flag;
    char input[50][50];
    cin>>T;
    for(i=1;i<=T;++i){
                      cin>>R>>C;
                      for(j=0;j<R;++j)
                                      for(k=0;k<C;++k)
                                                      cin>>input[j][k];
                      flag=0;
                      for(j=0;j<R;++j){
                                       for(k=0;k<C;++k){
                                                        if(input[j][k]=='#' && (j==R-1 || k==C-1)){
                                                                            flag=1;
                                                                            cout<<"Case #"<<i<<":\nImpossible\n";   
                                                                            break;
                                                        }
                                                        else if(input[j][k]=='#'){
                                                             if(input[j][k+1]=='#' && input[j+1][k]=='#' && input[j+1][k+1]=='#'){
                                                                                   input[j][k]='/';
                                                                                   input[j][k+1]='\\';
                                                                                   input[j+1][k]='\\';
                                                                                   input[j+1][k+1]='/';
                                                             }
                                                             else{
                                                                  flag=1;
                                                                  cout<<"Case #"<<i<<":\nImpossible\n";   
                                                                  break;
                                                                  }
                                                        }
                                                                                             
                                       }  
                                       if(flag==1)
                                       break;               
                      }
                      if(flag==0){
                                  cout<<"Case #"<<i<<":\n";
                       for(j=0;j<R;++j){
                                      for(k=0;k<C;++k){
                                                      cout<<input[j][k];
                                      }
                                      cout<<"\n";
                       }        
                       }
    }   
}
