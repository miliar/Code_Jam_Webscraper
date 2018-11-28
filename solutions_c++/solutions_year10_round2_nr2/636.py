#include<iostream.h>
#include <fstream.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

int main(){
    freopen("B-large.in", "r", stdin);
//	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
    
    int t,caseno=0;
    cin>>t;
    
    
    while(t--){
               caseno++;
               int n,k,b,time,ans=0,i,check=0;
               cin>>n>>k>>b>>time;
               int pos[n+1],speed[n+1],reach[n+1],got=0;
               
               for(i=0;i<n;i++)
                               cin>>pos[i];
                               
               for(i=0;i<n;i++)
                               cin>>speed[i];
                               
               for(i=0;i<n;i++){
                       int temp;
                       temp=pos[i]+speed[i]*time;
                        
                          reach[i]=temp;
                       if(temp>=b){
                                  
                                   check++;
                                 
                       }
                                  
                       
               }
               //cout<<check;
               if(check<k){
                           
                          cout<<"Case #"<<caseno<<": IMPOSSIBLE"<<endl;
                          continue;
               }
                 int loop=0;        
               for(i=n-1;i>=0;i--)
               {
                   if(got>=k)
                             break;
                   if(reach[i]>=b){
                                 
                                     ans+=loop;
                                     got++;
                                     continue;
                   }
                 
                   loop++;
                                              
               }
               
               cout<<"Case #"<<caseno<<": "<<ans<<endl;           
               
    }
       
}

