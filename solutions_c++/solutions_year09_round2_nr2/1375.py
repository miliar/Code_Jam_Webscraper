#include<iostream>
using namespace std;

int val(int n1,int n2)
{
 int a[20],b[20];
 memset(a,0,sizeof a);
 memset(b,0,sizeof b);
 
 while(n1)
 {
   a[n1%10]++;       
          
   n1/=10;         
 }   
    
    
    
 while(n2)
 {
   b[n2%10]++;       
          
   n2/=10;         
 }   int i;
    
    for(i=1;i<15;i++)
    if(a[i]!=b[i])return 0;
    return 1;
}
int T;

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("tt.out","w",stdout);
    cin>>T;
    for(int k=1;k<=T;k++)
    {int N;
              cin>>N;
              int i;
              for(i=N+1;i<50000000;i++)  
              {
                if(val(i,N))break;                        
                                      
                                      
              }        
              cout<<"Case #"<<k<<": "<<i<<endl;
              
              
              
    }
    
    
    
    
 return 0;   
}
