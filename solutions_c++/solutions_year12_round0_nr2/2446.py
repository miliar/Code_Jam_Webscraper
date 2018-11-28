#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int q,test,n,s,p,ar[110],a,b,c;

int solve(){
     int res=0;
     sort(ar,ar+n); 
     for(int i=0;i<n;i++)
      {
         a=b=c=ar[i]/3;  
         q=ar[i]%3;
          if(q==0){
             if(a>=p)
             res++;
             else
             if(a<p&&s>=1&&a+1>=p&& a>0)
             {res++;s-=1;}         
          }
          else
          if(q==1){
             if(a>=p)
             res++;
             else
             if(a<p&&a+1>=p)
             res++;         
          }
          else
          if(q==2)
          {
             if(a>=p)
             res++;
             else
             if(a<p&& a+1>=p)
             res++;
             else
             if(s>=1&&a+2>=p)
             {res++;s-=1;}        
          }
      } 
               return res; 

}    

void input(){

   ifstream cin("b-small.in");
   ofstream cout("b-small.out");
      
   cin>>test;
   for(int i=1;i<=test;i++){
     cin>>n>>s>>p;    
     for(int j=0;j<n;j++)
     cin>>ar[j];   
     cout<<"Case #"<<i<<": "<<solve()<<endl;   
   }     
}

int main(int argc, char *argv[])
{
     input();
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
