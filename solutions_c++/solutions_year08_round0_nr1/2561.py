#include<cstdio>
#include<iostream>
#include<string>
#include<cstdlib>
#include<sstream>
#include<cstring>
#include<map>

using namespace std;


bool completo(map<string,int> str, string s[],int S)
{
   int i;
   
   for(i=0;i<S;i++)
    if(str[s[i]]==0) return false;   
     
   return true;  
} 




int Calcula(string s[],string q[],int S,int Q)
{int i,j,cont=0;
  
map<string,int> str;  


  
  for(i=0;i<Q;i++)  
   {
      if(!str[q[i]]) str[q[i]]=1;              
                    
     if( completo(str,s,S) ) 
     {
      for(j=0;j<S;j++)   
        str[s[j]]=0;  
      
      cont++;               
      str[q[i]]=1;
     }               
                    
   } 
    
    
 return cont;   
}


int main()
{
int N,S,Q,i,j,game=1;

cin>>N;


for(i=0;i<N;i++)
{string s[1000],q[2000];
   

cin>>S;


getchar();  
  for(j=0;j<S;j++)
  getline(cin,s[j]);


   cin>>Q;
   


getchar();

for(j=0;j<Q;j++)
  getline(cin,q[j]);  
  

int x=Calcula(s,q,S,Q);         
   cout<<"Case #"<<game<<": "<<x<<endl;       
game++;

}
      

return 0;    
}
