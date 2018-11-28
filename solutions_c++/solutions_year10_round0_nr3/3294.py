#include<iostream>
#include<string.h>
using namespace std;

const int maxn=1024;
int T;
int N,L,P;
unsigned long long R,K;
unsigned long long n[maxn<<1];
unsigned long long s[maxn<<1];
bool used[maxn];

void pcmp()
{ 
     P=1; 
     memset(used,0,sizeof(used));
 for(int i=1;P<=R;i++)
  {  
    int x=i%N;
     if(x==0) x=N;
         
  if(s[P]-s[P-1]+n[x]>K || used[x]) { P++; s[P]=s[P-1]; memset(used,0,sizeof(used)); }    
   s[P]=s[P]+n[x];
    used[x]=1;
   }  
}
  
unsigned long long sol()
{ 
  unsigned long long ans=0;       
 if(R<=L) return s[L];
 
  ans=s[L];
    R=R-L;
    P=P-L; 
   
   ans=ans+(s[P+L]-s[L])*(R/P)+s[(R%P)+L]-s[L];

return ans;
}
               
int main()
{
 cin>>T;
  
  for(int i=1;i<=T;i++)
   {
   memset(s,0,sizeof(s));       
          
   cin>>R>>K>>N;
    
    for(int j=1;j<=N;j++)
     cin>>n[j];
                     
       pcmp();      
       
     
     cout<<"Case #"<<i<<": "<<s[R]<<endl; 
      
    }
    
return 0;
}    
