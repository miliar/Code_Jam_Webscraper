#include<iostream>
#include<stdio.h>
using namespace std;
int point[1005][1005];
int testing[1005];
int N;
int found;

void recurse(int T){
     for(int i=0;i<N;i++){
             if( point[T][i] ){
                 if( testing[i] ){
                     found=1;
                     return;
                 }
                 testing[i]=1;
                 recurse(i);
             }
     }
}        
               
     
int main(){
    int cases;
    cin>>cases;
    
    int mark[1005];
    for(int kases=1; kases<=cases; kases++){
            
            cin>>N;
            for(int i=0;i<N;i++){
                    for(int j=0;j<N;j++)
                            point[i][j]=0;
                    mark[i]=0;
            }
                             
            for(int i=0;i<N;i++){
                    int num;cin>>num;
                    for(int j=0;j<num;j++){
                            int to;cin>>to;
                            point[i][to-1]=1;
                            mark[to-1]=1;
                    }
            }        
            
            found=0;
            
            for(int i=0;i<N;i++){
                    for(int j=0;j<N;j++)
                            testing[j]=0;
                    testing[i]=1;
                    if( !mark[i] ){
                    //    cout<<i<<endl;
                        recurse(i);
                        if(found){
                            cout<<"Case #"<<kases<<": Yes\n";
                            break;
                        }                    
                    }
            }
            
            if(!found)
                  cout<<"Case #"<<kases<<": No\n";      
    }
    return 0;   
}
