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
string global;

int steps(string& str,map<string,int>& create){
    
    int ans;
    if(create.find(str)!=create.end())
                          return 0;
    
    int temp=str.find_last_of("//");
    string parent=str.substr(0,temp);
    if(create.find(str)!=create.end()){
                          ans=create[parent]+1;
                          create[str]=ans;
                          return ans;
    }
    if(temp==0){
     create[str]=1;
     return 1;
     }
     
     ans=steps(parent,create)+1;
     create[str]=ans;
     return ans;
        
    
    
    
}



int main(){
    freopen("A-large.in", "r", stdin);
	
	freopen("A-small.out", "w", stdout);
    
    int t,caseno=0;
    cin>>t;
    int n,m;
    
    while(t--){
               caseno++;
               int n,m,i,ans=0;
               cin>>n>>m;
               global="";
               map<string,int> create;
               string given[n+1],tomake[m+1];
               for(i=0;i<n;i++){
                               cin>>given[i];
                               create[given[i]]=0;
               }
               for(i=0;i<m;i++){
                               cin>>tomake[i];                  
               }
               
               for(i=0;i<m;i++)
               {
                               ans+=steps(tomake[i],create);
               
               }
               cout<<"Case #"<<caseno<<": "<<ans<<endl;
    }
       
}


