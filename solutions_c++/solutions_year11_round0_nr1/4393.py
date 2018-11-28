
//CODER: Adolfo Ccanto 
#include<iostream>
#include<stdio.h>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<algorithm>
#include<sstream>
#include<stack>
#include<math.h>
#include<string>

#define F(i,a,b) for(int i=a;i<b;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define pii pair<int,int>

#define FE(it,sto) for(typeof(sto.begin())it=sto.begin();it!=sto.end();++it)

// Les
// speedy Sub pitJad
using namespace std;

int main(){
 freopen("A-large (1).in","r",stdin);
 freopen("A-large (1).out","w",stdout);
 
 
 int t;
 cin>>t;
 F(i,1,t+1){
   int k;
   cin>>k;
   char c; int x;
   int b=1,o=1;
   int tiempo=0;
   long long ad=0;
   char ant;
   bool ok=true;
   while(k--){
    cin>>c>>x;
     if(ok){
      ant=c;
      ok=false;       
     }          
     if(c=='B'){
        int q=abs(x-b);
        
        if(c==ant){
          tiempo+=abs(x-b)+1;
          ad+=abs(x-b)+1;           
        }
        else{
          
          if(q<=tiempo)    
          {  ad++;
             tiempo=1;  
          }
          else{
             ad+=(q-tiempo)+1;
              tiempo=q-tiempo+1;     
          }    
        } 
        b=x;
        ant=c; 
     }    
     else{
        int q=abs(x-o);
        
        if(c==ant){
          tiempo+=abs(x-o)+1;
          ad+=abs(x-o)+1;        
        }
        else{
          //tiempo=0;
          if(q<=tiempo)    
          {  ad++;
             tiempo=1;  
          }
          else{
             ad+=(q-tiempo)+1;
              tiempo=q-tiempo+1;     
          }    
        }
        ant=c;
        o=x;
        
        
     }     
   }
            
            
   cout<<"Case #"<<i<<": "<<ad<<endl;           
 }
}
