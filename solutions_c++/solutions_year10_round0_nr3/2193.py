#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
ofstream fout("pro3.out");
long long T,R,K,N;
long long num[1001];
long long cnt;
          
void solve(){
     int now=0;
     cnt=0;
     long long sum=0;
     for(int i=0;i<R;i++){
             sum=0;
             int co=1;
             while(1){
                      sum=sum+num[now];
                      if(sum>K&&co<=N){
                                sum-=num[now];
                                break;
                      }else if(sum<=K && co==N){
                            now=0;
                            break;
                      }
                      now=(now+1)%N;
                      co++;
             }
             cnt+=sum;           
     }
}                                              
int main(){
    cin>>T;
    for(int i=1;i<=T;i++){
            cnt=0;
            cin>>R>>K>>N;
            for(int j=0;j<N;j++) cin>>num[j];
            solve();
            fout<<"Case #"<<i<<": "<<cnt<<endl;
    }
}
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                      
    
